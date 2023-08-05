# -*- coding: utf-8 -*-
"""Publication crawler and text mining module


Functions for creating dictionaries and starting up text mining explorations.
"""
import pandas as pd, numpy as np

# Utilities for making dictionaries
##CIDcounter class to create CID (concept id) according to Adil's requirement that it
##is the same as TID reference symbol
class CIDcounter:
    def __init__(self,startvalue=0):
        import itertools as it
        self.counter = it.count(startvalue)
        
    def next(self,increment):
        if increment:
            self.value = next(self.counter)
        else: next(self.counter) #this step ensures a CID == TID for a new reference concept
        return self.value

def makeCIDandTID(df,conceptCol='symbol',aliasCol='alias'):
    """Make text mining dictionary with TID and CID set

    According to Adil Salhi's text mining requirements.

    Args:
        df (pd.DataFrame): Dataframe to transform.
        conceptCol (str): Column name of main concept/symbol.
        aliasCol (str): Column name where all aliases for the concept
          are gathered in a list, including the concept itself as first list member.
    """
    from bidali.util import unfoldDFlistColumn
    df = unfoldDFlistColumn(df,aliasCol)
    df.reset_index(inplace=True,drop=True)
    df.index.name = 'TID' #term id
    c = CIDcounter()        
    df.insert(0, 'CID', (~df[conceptCol].duplicated()).apply(c.next)) #need to work with `not` duplicated column!
    return df

## get icd9 info
def get_icd9info(icd9code,type='disease',includeShortName=True):
    """Get info related to icd9code

    Info:
        https://clinicaltables.nlm.nih.gov/

    Reference:
        https://clinicaltables.nlm.nih.gov/apidoc/icd9cm_dx/v3/doc.html

    Args:
        icd9code (str): Code to query.
        type (option): `disease` or `procedure`.
        includeShortName: Also include the short name in output.
    """
    import requests, json
    if type == 'disease':
        url = 'https://clinicaltables.nlm.nih.gov/api/icd9cm_dx/v3/search?terms={term}'
    elif type == 'procedure':
        url = 'https://clinicaltables.nlm.nih.gov/api/icd9cm_sg/v3/search?terms={term}'
    else: raise Exception('Wrong type specified, should be disease or procedure, not',type)
    if includeShortName: url+='&ef=short_name'
    r = requests.get(url.format(term = icd9code))
    return json.loads(r.content)
    
# Dictionary functions
def get_biomart_gene_dictionary():
    from bidali.LSD.dealer.ensembl import get_biomart
    from bidali.genenames import fetchAliases
    bm = get_biomart(atts=[
        'ensembl_gene_id',
        'ensembl_peptide_id',
        'pdb',
        'entrezgene',
        'hgnc_symbol',
    ])
    HGNC_aliases = bm['HGNC symbol'].apply(lambda x: [(a,x) for a in fetchAliases(x,unknown_action='list')])
    HGNC_aliases = pd.concat([pd.Series(dict(a)) for a in HGNC_aliases])
    HGNC_aliases = pd.Series(HGNC_aliases.index.values, index=HGNC_aliases)
    HGNC_aliases.index.set_names('HGNC symbol', inplace = True)
    HGNC_aliases.name = 'HGNC alias'
    return bm.join(other = HGNC_aliases, on = 'HGNC symbol')

def get_gene_dictionary():
    """Gene symbol dictionary.
    Uses genenames.org data.
    """
    from bidali.LSD.dealer import genenames
    from bidali.util import unfoldDFlistColumn
    gn = genenames.get_genenames()
    gn['alias'] = gn.T.apply(
        lambda x: [x.symbol, x['name']] + #optionally add other names such as protein names here
        (
            x.alias_symbol.split('|') if x.alias_symbol is not np.nan else []
        )
    )
    print('Original columns',gn.columns)
    gn = gn[['hgnc_id','symbol','alias','uniprot_ids']].copy()
    print('Columns kept:',gn.columns)
    gn = makeCIDandTID(gn)
    return gn

def get_gene_family_dictionary(family_ids):
    """Gene family gene symbol dictionary.
    Uses genenames.org data.
    
    Args:
        family_ids (int or list of ints): Either a single family id, or a list of family ids.

    Example:
        >>> gfd = get_gene_family_dictionary(588) # HLA family
    """
    from bidali.LSD.dealer import genenames
    from bidali.util import unfoldDFlistColumn
    gf = genenames.get_genefamilies()

    # rename some columns
    gf.rename(
        {
            'Approved Symbol': 'symbol',
            'Approved Name': 'name',
            'HGNC ID': 'hgnc_id',
            'Previous Symbols': 'previous'
        }, axis=1, inplace=True
    )
    
    # filter families
    if isinstance(family_ids, int): family_ids = [family_ids]
    gf = gf[gf['Gene family ID'].isin(family_ids)].copy()

    # make alias
    gf['alias'] = gf.T.apply(
        lambda x: [x.symbol, x['name'],]
        +
        (
            x.previous.split(', ') if x.previous is not np.nan else []
        )
        +
        (
            x.Synonyms.split(', ') if x.Synonyms is not np.nan else []
        )
    )
    print('Original columns', gf.columns)
    gf = gf[['hgnc_id','symbol','alias']].copy()
    print('Columns kept:',gf.columns)
    gf = makeCIDandTID(gf)
    return gf
