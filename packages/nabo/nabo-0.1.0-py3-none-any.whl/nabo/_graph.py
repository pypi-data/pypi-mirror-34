import h5py
from typing import List, Dict
import networkx as nx
import numpy as np
from fa2 import ForceAtlas2
from itertools import combinations
import operator
import os
from collections import Counter
import pandas as pd
import hac

__all__ = ['Graph']


class Graph(nx.Graph):
    """
    Class for storing Nabo's SNN graph. Inherits from networkx's `Graph` class

    """

    def __init__(self):
        super().__init__()
        self.refName = None
        self.refNodes: List[str] = []
        self.refG = None
        self.targetNames: List[str] = []
        self.targetNodes: Dict[str, List[str]] = {}
        self.deTestCells: List[str] = None
        self.deCtrlCells: List[str] = None
        self._agglomDendrogram = None

    def load_from_h5(self, fn: str, name: str, kind: str) -> None:
        """
        Loads a graph saved by `Mapping` class in HDF5 format

        :param fn: Path to HDF5 file
        :param name: Label/name of sample used in Mapping object. This
                     function assumes that the group in HDF5 containing
                     graph data is named: `name` + '_graph'
        :param kind: Can have a value of either 'reference' or 'target'.
                     Only be one sample can have kind='reference' for an
                     instance of this class
        :return: None
        """
        if os.path.exists(fn) is False:
            raise IOError('ERROR: File %s does not exist' % fn)
        if kind == 'reference':
            if self.refName is not None:
                raise ValueError('ERROR: A reference kind is already loaded')
        elif kind == 'target':
            if name in self.targetNames:
                raise ValueError('ERROR: %s target group already present in '
                                 'graph' % name)
            if self.refName is None:
                raise ValueError('ERROR: Please load reference kind first')
        else:
            raise ValueError('ERROR: Kind can be either "reference" or '
                             '"target"')
        try:
            h5 = h5py.File(fn, mode='r')
        except (IOError, OSError):
            raise IOError('ERROR: Unable to open file %s' % fn)
        grp = name + '_graph'
        if grp not in h5:
            h5.close()
            raise KeyError('ERROR: Group %s not found in HDF5 file %s'
                           % (grp, fn))
        attrs = {'kind': kind, 'name': name}
        existing_nodes = {x: None for x in self.nodes()}
        new_nodes = []
        for node in h5[grp]:
            if node in existing_nodes:
                print('WARNING: node %s already present in the graph. Will '
                      'not add.' % node)
            else:
                new_nodes.append(node)
                self.add_node(node, **attrs)
                for j in h5[grp][node]:
                    node2 = j[0].decode('UTF-8')
                    weight = float(j[1].decode('UTF-8'))
                    self.add_edge(node, node2, weight=weight)
        h5.close()
        if kind == 'reference':
            self.refName = name
            self.refNodes = new_nodes
            self.refG = self.subgraph(self.refNodes)
        else:
            self.targetNames.append(name)
            self.targetNodes[name] = new_nodes
        return None

    def load_from_gml(self, fn: str) -> None:
        """
        Load data from GML format file. It is critical that this graph was
        generated using Nabo's `Mapping` class.

        :param fn: Full path of GML file
        :return: None
        """
        if len(self.nodes) > 0:
            raise ValueError('ERROR: The graph already contains nodes. '
                             'Cannot load GML file on this object.')
        if os.path.exists(fn) is False:
            raise IOError('ERROR: File %s does not exist' % fn)
        try:
            g = nx.read_gml(fn)
        except (IOError, OSError):
            raise IOError('ERROR: Could open the file %s. Make sure the file '
                          'is in GML format' % fn)
        for i in g.nodes(data=True):
            attrs = i[1]
            if 'kind' not in attrs or 'name' not in attrs:
                self.clear()
                raise ValueError('ERROR: Attributes "kind" and/or "name" '
                                 'not found for one or more cells. Make '
                                 'sure that the GML was saved using Nabo')
            if attrs['kind'] == 'reference':
                if self.refName is None:
                    self.refName = attrs['name']
                else:
                    if self.refName != attrs['name']:
                        self.clear()
                        raise ValueError('ERROR: Multiple reference samples '
                                         'found. Please make sure you saved '
                                         'the GML with Nabo.')
                self.refNodes.append(i[0])
            elif attrs['kind'] == 'target':
                if attrs['name'] not in self.targetNames:
                    self.targetNames.append(attrs['name'])
                    self.targetNodes[attrs['name']] = []
                self.targetNodes[attrs['name']].append(i[0])
            else:
                self.clear()
                raise ValueError('ERROR: Kind can only be either "reference" '
                                 'or "target"')
            self.add_node(i[0], **i[1])
        for i in g.edges(data=True):
            self.add_edge(i[0], i[1], weight=i[2]['weight'])
        self.refG = self.subgraph(self.refNodes)
        return None

    def save_graph(self, save_name: str) -> None:
        """
        Save graph in GML format

        :param save_name: Output filename with path
        :return: None
        """
        nx.write_gml(self, save_name)
        return None

    def set_ref_layout(self, niter: int = 500, verbose: bool = True,
                       init_pos: dict = None,
                       outbound_attraction_distribution: bool = True,
                       edge_weight_influence: float = 1.0,
                       jitter_tolerance: float = 1.0,
                       barnes_hut_optimize: bool = True,
                       barnes_hut_theta: float = 1.2,
                       scaling_ratio: float = 1.0,
                       strong_gravity_mode: bool = False,
                       gravity: float = 1.0) -> None:
        """
        Calculates a 2D graph layout using ForceAtlas2 algorithm.
        The ForceAtlas2 implementation being used here will not prevent
        nodes in the graph from overlapping with each other. We aim to
        improve this in the future.

        :param niter: Number of iterations (default: 500)
        :param verbose: Print the progress (default: True)
        :param init_pos: Initial positions of nodes
        :param outbound_attraction_distribution:
        :param edge_weight_influence:
        :param jitter_tolerance:
        :param barnes_hut_optimize:
        :param barnes_hut_theta:
        :param scaling_ratio:
        :param strong_gravity_mode:
        :param gravity:
        :return: None
        """
        force_atlas = ForceAtlas2(
            outboundAttractionDistribution=outbound_attraction_distribution,
            edgeWeightInfluence=edge_weight_influence,
            jitterTolerance=jitter_tolerance,
            barnesHutOptimize=barnes_hut_optimize,
            barnesHutTheta=barnes_hut_theta, scalingRatio=scaling_ratio,
            strongGravityMode=strong_gravity_mode, gravity=gravity,
            verbose=verbose)
        pos = force_atlas.forceatlas2_networkx_layout(
            self.refG, pos=init_pos, iterations=niter)
        pos_array = np.array(list(pos.values())).T
        min_x, min_y = pos_array[0].min(), pos_array[1].min()
        max_x, max_y = pos_array[0].max(), pos_array[1].max()
        pos = {k: ((v[0] - min_x) / (max_x - min_x),
                   (v[1] - min_y) / (max_y - min_y)) for k, v in pos.items()}
        for node in pos:
            self.nodes[node]['pos'] = pos[node]
        return None

    @property
    def clusters(self) -> Dict[str, str]:
        ret_val = {}
        for i in self.refG.nodes(data=True):
            if 'cluster' in i[1]:
                ret_val[i[0]] = i[1]['cluster']
            else:
                ret_val[i[0]] = 'NA'
        return ret_val

    def make_clusters(self, n_clusters: int) -> None:
        """
        Performs graph agglomerative clustering using algorithm in Newman
        2004

        :param n_clusters: Number of clusters
        :return: None
        """
        if self._agglomDendrogram is None:
            clusterer = hac.GreedyAgglomerativeClusterer()
            self._agglomDendrogram = clusterer.cluster(self.refG)
        cluster_list = self._agglomDendrogram.clusters(n_clusters)
        for n, node_group in enumerate(cluster_list):
            for node in node_group:
                clust_num = n + 1
                self.nodes[node]['cluster'] = str(clust_num)
        return None

    def import_clusters(self, cluster_dict: Dict[str, str] = None,
                        from_csv: str = None, csv_sep: str = ',') -> None:
        """
        Import cluster information for reference cells.

        :param cluster_dict: Dictionary with cell names as keys and cluster
                             number as values. Cluster numbers should start
                             from 1
        :param from_csv: Filename containing cluster information. Make
                         sure that the first column contains cell names and
                         second contains the cluster labels.
        :param csv_sep: Separator for CSV file (default: ',')
        :return: None
        """
        skipped_nodes = 0
        if cluster_dict is None and from_csv is None:
            raise ValueError("ERROR: provide a value for either "
                             "'cluster_dict' or 'from_csv'")
        if cluster_dict is not None and from_csv is not None:
            raise ValueError("ERROR: provide a value for only ONE of either"
                             "'cluster_dict' or 'from_csv'")
        if from_csv is not None:
            df = pd.read_csv(from_csv, index_col=0, sep=csv_sep)
            cluster_dict = df[df.columns[0]].to_dict()
            cluster_dict = {k.upper()+'_'+self.refName: v for
                            k, v in cluster_dict.items()}
        for node in cluster_dict:
            try:
                self.nodes[node]['cluster'] = str(cluster_dict[node])
            except KeyError:
                skipped_nodes += 1
        if skipped_nodes > 0:
            print('WARNING: %d cells do not exist in the reference graph and '
                  'their cluster info was not imported.' % skipped_nodes)

    def calc_modularity(self) -> float:
        """
        Calculates modularity of the reference graph. The clusters should have
        already been defined.

        :return: Value between 0 and 1
        """
        partition = {}
        for k, v in self.clusters.items():
            if v not in partition:
                partition[v] = {}
            partition[v][k] = None
        partition = list(partition.values())
        if sum([len(x) for x in partition]) != len(self.refG):
            raise AssertionError('ERROR: Not all reference nodes have been '
                                 'assigned to a cluster. Cannot calculate '
                                 'modularity!')
        # noinspection PyCallingNonCallable
        w_degree = dict(self.refG.degree(weight='weight'))
        norm = 1 / (2 * self.refG.size(weight='weight'))
        q = 0
        for p in partition:
            for i in p:
                t = -w_degree[i] * norm
                q += sum([t * w_degree[x] for x in p])
                q += sum([self.refG[i][x]['weight']
                          for x in self.refG[i] if x in p])
        return q * norm

    def import_layout(self, graph) -> None:
        """
        Copies 'pos' attribute values (x/y coordinate tuple) from input
        graph into the to reference cells.

        :param graph: Graph
        :return: None
        """
        pos_dict = {}
        for i in graph.refG.nodes(data=True):
            pos_dict[i[0]] = i[1]['pos']
        for node in self.refNodes:
            if node in pos_dict:
                self.nodes[node]['pos'] = pos_dict[node]
            else:
                self.nodes[node]['pos'] = (0, 0)
        return None

    @staticmethod
    def get_score_percentile(score: Dict[str, int], p: int) -> float:
        """
        Get value for at a given percentile

        :param score: Mapping score or any other dictionary
                      where values are numbers
        :param p: Percentile
        :return: Percentile value
        """
        return np.percentile(list(score.values()), p)

    def get_mapping_score(self, target: str, min_weight: float = 0,
                          min_score: float = 0, weighted: bool = True,
                          by_cluster: bool = False,
                          sorted_names_only: bool = False,
                          top_n_only: int = None,
                          all_nodes: bool = True, score_multiplier: int = 1000,
                          ignore_nodes: List[str] = None,
                          remove_suffix: bool = False):
        """
        Calculate a weighted/unweighted degree of incident target nodes on
        reference nodes.

        :param target: Target sample name
        :param min_weight: Ignore a edge if edge weight is smaller then this
                           value in the SNN graph. Only applicable if
                           calculating a weighted mapping score
        :param min_score: If score is smaller then reset score to zero
        :param weighted: Use edge weights if True
        :param by_cluster: If True, then combine scores from nodes of same
                           cluster into a list. The keys are cluster number
                           in the output dictionary
        :param sorted_names_only: If True, then return only sorted list of
                                  base cells from highest to lowest mapping
                                  score. Cells with mapping score less than
                                  `min_score` are not reported (default: False)
        :param top_n_only: If sorted_names_only is True and an integer value is
                           provided then this method will return top n
                           number of nodes sorted based on score. min_score
                           value will be ignored.
        :param all_nodes: if False, then returns only nodes with non-zero
                          score (after resetting using min_score)
        :param score_multiplier: Score is multiplied by this number after
                                 normalizing for total number of target cells.
        :param ignore_nodes: List of nodes from 'target' sample to be
                             ignored while calculating the score (default:
                             None).
        :param remove_suffix: Remove suffix from cell names (default: False)
        :return: Mapping score
        """
        if by_cluster:
            if set(self.clusters.values()) == 'NA':
                raise ValueError('ERROR: Calculate clusters first using '
                                 '"make_clusters" or import clusters using '
                                 '"import_clusters"')
        if target not in self.targetNames:
            raise ValueError('ERROR: %s not present in graph' % target)
        score = {}
        if ignore_nodes is None:
            ignore_nodes = []
        if len(ignore_nodes) != 0:
            ignore_nodes = {x: None for x in ignore_nodes}
        for i in self.refNodes:
            score[i] = 0
            for j in self.edges(i, data=True):
                if j[1] in ignore_nodes:
                    continue
                if self.nodes[j[1]]['name'] == target:
                    if weighted:
                        if j[2]['weight'] > min_weight:
                            score[i] += j[2]['weight']
                    else:
                        score[i] += 1
        score = {k: score_multiplier * v / len(self.targetNodes[target])
                 for k, v in score.items()}

        if by_cluster:
            cluster_values = {x: [] for x in set(self.clusters.values())}
            for node in score:
                cluster_values[self.clusters[node]].append(score[node])
            return cluster_values

        if sorted_names_only:
            if top_n_only is not None:
                if top_n_only > len(score):
                    raise ValueError('ERROR: Value of top_n_only should be '
                                     'less than total number of nodes in '
                                     'reference graph')
                retval = [x[0] for x in sorted(score.items(),
                                               key=lambda x: x[1])][::-1][
                         :top_n_only]
            else:
                ms = {k: v for k, v in score.items() if v >= min_score}
                retval = [x[0] for x in sorted(ms.items(),
                                               key=lambda x: x[1])][::-1]
            if remove_suffix:
                return [x.rsplit('_', 1)[0] for x in retval]
            else:
                return retval
        if not all_nodes:
            retval = {k: v for k, v in score.items() if v >= min_score}
        else:
            retval = {k: v if v >= min_score else 0 for k, v in score.items()}
        if remove_suffix:
            return [x.rsplit('_', 1)[0] for x in retval]
        else:
            return retval

    def get_cells_from_clusters(self, clusters: List[str],
                                remove_suffix: bool = True) -> List[str]:
        """
        Get cell names for input cluster numbers

        :param clusters: list of cluster identifiers
        :param remove_suffix: Remove suffix from cell names
        :return: List of cell names
        """
        if set(self.clusters.values()) == 'NA':
            raise ValueError('ERROR: Calculate clusters first using '
                             '"make_clusters" or import clusters using '
                             '"import_clusters"')
        cells = []
        clusters = {str(x) for x in clusters}
        for k, v in self.clusters.items():
            if v in clusters:
                if remove_suffix:
                    cells.append(k.rsplit('_', 1)[0])
                else:
                    cells.append(k)
        return cells

    def classify_target(self, target: str, weight_frac: float = 0.5,
                        min_degree: int = 2, min_weight: float = 0.1,
                        cluster_dict: Dict[str, int] = None, na_label: str
                        = 'NA', ret_counts: bool = False) -> dict:
        """
        This classifier identifies the total weight of all the connections made
        by each target cell to each cluster (of reference cells). If a target
        cell has more than 50% (default value) of it's total connection weight
        in one of the clusters then the target cell is labeled to be from that
        cluster. One useful aspect of this classifier is that it will not
        classify the target cell to be from any cluster if it fails to reach
        the threshold (default, 50%) for any cluster (such target cell be
        labeled as '0' by default).

        :param target: Name of target sample
        :param weight_frac: Required minimum fraction of weight in a cluster
                            to be classified into that cluster
        :param min_degree: Minimum degree of the target node
        :param min_weight: Minimum edge weight. Edges with less weight
                           than min_weight will be ignored but will still
                           contribute to total weight.
        :param cluster_dict: Cluster labels for each reference cell
        :param na_label: Label for cells that failed to get classified
                           into any cluster
        :param ret_counts: It True, then returns number of target cells
                           classified to each cluster, else returns predicted
                           cluster for each target cell
        :return: Dictionary. Keys are target cell names and value their
                             predicted custer if re_Count is False. Otherwise,
                             keys are cluster labels and values are the number
                             of target cells classified to that cluster
        """
        if cluster_dict is None:
            if set(self.clusters.values()) == 'NA':
                raise ValueError('ERROR: Calculate clusters first using '
                                 '"make_clusters" or import clusters using '
                                 '"import_clusters"')
            cluster_dict = self.clusters
        clusts = set(cluster_dict.values())
        classified_clusters = []
        degrees = dict(self.degree)
        for i in self.targetNodes[target]:
            if degrees[i] < min_degree:
                classified_clusters.append(na_label)
                continue
            clust_weights = {x: 0 for x in clusts}
            tot_weight = 0
            for j in self.edges(i, data=True):
                if j[2]['weight'] > min_weight:
                    clust_weights[cluster_dict[j[1]]] += j[2]['weight']
                tot_weight += j[2]['weight']  # even low weight is added to
                # total weight to allow poor mappings to be penalized.
            max_clust = max(clust_weights.items(),
                            key=operator.itemgetter(1))[0]
            if clust_weights[max_clust] > (weight_frac * tot_weight):
                classified_clusters.append(max_clust)
            else:
                classified_clusters.append(na_label)
        if ret_counts:
            counts = Counter(classified_clusters)
            if na_label not in counts:
                counts[na_label] = 0
            for i in set(cluster_dict.values()):
                if i not in counts:
                    counts[i] = 0
            return counts
        else:
            return dict(zip(self.targetNodes[target], classified_clusters))

    def get_mapped_cells(self, target: str, ref_cells: str,
                         remove_suffix: bool = True) -> List[str]:
        """
        Get target cells that map to a given list of reference cells.

        :param target: Name of target sample
        :param ref_cells: List of reference cell names
        :param remove_suffix: If True then removes target name suffix from
                              end of node name
        :return: List of target cell names
        """
        if target not in self.targetNames:
            raise ValueError('ERROR: %s not present in graph!' % target)
        target_cells = {x: None for x in self.targetNodes[target]}
        mapped_cells = []
        for i in ref_cells:
            i = i + '_' + self.refName
            for j in self.edges(i):
                if j[1] in target_cells:
                    mapped_cells.append(j[1])
        mapped_cells = list(set(mapped_cells))
        if remove_suffix:
            return [x.rsplit('_', 1)[0] for x in mapped_cells]
        else:
            return mapped_cells

    def get_random_nodes(self, n: int) -> List[str]:
        """
        Get random list of nodes from reference graph.

        :param n: Number of nodes to return
        :return: A list of reference nodes
        """
        all_nodes = list(self.refNodes)
        if n >= len(all_nodes):
            raise ValueError('ERROR: n should be lower than total nodes in '
                             'reference graph')
        random_nodes = []
        for i in range(n):
            x = np.random.choice(all_nodes)
            random_nodes.append(x)
            all_nodes.remove(x)
        return sorted(random_nodes)

    def calc_contiguous_spl(self, nodes: List[str]) -> float:
        """
        Calculates mean of shortest path lengths between subsequent nodes
        provided in the input list in reference graph.

        :param nodes: List of nodes from reference sample
        :return: Mean shortest path length
        """
        spl = []
        for i in range(len(nodes) - 1):
            spl.append(nx.shortest_path_length(self.refG, nodes[i],
                                               nodes[i + 1]))
        return float(np.mean(spl))

    def calc_diff_potential(self,
                            r: Dict[str, float]=None) -> Dict[str, float]:
        """
        Calculate differentiation potential of cells.

        This function is a reimplementation of population balance analysis
        (PBA) approach published in Weinreb et al. 2017, PNAS.
        This function computes the random walk normalized Laplacian matrix
        of the reference graph, L_rw = I-A/D and then calculates a
        Moore-Penrose pseudoinverse of L_rw. The method takes an optional
        but recommended parameter 'r' which represents the relative rates of
        proliferation and loss in different gene expression states (R). If
        not provided then a vector with ones is used. The differentiation
        potential is the dot product of inverse L_rw and R

        :param r: Same as parameter R in the above said reference. Should be a
                  dictionary with each reference cell name as a key and its
                  corresponding R values.
        :return: V (Vector potential) as dictionary. Smaller values
                 represent less differentiated cells.
        """
        adj = nx.to_pandas_adjacency(self.refG, weight=False)
        degree = adj.sum(axis=1)
        lap = np.identity(adj.shape[0]) - adj / np.meshgrid(degree, degree)[1]
        ilap = np.linalg.pinv(lap)
        if r is None:
            r = np.ones(ilap.shape[0])
        return dict(zip(adj.columns, np.dot(ilap, r)))

    def get_k_path_neighbours(self, nodes: List[str], k_dist: int,
                              full_trail: bool = False,
                              trail_start: int = 0) -> List[str]:
        """
        Get set of nodes at a given distance

        :param nodes: Input nodes
        :param k_dist: Path distance from input node
        :param full_trail: If True then returns only nodes at k_dist path
                           distance else return all nodes upto k_dist (
                           default: False)
        :param trail_start: If full_trail is True, then the trail starts at
                            this path distance (default: 0).
        :return: List of nodes
        """

        def get_neighbours(g, n):
            g.remove_edges_from(list(combinations(n, 2)))
            n = list(set(n).intersection(list(g.nodes())))
            return list(set(sum([list(g.neighbors(x)) for x in n], [])))

        neighbours = [list(nodes)]
        # copying because will modify the graph
        ref_g = nx.Graph(self.refG)
        for i in range(k_dist):
            neighbours.append(get_neighbours(ref_g, neighbours[i]))
            ref_g.remove_nodes_from(neighbours[i])
        if full_trail:
            return sum(neighbours[1 + trail_start:], [])
        else:
            return neighbours[-1]

    def set_de_groups(self, target: str, min_score: float,
                      node_dist: int, from_clusters: List[str] = None,
                      full_trail: bool = False, trail_start: int = 1) -> None:
        """
        Categorises reference nodes into either 'Test', 'Control' or 'Other'
        group. Nodes with mapping score higher than `min_score` are
        categorized as 'Test', cells at `node_dist` path distance are
        categorized as 'Control' and rest of the nodes are categorized as
        'Other'.

        :param target: Name of target sample whose corresponding mapping
                       scores to be considered
        :param min_score: Minimum mapping score
        :param node_dist: Path distance
        :param from_clusters: List of cluster number. 'Test' cells will only be
                              limited to these clusters.
        :param full_trail: If True then returns only nodes at `node_dist` path
                           distance else return all nodes upto `node_dist` (
                           default: False)
        :param trail_start: If full_trail is True, then the trail starts at
                            this path distance (default: 0).
        :return: None
        """
        valid_nodes = list(self.refNodes)
        if from_clusters is not None:
            if set(self.clusters.values()) == 'NA':
                raise ValueError('ERROR: Calculate clusters first using '
                                 '"make_clusters" or import clusters using '
                                 '"import_clusters"')
            else:
                if type(from_clusters) != list:
                    raise TypeError("ERROR: from_cluster parameter value "
                                    "should be a list")
                from_clusters = {str(x): None for x in from_clusters}
                valid_nodes = [x for x in valid_nodes if
                               self.clusters[x] in from_clusters]
        valid_scores = self.get_mapping_score(target, min_score=min_score,
                                              all_nodes=False)
        test_nodes = {x: None for x in valid_nodes if x in valid_scores}
        if len(test_nodes) < 5:
            print('WARNING: Less than 5 test nodes found! Will not '
                  'set "de_group"')
            return None
        control_nodes = {x: None for x in self.get_k_path_neighbours(
            list(test_nodes.keys()), node_dist,
            full_trail=full_trail, trail_start=trail_start)}
        for node in self.refNodes:
            if node in test_nodes:
                self.nodes[node]['de_group'] = 'Test'
            elif node in control_nodes:
                self.nodes[node]['de_group'] = 'Control'
            else:
                self.nodes[node]['de_group'] = 'Other'

        self.deTestCells = [x.rsplit('_', 1)[0] for x in test_nodes]
        self.deCtrlCells = [x.rsplit('_', 1)[0] for x in control_nodes]
        print("Test nodes: %d, Control nodes: %d" % (
            len(self.deTestCells), len(self.deCtrlCells)), flush=True)
        return None
