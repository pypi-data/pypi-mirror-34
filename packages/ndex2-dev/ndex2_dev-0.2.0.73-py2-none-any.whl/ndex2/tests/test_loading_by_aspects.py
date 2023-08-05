__author__ = 'aarongary'

import unittest

import json
import ndex2
import os

import json
import pandas as pd
import csv
import networkx as nx
import ndex2
import os
import io
import requests
from ndex2.niceCXNetwork import NiceCXNetwork
from ndex2.client import DecimalEncoder
import ndex2.client as nc

upload_server = 'dev.ndexbio.org'
upload_username = 'scratch'
upload_password = 'scratch'

path_this = os.path.dirname(os.path.abspath(__file__))

class TestLoadByAspects(unittest.TestCase):
    @unittest.skip("Temporary skipping")
    def test_create_from_pandas_with_headers2(self):
        path_to_network = os.path.join(path_this, 'CTD_genes_pathways.txt')

        with open(path_to_network, 'rU') as tsvfile:
            header = [h.strip() for h in tsvfile.readline().split('\t')]

            df = pd.read_csv(tsvfile,delimiter='\t',engine='python',names=header)

            niceCx = ndex2.create_nice_cx_from_pandas(df, source_field='GeneSymbol', target_field='PathwayName',
            source_node_attr=['GeneID'], target_node_attr=['Pathway Source'], edge_attr=[], user_agent='UNIT-TESTING')

            upload_message = True #niceCx.upload_to(upload_server, upload_username, upload_password)
            self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping")
    def test_load_nodes(self):
        niceCx = ndex2.create_empty_nice_cx(user_agent='UNIT-TESTING') #NiceCXNetwork()
        gene_list = ['OR2J3', 'AANAT', 'CCDC158', 'PLAC8L1', 'CLK1', 'GLTP', 'PITPNM2','TRAPPC8', 'EIF2S2', 'ST14',
                     'NXF1', 'H3F3B','FOSB', 'MTMR4', 'USP46', 'CDH11', 'ENAH', 'CNOT7', 'STK39', 'CAPZA1', 'STIM2',
                     'DLL4', 'WEE1', 'MYO1D', 'TEAD3']
        for i in range(1,10):
            niceCx.create_node(id=i, node_name='node%s' % str(i), node_represents=gene_list[i])

        upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)
        self.assertTrue(upload_message)
        #print(niceCx.to_cx())

    @unittest.skip("Temporary skipping")
    def test_load_edges(self):
        niceCx = ndex2.create_empty_nice_cx(user_agent='UNIT-TESTING') #NiceCXNetwork()
        niceCx.create_node(id=1, node_name='node%s' % str(1), node_represents='ABC')
        niceCx.create_node(id=2, node_name='node%s' % str(2), node_represents='DEF')
        niceCx.create_edge(id=1, edge_source=1, edge_target=2, edge_interaction='neighbor')

        upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)
        self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping")
    def test_pandas_loading(self):
        path_to_network = os.path.join(path_this, 'MDA1.txt')

        with open(path_to_network, 'rU') as tsvfile:
            header = [h.strip() for h in tsvfile.readline().split('\t')]

            df = pd.read_csv(tsvfile,delimiter='\t',engine='python',names=header)

            niceCx = ndex2.create_empty_nice_cx(user_agent='UNIT-TESTING') #NiceCXNetwork()
            for index, row in df.iterrows():
                niceCx.create_node(id=row['Bait'], node_name=row['Bait'], node_represents=row['Bait'])
                niceCx.create_node(id=row['Prey'], node_name=row['Prey'], node_represents=row['Prey'])

                niceCx.create_edge(id=index, edge_source=row['Bait'], edge_target=row['Prey'], edge_interaction='interacts-with')

            niceCx.add_metadata_stub('nodes')
            niceCx.add_metadata_stub('edges')
            if niceCx.nodeAttributes:
                niceCx.add_metadata_stub('nodeAttributes')
            if niceCx.edgeAttributes:
                niceCx.add_metadata_stub('edgeAttributes')
            upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)

            #print(df)

        my_df = pd.DataFrame(data=[(4,14),(5,15),(6,16),(7,17)], index=range(0,4), columns=['A','B'])
        self.assertIsNotNone(my_df)
        #print(pd.DataFrame(my_df))

    @unittest.skip("Temporary skipping")
    def test_create_from_pandas_no_headers(self):
        path_to_network = os.path.join(path_this, 'SIMPLE.txt')

        with open(path_to_network, 'rU') as tsvfile:
            df = pd.read_csv(tsvfile,delimiter='\t',engine='python',header=None)

            niceCx = ndex2.create_nice_cx_from_pandas(df, user_agent='UNIT-TESTING') #NiceCXNetwork(pandas_df=df)
            upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)
            self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping")
    def test_create_from_pandas_with_headers(self):
        path_to_network = os.path.join(path_this, 'MDA1.txt')

        with open(path_to_network, 'rU') as tsvfile:
            header = [h.strip() for h in tsvfile.readline().split('\t')]

            df = pd.read_csv(tsvfile,delimiter='\t',engine='python',names=header)

            niceCx = ndex2.create_nice_cx_from_pandas(df, source_field='Bait', target_field='Prey',
            source_node_attr=['AvePSM'], target_node_attr=['WD'], edge_attr=['Z', 'Entropy'], user_agent='UNIT-TESTING') #NiceCXNetwork()
            #niceCx.create_from_pandas(df, source_field='Bait', target_field='Prey', source_node_attr=['AvePSM'], target_node_attr=['WD'], edge_attr=['Z', 'Entropy'])
            my_cx_json = niceCx.to_cx()
            #print(json.dumps(my_cx_json, cls=DecimalEncoder))
            upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)
            self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping") # PASS
    def test_create_from_server(self):
        print('public network')
        niceCx = ndex2.create_nice_cx_from_server(server='public.ndexbio.org', uuid='72ef5c3a-caff-11e7-ad58-0ac135e8bacf',
        user_agent='UNIT-TESTING') #NiceCXNetwork(server='dev2.ndexbio.org', username='scratch', password='scratch', uuid='9433a84d-6196-11e5-8ac5-06603eb7f303')
        #niceCx = ndex2.create_nice_cx_from_server(server='public.ndexbio.org', username='scratch', password='scratch', uuid='75bf1e85-1bc7-11e6-a298-06603eb7f303') #NiceCXNetwork(server='dev2.ndexbio.org', username='scratch', password='scratch', uuid='9433a84d-6196-11e5-8ac5-06603eb7f303')

        niceCx.to_networkx()

        upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)
        self.assertTrue(upload_message)

    #@unittest.skip("Temporary skipping") # PASS
    def test_create_from_pandas_no_headers_3_columns(self):
        path_to_network = os.path.join(path_this, 'SIMPLE3.txt')

        with open(path_to_network, 'rU') as tsvfile:
            df = pd.read_csv(tsvfile,delimiter='\t',engine='python',header=None)

            #====================================
            # BUILD NICECX FROM PANDAS DATAFRAME
            #====================================
            niceCx = ndex2.create_nice_cx_from_pandas(df, user_agent='UNIT-TESTING') #NiceCXNetwork(pandas_df=df)
            #niceCx.apply_template('public.ndexbio.org', '72ef5c3a-caff-11e7-ad58-0ac135e8bacf')
            niceCx.apply_template('dev.ndexbio.org', '792698a8-8ba4-11e8-8b82-525400c25d22', username='scratch', password='scratch')
            upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)
            self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping") #PASS
    def test_create_from_networkx(self):
        path_to_network = os.path.join(path_this, 'SIMPLE3.txt')

        with open(path_to_network, 'rU') as tsvfile:
            reader = csv.DictReader(filter(lambda row: row[0] != '#', tsvfile), dialect='excel-tab', fieldnames=['s','t','e'])

            #===========================
            # BUILD NETWORKX GRAPH
            #===========================
            G = nx.Graph(name='loaded from Simple3.txt')
            G.graph['some property 1'] = 'some value 1'
            for row in reader:
                G.add_node(row.get('s'), test1='test1_s', test2='test2_s')
                G.add_node(row.get('t'), test1='test1_t', test2='test2_t')
                G.add_edge(row.get('s'), row.get('t'), {'interaction': 'controls-production-of', 'test3': 'test3'})

            #====================================
            # BUILD NICECX FROM NETWORKX GRAPH
            #====================================
            niceCx = ndex2.create_nice_cx_from_networkx(G, user_agent='UNIT-TESTING') #NiceCXNetwork(networkx_G=G)
            niceCx.apply_template('public.ndexbio.org', '72ef5c3a-caff-11e7-ad58-0ac135e8bacf')
            upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)
            self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping")
    def test_create_from_cx_file(self):
        path_to_network = os.path.join(path_this, 'MEDIUM_NETWORK.cx')

        with open(path_to_network, 'rU') as ras_cx:
            #====================================
            # BUILD NICECX FROM PANDAS DATAFRAME
            #====================================
            niceCx = ndex2.create_nice_cx_from_cx(cx=json.load(ras_cx), user_agent='UNIT-TESTING') #NiceCXNetwork(cx=json.load(ras_cx))
            my_cx = niceCx.to_cx()
            #print(my_cx)
            upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)
            self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping")
    def test_create_from_server_1(self):
        #====================================
        # BUILD NICECX FROM SERVER
        #====================================
        niceCx = ndex2.create_nice_cx_from_server(server='dev.ndexbio.org', username='scratch', password='scratch',
        uuid='b7190ca4-aec2-11e7-9b0a-06832d634f41', user_agent='UNIT-TESTING') #NiceCXNetwork(server='dev.ndexbio.org', username='scratch', password='scratch', uuid='b7190ca4-aec2-11e7-9b0a-06832d634f41')
        upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)
        self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping") # PASS
    def test_export_to_cx_file(self):
        path_to_network = os.path.join(path_this, 'MEDIUM_NETWORK.cx')

        with open(path_to_network, 'rU') as ras_cx:
            #====================================
            # BUILD NICECX FROM PANDAS DATAFRAME
            #====================================
            niceCx = ndex2.create_nice_cx_from_cx(cx=json.load(ras_cx), user_agent='UNIT-TESTING') #NiceCXNetwork(cx=json.load(ras_cx))
            nice_networkx = niceCx.to_networkx()
            #my_cx = niceCx.to_cx()
            #print(nice_networkx)
            upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)
            self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping") # PASS
    def test_cx_file_with_position(self):
        path_to_network = os.path.join(path_this, 'network_with_position.cx')

        with open(path_to_network, 'rU') as ras_cx:
            #====================================
            # BUILD NICECX FROM PANDAS DATAFRAME
            #====================================
            niceCx = ndex2.create_nice_cx_from_cx(cx=json.load(ras_cx), user_agent='UNIT-TESTING') #NiceCXNetwork(cx=json.load(ras_cx))

            nice_networkx = niceCx.to_networkx(graphml_compatible=True)

            niceCx_from_netx = ndex2.create_nice_cx_from_networkx(nice_networkx, graphml_compatible=True)

            upload_message = niceCx_from_netx.upload_to(upload_server, upload_username, upload_password)
            self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping") # PASS
    def test_cx_file_with_visualProperties(self):
        path_to_network = os.path.join(path_this, 'network_with_position.cx')

        with open(path_to_network, 'rU') as ras_cx:
            #====================================
            # BUILD NICECX FROM PANDAS DATAFRAME
            #====================================
            niceCx = ndex2.create_nice_cx_from_cx(cx=json.load(ras_cx), user_agent='UNIT-TESTING') #NiceCXNetwork(cx=json.load(ras_cx))

            #upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)

            niceCx2 = ndex2.create_nice_cx_from_server(server=upload_server, username=upload_username,
                                  password=upload_password, uuid='ae118ade-8ae1-11e8-8b82-525400c25d22')

            upload_message = niceCx2.upload_to(upload_server, upload_username, upload_password)

            self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping")
    def test_manual_build(self):
        niceCx = ndex2.create_empty_nice_cx(user_agent='UNIT-TESTING') #NiceCXNetwork()

        fox_node_id = niceCx.create_node(node_name='Fox')
        mouse_node_id = niceCx.create_node(node_name='Mouse')
        bird_node_id = niceCx.create_node(node_name='Bird')

        fox_bird_edge = niceCx.create_edge(edge_source=fox_node_id, edge_target=bird_node_id, edge_interaction='interacts-with')
        fox_mouse_edge = niceCx.create_edge(edge_source=fox_node_id, edge_target=mouse_node_id, edge_interaction='interacts-with')

        niceCx.add_node_attribute(property_of=fox_node_id, name='Color', values='Red')
        niceCx.add_node_attribute(property_of=mouse_node_id, name='Color', values='Gray')
        niceCx.add_node_attribute(property_of=bird_node_id, name='Color', values='Blue')

        #print(niceCx)

    @unittest.skip("Temporary skipping")
    def test_create_from_small_cx(self):
        my_cx = [
            {"numberVerification":[{"longNumber":281474976710655}]},
            {"metaData":[{"consistencyGroup":1,"elementCount":2,"idCounter":2,"name":"nodes","version":"1.0"},
            {"consistencyGroup":1,"elementCount":1,"idCounter":1,"name":"edges","version":"1.0"}]},
            {"nodes":[{"@id": 1, "n": "node1", "r": "ABC"}, {"@id": 2, "n": "node2", "r": "DEF"}]},
            {"edges":[{"@id": 1, "s": 1, "t": 2, "i": "neighbor"}]},
            {"status":[{"error":"","success":True}]}
        ]

        #niceCx = NiceCXNetwork(cx=my_cx)

        #data = [('Source', 'Target', 'interaction', 'EdgeProp'), ('ABC', 'DEF', 'interacts-with', 'Edge property 1'), ('DEF', 'XYZ', 'neighbor-of', 'Edge property 2')]
        #df = pd.DataFrame.from_records(data)
        #niceCx = NiceCXNetwork(pandas_df=df)

        df = pd.DataFrame.from_items([('Source', ['ABC', 'DEF']),
                                        ('Target', ['DEF', 'XYZ']),
                                        ('Interaction', ['interacts-with', 'neighbor-of']),
                                        ('EdgeProp', ['Edge property 1', 'Edge property 2'])])

        niceCx = ndex2.create_empty_nice_cx(user_agent='UNIT-TESTING') #NiceCXNetwork()
        niceCx.create_from_pandas(df, source_field='Source', target_field='Target', edge_attr=['EdgeProp'], edge_interaction='Interaction')

        niceCx = '' #NiceCXNetwork(server='public.ndexbio.org', uuid='f1dd6cc3-0007-11e6-b550-06603eb7f303')

        #upload_message = niceCx.upload_to(upload_server, upload_username, upload_password)
        #print(niceCx)

    @unittest.skip("Temporary skipping") # PASS
    def test_create_from_server_manipulate_and_save(self):
        print('public network')
        niceCx = ndex2.create_nice_cx_from_server(server='public.ndexbio.org', uuid='72ef5c3a-caff-11e7-ad58-0ac135e8bacf',
        user_agent='UNIT-TESTING')

        nice_networkx = niceCx.to_networkx()

        niceCx_from_netx = ndex2.create_nice_cx_from_networkx(nice_networkx)

        # Restore template
        niceCx_from_netx.apply_template('public.ndexbio.org', '72ef5c3a-caff-11e7-ad58-0ac135e8bacf')
        niceCx_from_netx.set_name('Round trip from server to networkx to NDEx')

        upload_message = niceCx_from_netx.upload_to(upload_server, upload_username, upload_password)
        self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping") # PASS
    def test_create_from_server_manipulate_and_save2(self):
        print('public network')
        niceCx = ndex2.create_nice_cx_from_server(server='public.ndexbio.org', uuid='21106ea7-cbba-11e7-ad58-0ac135e8bacf',
        user_agent='UNIT-TESTING')

        #serialized = pickle.dumps(niceCx.to_cx(), protocol=0)
        #print('Serialized memory:', sys.getsizeof(serialized))

        nice_networkx = niceCx.to_networkx()

        niceCx_from_netx   = ndex2.create_nice_cx_from_networkx(nice_networkx)

        # Restore template
        niceCx_from_netx.apply_template('public.ndexbio.org', '72ef5c3a-caff-11e7-ad58-0ac135e8bacf')
        niceCx_from_netx.set_name('Round trip from server to networkx to NDEx')

        upload_message = niceCx_from_netx.upload_to(upload_server, upload_username, upload_password)
        self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping") # PASS
    def test_create_from_tsv_manipulate_and_save(self):
        path_to_network = os.path.join(path_this, 'mgdb_mutations.txt')

        with open(path_to_network, 'rU') as tsvfile:
            header = [h.strip() for h in tsvfile.readline().split('\t')]

            df = pd.read_csv(tsvfile,delimiter='\t',engine='python',names=header)

            niceCx = ndex2.create_nice_cx_from_pandas(df, source_field='CDS Mutation', target_field='Gene Symbol',
            source_node_attr=['Primary Tissue', 'Histology', 'Genomic Locus'], target_node_attr=['Gene ID'],
            edge_interaction='variant-gene-relationship', user_agent='UNIT-TESTING') #NiceCXNetwork()

            nice_networkx = niceCx.to_networkx()
            nice_pandas = niceCx.to_pandas_dataframe()
            my_csv = nice_pandas.to_csv(sep='\t')

            with open("pandas_to_cx_to_tsv_results.txt", "w") as text_file:
                text_file.write(my_csv)

            niceCx_from_netx = ndex2.create_nice_cx_from_networkx(nice_networkx)

            # Restore template
            niceCx_from_netx.apply_template('public.ndexbio.org', '72ef5c3a-caff-11e7-ad58-0ac135e8bacf')
            niceCx_from_netx.set_name('Round trip from server to networkx to NDEx')

            upload_message = niceCx_from_netx.upload_to(upload_server, upload_username, upload_password)
            self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping") # PASS
    def test_visibility_and_showcase(self):
        path_to_network = os.path.join(path_this, 'network.cx')
        with open(path_to_network, 'rU') as tsvfile:
            cx_json = json.loads(tsvfile.read())

        niceCx = ndex2.create_nice_cx_from_cx(cx_json)

        nice_pandas = niceCx.to_pandas_dataframe()
        my_csv = nice_pandas.to_csv(sep='\t')

        with open("network_to_table.txt", "w") as text_file:
            text_file.write(my_csv)




        #my_ndex = nc.Ndex2('http://dev.ndexbio.org', 'scratch', 'scratch')
        #my_ndex._make_network_public_indexed('e12acb46-11de-11e8-a596-06832d634f41')

    @unittest.skip("Temporary skipping") # PASS
    def test_netx_plotx2(self):
        #url = "http://signor.uniroma2.it/getPathwayData.php?pathway=SIGNOR-PC"
        #print(url)
        #response = requests.get(url)
        #pathway_info = response.text
        #my_pathway_info = pathway_info.split('\t')
        #dataframe = pd.read_csv(io.StringIO(pathway_info), sep='\t', encoding='utf-8')
        #print(pd.isnull(dataframe.iat[0, 1]))
        #field0 = dataframe.iat[0, 0]
        #field1 = dataframe.iat[0, 1]
        #field2 = dataframe.iat[0, 2]
        #field3 = dataframe.iat[0, 3]
        #print(dataframe)

        signor_mapping_set = {}
        signor_list_url = 'https://signor.uniroma2.it/getPathwayData.php?list'
        cols = ['pathway_id', 'pathway_name']
        signor_mapping_list_df = pd.read_csv(signor_list_url, sep="\t", names=cols)
        signor_dict = signor_mapping_list_df.to_dict()
        pathway_name = signor_dict.get('pathway_name')
        pathway_id = signor_dict.get('pathway_id')
        id_to_name = {}
        for k, v in pathway_name.items():
            id_to_name[pathway_id.get(k)] = v
            signor_mapping_set[v] = k

        my_account = "scratch"
        my_password = "scratch"
        try:


            my_ndex = nc.Ndex2("http://dev.ndexbio.org", my_account, my_password)
            networks = my_ndex.get_network_summaries_for_user('scratch')
            update_mapping = {}
            for nk in networks:
                if signor_mapping_set.get(nk.get('name')) is not None:
                    update_mapping[nk.get('name')] = nk.get('externalId')

            print('my_ndex client: %s ' % (networks))
        except Exception as inst:
            print("Could not access account %s with password %s" % (my_account, my_password))
            print(inst.args)

    @unittest.skip("Temporary skipping") # PASS
    def test_netx_plot(self):
        my_ndex=ndex2.client.Ndex2('http://test.ndexbio.org', 'scratch', 'scratch')
        my_ndex.update_status()

        test1 = my_ndex.get_network_ids_for_user('scratch')

        nx_my_graph = nx.read_edgelist("edge_list_network_adrian.txt", nodetype=str)

        G = nx.Graph()
        G.add_node('ABC')
        G.add_node('DEF')
        G.add_node('GHI')
        G.add_node('JKL')
        G.add_node('MNO')
        G.add_node('PQR')
        G.add_node('XYZ')
        G.add_edges_from([('ABC','DEF'), ('DEF', 'GHI'),('GHI', 'JKL'),
                          ('DEF', 'JKL'), ('JKL', 'MNO'), ('DEF', 'MNO'),
                         ('MNO', 'XYZ'), ('DEF', 'PQR')])

        niceCx_full = ndex2.create_nice_cx_from_networkx(G)
        niceCx_full_networkx = niceCx_full.to_networkx()

        names = nx.get_node_attributes(niceCx_full_networkx, 'name')
        for n in niceCx_full_networkx.nodes():
            print(n)
        print(niceCx_full_networkx.nodes)
        print(names)


    @unittest.skip("Temporary skipping") # PASS
    def test_cartesian_pos(self):
        my_server = 'dev.ndexbio.org'
        my_account = 'scratch'
        my_password = 'scratch'
        G = nx.Graph()
        G.add_node('ABC')
        G.add_node('DEF')
        G.add_node('GHI')
        G.add_node('JKL')
        G.add_node('MNO')
        G.add_node('PQR')
        G.add_node('XYZ')
        G.add_edges_from([('ABC','DEF'), ('DEF', 'GHI'),('GHI', 'JKL'),
                    ('DEF', 'JKL'), ('JKL', 'MNO'), ('DEF', 'MNO'),
                    ('MNO', 'XYZ'), ('DEF', 'PQR')])

        pos = nx.circular_layout(G)  # Note the circular layout
        G.pos = pos
        #for u, d in G.nodes(data=True):
        #   temp = list(pos[u])
        #   d['pos'] = temp  # give nodes the property 'pos'


        niceCx_full = ndex2.create_nice_cx_from_networkx(G)
        niceCx_full.set_name('This is a test graph')
        niceCx_full.upload_to(my_server, my_account, my_password)

    @unittest.skip("Temporary skipping")
    def test_pandas_loading(self):
        niceCx = ndex2.create_empty_nice_cx(user_agent='UNIT-TESTING') #NiceCXNetwork()
        niceCx.create_node(id=0, node_name='ABC', node_represents='ABC_HUMAN')
        niceCx.create_node(id=1, node_name='XYZ', node_represents='XYZ_HUMAN')

        niceCx.create_edge(id=0, edge_source=0, edge_target=1, edge_interaction='interacts-with1')
        niceCx.create_edge(id=1, edge_source=0, edge_target=1, edge_interaction='interacts-with2')
        niceCx.create_edge(id=2, edge_source=0, edge_target=1, edge_interaction='interacts-with3')
        niceCx.create_edge(id=3, edge_source=0, edge_target=1, edge_interaction='interacts-with4')
        niceCx.create_edge(id=4, edge_source=0, edge_target=1, edge_interaction='interacts-with5')
        niceCx.create_edge(id=5, edge_source=0, edge_target=1, edge_interaction='interacts-with6')

        niceCx.add_metadata_stub('nodes')
        niceCx.add_metadata_stub('edges')

        netx = niceCx.to_networkx()
        print(netx)




def get_sognor_update_mapping(username, password):
    signor_mapping_set = {}
    signor_list_url = 'https://signor.uniroma2.it/getPathwayData.php?list'
    cols = ['pathway_id', 'pathway_name']

    signor_mapping_list_df = pd.read_csv(signor_list_url, sep="\t", names=cols)
    signor_dict = signor_mapping_list_df.to_dict()

    pathway_names = signor_dict.get('pathway_name')
    for k, v in pathway_names.items():
        signor_mapping_set[v] = k

    my_ndex = nc.Ndex2("http://dev.ndexbio.org", username, password)
    networks = my_ndex.get_network_summaries_for_user('scratch')
    update_mapping = {}
    for nk in networks:
        if signor_mapping_set.get(nk.get('name')) is not None:
            update_mapping[nk.get('name')] = nk.get('externalId')

    return update_mapping
