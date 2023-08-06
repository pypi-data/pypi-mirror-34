from backtester.features.feature import Feature
import numpy as np


class RatioMarketFeature(Feature):

    '''
    Computing for Instrument. By default defers to computeForLookbackData
    '''
    @classmethod
    def computeForInstrument(cls, updateNum, time, featureParams, featureKey, instrumentManager):
        instrumentLookbackData = instrumentManager.getLookbackInstrumentFeatures()
        feature1 = instrumentLookbackData.getFeatureDf(featureParams['featureName1']).iloc[-1]
        feature2 = instrumentLookbackData.getFeatureDf(featureParams['featureName2']).iloc[-1]

        toRtn = feature1 / feature2
        toRtn[toRtn == np.Inf] = 0
        return toRtn

    '''
    Computing for Market. By default defers to computeForLookbackData
    '''
    @classmethod
    def computeForMarket(cls, updateNum, time, featureParams, featureKey, currentMarketFeatures, instrumentManager):
        feature = featureParams['featureName']
        instrumentId1 = featureParams['instrumentId1']
        instrument1 = instrumentManager.getInstrument(instrumentId1)
        instrumentId2 = featureParams['instrumentId2']
        instrument2 = instrumentManager.getInstrument(instrumentId2)
        if (instrument1 is None) or (instrument2 is None):
            return 0
        else:
            instrumentLookbackData = instrumentManager.getLookbackInstrumentFeatures()
            dataDf = instrumentLookbackData.getFeatureDf(feature)

            instrument1Price = dataDf[instrumentId1].iloc[-1]
            instrument2Price = dataDf[instrumentId2].iloc[-1]
            if instrument2Price == 0:
                return 0
            return instrument1Price / float(instrument2Price)

    @classmethod
    def computeForInstrumentData(cls, updateNum, featureParams, featureKey, featureManager):
        data1= featureManager.getFeatureDf(featureParams['featureName1'])
        data2= featureManager.getFeatureDf(featureParams['featureName2'])
        if (data1 is None) or (data2 is None):
            logWarn("[%d] instrument data for \"%s\" is not available, can't calculate \"%s\"" % (updateNum, featureParams['featureName'], featureKey))
            return None
        ratio = data1/data2
        ratio[ratio==np.Inf]=0
        return ratio
