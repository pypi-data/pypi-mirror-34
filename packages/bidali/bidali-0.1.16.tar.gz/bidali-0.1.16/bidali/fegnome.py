# -*- coding: utf-8 -*-
"""fegnome:Fisher exact genome module

Functions and classes for FE testing in relation to genomic context
"""
#TODO https://www.math.hmc.edu/funfacts/ffiles/10006.3.shtml -> proportional volume
#TODO http://pythonhosted.org/gseapy/gseapy_example.html#prerank-example

import pandas as pd
import numpy as np
from collections import namedtuple, OrderedDict
import matplotlib.pyplot as plt
import matplotlib.patches as ptch
from scipy.stats import fisher_exact

def genesetOverlap(geneset_a,geneset_b,universe,alternative='greater'):
    """Calculate Fisher exact value for overlap of two genesets

    Args:
        geneset_a (set): Geneset A.
        geneset_b (set): Geneset B.
        universe (int): The size of the universe from which the genesets are taken.

    Returns:
        (oddsratio, p_value) result from scipy.stats.fisher_exact

    Todos:
        * output venn/contingency table, jaccard index
        * write test with random model als negative control
    """
    # transform genesets to sets if not provided as such
    if not isinstance(geneset_a,set): geneset_a = set(geneset_a)
    if not isinstance(geneset_b,set): geneset_b = set(geneset_b)
    # prepare contingency table
    universe_over = universe - len(geneset_a | geneset_b)
    geneseta_unique = len(geneset_a - geneset_b)
    genesetb_unique = len(geneset_b - geneset_a)
    common_genes = len(geneset_a & geneset_b)
    # calculate fe score
    return fisher_exact(
        [
            [ universe_over, geneseta_unique ],
            [ genesetb_unique, common_genes ]
        ],
        alternative = alternative
    )

def enrichometer(ranks,genesUp,genesDown=None,universe=None,fexact_H1='two-sided',
                 reservoirR1=1.4,reservoirR2=None,fillingLinewidths=False,ax=None,title=None,
                 feminpv=.05,invertx=False,textrotation=0,fontsize=12,**kwargs):
    """Enrichometer plot

    Args:
        ranks (pd.Series): Series with ranked statistic.
        genesUp (set): Up or differentially regulated genes.
        genesDown (set): If not provided, considered as unitary geneset.
        universe (int or list): Total number of genes in the universe
            or list with all genes in the universe .
        fexact_H1 (str): greater, less, or two-sided
        reservoirR1 (float): Radius1 of reservoir
        reservoirR2 (float): Radius2 of reservoir, default 0.8
        fillingLinewidths (bool): Needs to be reimplemented, is not proportional
        ax (ax): ax for plot.
        title (str): Plot title.
        feminpv (float): Plot where enrichment is the strongest;
            provide as float, if fisher enrichment at strongest is not
            significant in respect to value provided nothing is plotted
        invertx (bool): Invert x axis.
        textrotation (float): Text rotation.
        fontsize (float): Font size.

    Returns:
        figure[, leadingEdgeGenes if feminpv]

    Note:
        *kwargs* are passed to `ax.eventplot`
    """
    #enrichometer settings
    axiscale = 10
    eventoffset = 0
    if reservoirR1 and reservoirR2:
        eventlen = np.pi*reservoirR1*reservoirR2*len(ranks)/(axiscale*len(genesUp))
    else: eventlen = 1
    reservoirR2 = reservoirR2 if reservoirR2 else .8
    reservoirR1 = (reservoirR1 if reservoirR1 else
                   axiscale*eventlen*len(genesUp)/
                   (np.pi*reservoirR2*len(ranks)))
    padding = .1
    if not ax:
        fig,ax = plt.subplots(figsize=(8,2))
    else: fig = ax.get_figure()
    ax.axis('off')
    if fillingLinewidths:
        raise NotImplemented #todo use rectangle patches, does not work with linewidths
        axPixels = ax.transData.transform([(0,1),(1,0)])-ax.transData.transform((0,0))
        linewidths = (axPixels[1,0]/fig.dpi)*axiscale/len(ranks)
    settings = {
        'colors':'r',
        }
    settings.update(kwargs)

    #Normalize the ranks
    minR,maxR = (ranks.min(),ranks.max())
    normalized = ((ranks-minR)*axiscale/(maxR-minR)-axiscale-reservoirR1)
    
    ax.eventplot(normalized[normalized.index.isin(genesUp)],
                 lineoffsets=eventoffset,linelengths=eventlen,**settings)
    ax.set_xlim((-axiscale-reservoirR1-padding,reservoirR1+padding))
    ax.set_ylim((eventoffset-max(eventlen/2,reservoirR2)-padding,eventoffset+max(eventlen/2,reservoirR2)+padding))

    #Draw thermometer
    overlap = sum(ranks.index.isin(genesUp))
    filled = 1-overlap/len(genesUp)
    emptyReservoir = reservoirR1*2-(reservoirR1*2*filled)
    ax.add_patch(ptch.Ellipse((0,eventoffset),width=2*reservoirR1,height=2*reservoirR2,facecolor='r',edgecolor='none'))   
    ax.add_patch(ptch.Rectangle((-reservoirR1,eventoffset-reservoirR2),
                                emptyReservoir,2*reservoirR2,facecolor='w',edgecolor='none'))
    ax.add_patch(ptch.Ellipse((0,eventoffset),width=2*reservoirR1,height=2*reservoirR2,facecolor='none',edgecolor='k'))
    ax.add_patch(ptch.Rectangle((-axiscale-reservoirR1,eventoffset-eventlen/2),axiscale,eventlen,facecolor='w',edgecolor='k'))

    #Annotations
    ax.annotate('{:g}'.format(minR),(-axiscale-reservoirR1,(eventoffset-eventlen/2)-padding),
                ha='right' if invertx else 'left',va='top',rotation=textrotation,size=fontsize)
    ax.annotate('{:g}'.format(maxR),(-reservoirR1,(eventoffset-eventlen/2)-padding),
                ha='left' if invertx else 'right',va='top',rotation=textrotation,size=fontsize)

    if universe:
        if type(universe) is list: raise NotImplemented
        odds,pval = fisher_exact([[overlap,len(ranks)],[len(genesUp)-overlap,universe]],alternative=fexact_H1)
        ax.annotate('{}\n{:.3g}'.format(len(genesUp),pval),(0,eventoffset),
                    ha='center',va='center',rotation=textrotation,size=fontsize)

    if feminpv:
        fenrichscores = fenrichmentscore(ranks,genesUp)
        pvmin = fenrichscores.pvalue.min()
        if pvmin <= feminpv:
            leadingEdgeGene = fenrichscores[fenrichscores.pvalue==pvmin].first_valid_index()
            #ax.eventplot((normalized.loc[leadingEdgeGene],),lineoffsets=eventoffset,linelengths=eventlen,
            #             color='g')
            ax.add_patch(ptch.Rectangle((-axiscale-reservoirR1,eventoffset-eventlen/2),
                                        normalized.loc[leadingEdgeGene]+axiscale+reservoirR1,
                                        eventlen,facecolor='r',alpha=.4))
            ax.annotate('{:.3g}'.format(pvmin),(normalized.loc[leadingEdgeGene]+padding,eventoffset),
                        ha='left',va='center',size=fontsize)
        else: leadingEdgeGene = None
        
    if title:
        #ax.set_title(title)
        ax.annotate(title,(-axiscale-reservoirR1,eventoffset+padding+eventlen/2),
                    ha='right' if invertx else 'left',va='bottom',size=fontsize+2)

    if invertx: ax.invert_xaxis()
    
    return (fig,leadingEdgeGene) if feminpv else fig

def fenrichmentscore(ranks,genesUp,genesDown=None):
    """Calculate fe score for each position in the ranked list

    Args:
        ranks (pd.Series): Ranks for all genes.
        genesUp (set): Up or differentially regulated genes.
        genesDown (set): Optionally down regulated genes.

    Returns:
        pd.DataFrame with oddratio's and pvalue's.
    """
    genes = {g for g in genesUp if g in ranks.index}
    ranks = ranks.sort_values()
    fescores = []
    for i in range(1,len(ranks)):
        genesUpto,genesAfter = set(ranks.index[:i]),set(ranks.index[i:])
        fescores.append(
            fisher_exact([[len(genesUpto&genes),len(genesUpto-genes)],
                          [len(genesAfter&genes),len(genesAfter-genes)]],
                         alternative='greater')
        )
        
    return pd.DataFrame(fescores,columns=['oddratio','pvalue'],index=ranks.index[:-1])

RankSumResult = namedtuple('RankSumResult',[
    'probability',
    'genesetsize',
    'overlapsize',
    'rankedgenes',
    'nulldistrosize',
    'fe_s','fe_p'])
        
def rankSumProbability(ranks, geneset, alternative='greater',
                       nulldistrosize=10000, nulldistrosave=True, universe=30000, verbose=False):
    """Probability of the ranksum

    Args:
        ranks (pd.Series): Ranks of the genes.
        geneset (set): Genes for the rank sum.
        alternative (str): greater or less.
        nulldistrosize (int): Size of the null distribution to calculate.
        nulldistrosave (bool): Option to cache nulldistro for a given geneset size and ranks.
        universe (int): Size of the genes universe.
        verbose (bool): Extra info.

    Returns:
        namedtuple RankSumResult

    Example:
        >>> from .tests.test_fegnome import testRanks, testGeneset
        >>> rankSumProbability(testRanks,testGeneset,nulldistrosave=False) # doctest: +ELLIPSIS
        RankSumResult(...)
    """
    realsetlen = len(geneset)
    setlen = ranks.index.isin(geneset).sum()
    if not setlen: return RankSumResult(None,realsetlen,setlen,None,None,None,None)
    ranksum = ranks[ranks.index.isin(geneset)].sum()
    if nulldistrosave:
        import pickle,hashlib
        from bidali import LSD
        hashindex = hashlib.md5(str(tuple(sorted(ranks))).encode()).hexdigest()
        try: nulldistros = pickle.load(open(LSD.processedDataStorage+'ranklogsum_nulldistros.pickle','rb'))
        except FileNotFoundError: nulldistros = {}
        if (hashindex,setlen) in nulldistros and nulldistros[(hashindex,setlen)][0] >= nulldistrosize:
            nulldistrosize,nulldistro = nulldistros[(hashindex,setlen)]
            if verbose: print('Using previously stored nulldistribution size',nulldistrosize)
        else:
            nulldistro = pd.Series([ranks.sample(n=setlen).sum() for i in range(nulldistrosize)])
            nulldistros[(hashindex,setlen)] = (nulldistrosize, nulldistro)
            pickle.dump(nulldistros,open(LSD.processedDataStorage+'ranklogsum_nulldistros.pickle','wb'))
    else:
        nulldistro = pd.Series([ranks.sample(n=setlen).sum() for i in range(nulldistrosize)])

    if alternative == 'greater':
        probability = float(sum(nulldistro < ranksum))/nulldistrosize
    elif alternative == 'less':
        probability = float(sum(nulldistro > ranksum))/nulldistrosize

    fe = fisher_exact([[setlen,len(ranks)],
                       [realsetlen-setlen,universe]],
                      alternative='greater')
        
    return RankSumResult(probability,realsetlen,setlen,len(ranks),nulldistrosize,*fe)
