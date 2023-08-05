
from matplotlib.colors import ListedColormap
from numpy import nan, inf

# Used to reconstruct the colormap in pycam02ucs.cm.viscm
parameters = {'xp': [3.1985305919363043, -1.749263468013453, -9.4691953967642633, -30.479082402413965, -29.861144549306616, -2.3629100860297854],
              'yp': [-24.699858757062117, -40.9722222222222, -29.025423728813536, -2.1451271186440408, 40.801553672316402, 19.791666666666686],
              'min_Jp': 18.8671875,
              'max_Jp': 95.0}

cm_data = [[ 0.16295295, 0.09521592, 0.42257292],
           [ 0.16481011, 0.09635116, 0.43184597],
           [ 0.16661617, 0.09744967, 0.44120648],
           [ 0.16836624, 0.09851521, 0.4506511 ],
           [ 0.17005471, 0.09955275, 0.46017511],
           [ 0.17167508, 0.10056873, 0.46977222],
           [ 0.17321987, 0.10157136, 0.47943423],
           [ 0.17468043, 0.10257097, 0.48915068],
           [ 0.17604337, 0.10356584, 0.4989416 ],
           [ 0.17729823, 0.10458025, 0.50877159],
           [ 0.1784323 , 0.10563803, 0.51861083],
           [ 0.17942267, 0.10674166, 0.52848361],
           [ 0.18025423, 0.10793563, 0.53832457],
           [ 0.18089754, 0.10923866, 0.54813521],
           [ 0.18132983, 0.11070429, 0.55784354],
           [ 0.18150693, 0.11236134, 0.56744719],
           [ 0.18139596, 0.11428044, 0.57685059],
           [ 0.18094994, 0.11652515, 0.5859821 ],
           [ 0.18011665, 0.1191683 , 0.59474942],
           [ 0.17884196, 0.12228861, 0.60303661],
           [ 0.17707513, 0.12596207, 0.61070774],
           [ 0.1747765 , 0.13024864, 0.61761743],
           [ 0.17192559, 0.13517685, 0.62362908],
           [ 0.16853023, 0.14073088, 0.62863572],
           [ 0.16463735, 0.14684332, 0.63257966],
           [ 0.16031417, 0.15340748, 0.63547019],
           [ 0.15565395, 0.16029118, 0.63737422],
           [ 0.15073736, 0.16736889, 0.63839897],
           [ 0.14564276, 0.17452933, 0.63866876],
           [ 0.14043681, 0.18168415, 0.63830895],
           [ 0.13517265, 0.18876883, 0.63743501],
           [ 0.12989066, 0.19573986, 0.63614699],
           [ 0.12462051, 0.20257034, 0.63452826],
           [ 0.1193859 , 0.20924466, 0.63264783],
           [ 0.11422949, 0.21574563, 0.63057687],
           [ 0.10914049, 0.22208312, 0.62834552],
           [ 0.10414386, 0.22825465, 0.62599796],
           [ 0.09926305, 0.23426098, 0.62357178],
           [ 0.09449513, 0.240114  , 0.62108167],
           [ 0.08986952, 0.24581472, 0.61855919],
           [ 0.08539286, 0.25137295, 0.61601663],
           [ 0.08106757, 0.25679971, 0.61345967],
           [ 0.07694419, 0.26209156, 0.61092383],
           [ 0.07300704, 0.2672655 , 0.6083965 ],
           [ 0.06927651, 0.2723273 , 0.60588732],
           [ 0.06578801, 0.27727895, 0.60341418],
           [ 0.06255595, 0.28212824, 0.60097879],
           [ 0.05959205, 0.28688317, 0.59857975],
           [ 0.05691772, 0.29154887, 0.5962215 ],
           [ 0.05455347, 0.29613025, 0.5939076 ],
           [ 0.0525189 , 0.30063184, 0.59164148],
           [ 0.05083877, 0.30505623, 0.58943153],
           [ 0.04951454, 0.30941022, 0.58727149],
           [ 0.0485549 , 0.31369777, 0.58516273],
           [ 0.04796369, 0.3179226 , 0.58310625],
           [ 0.04773946, 0.32208826, 0.58110273],
           [ 0.04787545, 0.32619809, 0.57915259],
           [ 0.04835985, 0.33025524, 0.57725602],
           [ 0.04917639, 0.3342627 , 0.57541302],
           [ 0.05030519, 0.3382233 , 0.57362343],
           [ 0.05172369, 0.34213968, 0.57188697],
           [ 0.05340768, 0.34601437, 0.57020322],
           [ 0.05533215, 0.34984975, 0.5685717 ],
           [ 0.05747218, 0.35364807, 0.56699183],
           [ 0.05980352, 0.35741146, 0.56546298],
           [ 0.06230309, 0.36114193, 0.56398445],
           [ 0.06494928, 0.36484141, 0.56255553],
           [ 0.06772215, 0.3685117 , 0.56117544],
           [ 0.07060351, 0.37215453, 0.55984338],
           [ 0.0735784 , 0.37577101, 0.55856129],
           [ 0.07663101, 0.379363  , 0.55732688],
           [ 0.0797474 , 0.38293224, 0.55613803],
           [ 0.08291581, 0.38648014, 0.55499386],
           [ 0.08612581, 0.39000807, 0.55389345],
           [ 0.08936818, 0.39351731, 0.55283591],
           [ 0.09263475, 0.39700911, 0.5518203 ],
           [ 0.09591831, 0.40048465, 0.55084572],
           [ 0.09921324, 0.4039447 , 0.54991337],
           [ 0.10251396, 0.40739026, 0.54902285],
           [ 0.10581449, 0.41082289, 0.54817039],
           [ 0.10911041, 0.41424357, 0.54735502],
           [ 0.11239785, 0.41765327, 0.5465758 ],
           [ 0.11567334, 0.42105293, 0.54583174],
           [ 0.11893417, 0.42444322, 0.54512319],
           [ 0.12217819, 0.42782467, 0.5444513 ],
           [ 0.12540189, 0.43119871, 0.54381137],
           [ 0.12860313, 0.43456614, 0.54320239],
           [ 0.13177997, 0.43792773, 0.54262334],
           [ 0.1349307 , 0.44128422, 0.54207318],
           [ 0.13805491, 0.44463569, 0.54155509],
           [ 0.14115011, 0.44798348, 0.54106381],
           [ 0.14421502, 0.45132831, 0.54059793],
           [ 0.14724858, 0.45467082, 0.54015636],
           [ 0.15024993, 0.4580116 , 0.5397383 ],
           [ 0.1532192 , 0.46135071, 0.53934608],
           [ 0.15615459, 0.46468937, 0.53897446],
           [ 0.15905548, 0.46802811, 0.53862227],
           [ 0.16192139, 0.47136748, 0.53828832],
           [ 0.16475245, 0.4747077 , 0.53797335],
           [ 0.16754826, 0.47804933, 0.5376757 ],
           [ 0.17030807, 0.48139312, 0.53739229],
           [ 0.17303172, 0.4847395 , 0.53712185],
           [ 0.17571937, 0.48808883, 0.53686368],
           [ 0.17837165, 0.49144123, 0.53661836],
           [ 0.18098782, 0.4947975 , 0.53638175],
           [ 0.18356807, 0.49815802, 0.53615252],
           [ 0.18611271, 0.50152311, 0.53592932],
           [ 0.18862304, 0.50489271, 0.53571335],
           [ 0.19109853, 0.50826757, 0.53550031],
           [ 0.19353972, 0.51164795, 0.53528878],
           [ 0.19594729, 0.51503411, 0.53507737],
           [ 0.19832271, 0.51842599, 0.53486655],
           [ 0.20066603, 0.52182411, 0.5346528 ],
           [ 0.20297814, 0.52522869, 0.53443452],
           [ 0.20526004, 0.52863989, 0.53421026],
           [ 0.20751347, 0.53205763, 0.53398   ],
           [ 0.20973895, 0.53548228, 0.53374061],
           [ 0.21193777, 0.53891395, 0.53349055],
           [ 0.21411134, 0.54235271, 0.53322838],
           [ 0.21626158, 0.54579847, 0.53295358],
           [ 0.21838953, 0.54925145, 0.53266342],
           [ 0.2204969 , 0.55271165, 0.53235648],
           [ 0.22258553, 0.55617904, 0.53203143],
           [ 0.22465737, 0.55965355, 0.53168703],
           [ 0.22671414, 0.56313522, 0.53132127],
           [ 0.22875792, 0.56662395, 0.53093283],
           [ 0.23079087, 0.57011965, 0.53052033],
           [ 0.23281507, 0.57362224, 0.53008206],
           [ 0.23483286, 0.57713158, 0.52961673],
           [ 0.23684665, 0.58064749, 0.52912308],
           [ 0.23885883, 0.58416983, 0.52859959],
           [ 0.24087168, 0.5876985 , 0.52804439],
           [ 0.24288806, 0.59123319, 0.52745678],
           [ 0.24491068, 0.59477367, 0.52683562],
           [ 0.24694203, 0.59831977, 0.52617913],
           [ 0.24898467, 0.60187131, 0.5254855 ],
           [ 0.25104184, 0.60542788, 0.52475455],
           [ 0.25311648, 0.60898917, 0.5239853 ],
           [ 0.25521116, 0.61255501, 0.52317565],
           [ 0.25732863, 0.61612516, 0.52232392],
           [ 0.25947244, 0.61969909, 0.52143048],
           [ 0.26164566, 0.62327645, 0.52049446],
           [ 0.26385093, 0.62685702, 0.51951365],
           [ 0.26609108, 0.63044055, 0.51848614],
           [ 0.26836985, 0.63402641, 0.51741302],
           [ 0.27069035, 0.63761419, 0.51629357],
           [ 0.27305542, 0.64120359, 0.51512593],
           [ 0.27546763, 0.64479445, 0.51390698],
           [ 0.2779309 , 0.64838599, 0.51263903],
           [ 0.28044833, 0.65197775, 0.51132146],
           [ 0.283023  , 0.65556926, 0.5099537 ],
           [ 0.28565699, 0.6591606 , 0.50852973],
           [ 0.28835435, 0.66275079, 0.50705376],
           [ 0.29111809, 0.66633932, 0.50552536],
           [ 0.29395118, 0.66992568, 0.50394405],
           [ 0.29685621, 0.67350965, 0.50230621],
           [ 0.29983621, 0.6770907 , 0.50061096],
           [ 0.3028944 , 0.68066801, 0.49886092],
           [ 0.30603358, 0.68424103, 0.49705572],
           [ 0.30925654, 0.6878092 , 0.495195  ],
           [ 0.31256595, 0.69137231, 0.4932732 ],
           [ 0.31596475, 0.69492953, 0.49129275],
           [ 0.31945565, 0.6984801 , 0.48925534],
           [ 0.32304124, 0.70202339, 0.48716074],
           [ 0.3267241 , 0.70555876, 0.48500876],
           [ 0.33050708, 0.70908574, 0.48279556],
           [ 0.33439297, 0.71260364, 0.48052013],
           [ 0.33838396, 0.71611153, 0.47818646],
           [ 0.34248248, 0.71960867, 0.47579452],
           [ 0.34669093, 0.72309429, 0.47334431],
           [ 0.3510117 , 0.72656762, 0.4708359 ],
           [ 0.35544775, 0.73002792, 0.46826672],
           [ 0.36000221, 0.73347437, 0.46563433],
           [ 0.36467645, 0.73690592, 0.46294413],
           [ 0.36947282, 0.74032165, 0.46019651],
           [ 0.37439369, 0.7437206 , 0.45739197],
           [ 0.37944143, 0.74710175, 0.45453114],
           [ 0.38461841, 0.75046408, 0.45161478],
           [ 0.38992704, 0.75380647, 0.44864382],
           [ 0.39536975, 0.75712778, 0.44561937],
           [ 0.40095086, 0.76042675, 0.44253806],
           [ 0.4066714 , 0.76370211, 0.43940565],
           [ 0.41253348, 0.76695254, 0.43622497],
           [ 0.41853957, 0.77017668, 0.43299833],
           [ 0.42469214, 0.77337305, 0.42972841],
           [ 0.43099366, 0.77654014, 0.42641835],
           [ 0.4374466 , 0.77967637, 0.4230718 ],
           [ 0.44405337, 0.78278006, 0.41969303],
           [ 0.45081634, 0.78584949, 0.41628696],
           [ 0.45773776, 0.78888286, 0.41285929],
           [ 0.46481977, 0.79187831, 0.40941661],
           [ 0.47206428, 0.7948339 , 0.4059665 ],
           [ 0.47947297, 0.79774769, 0.40251764],
           [ 0.4870472 , 0.80061765, 0.39907996],
           [ 0.49478789, 0.80344179, 0.39566477],
           [ 0.50269545, 0.80621808, 0.39228485],
           [ 0.51077223, 0.80894416, 0.38895135],
           [ 0.51901758, 0.81161801, 0.38568043],
           [ 0.52742705, 0.81423825, 0.38249349],
           [ 0.53599744, 0.81680329, 0.37941065],
           [ 0.5447243 , 0.8193118 , 0.37645392],
           [ 0.55360175, 0.82176277, 0.37364707],
           [ 0.56262239, 0.82415554, 0.37101546],
           [ 0.57178017, 0.8264893 , 0.36858305],
           [ 0.58106198, 0.82876481, 0.36637986],
           [ 0.59045227, 0.83098363, 0.36443634],
           [ 0.59993631, 0.83314747, 0.3627802 ],
           [ 0.60949784, 0.8352587 , 0.36143806],
           [ 0.61911788, 0.83732074, 0.3604355 ],
           [ 0.62877531, 0.83933797, 0.35979568],
           [ 0.63845159, 0.84131462, 0.35953618],
           [ 0.64812757, 0.84325556, 0.35967077],
           [ 0.65778455, 0.84516598, 0.36020866],
           [ 0.66740471, 0.84705131, 0.36115427],
           [ 0.67696176, 0.84891984, 0.36250963],
           [ 0.68644876, 0.85077489, 0.36426656],
           [ 0.69585443, 0.85262128, 0.36641547],
           [ 0.70516856, 0.85446373, 0.36894368],
           [ 0.71438303, 0.85630656, 0.37183582],
           [ 0.72349176, 0.85815365, 0.3750745 ],
           [ 0.73249065, 0.86000837, 0.37864099],
           [ 0.74137736, 0.86187357, 0.3825159 ],
           [ 0.7501512 , 0.86375161, 0.38667965],
           [ 0.75881284, 0.86564434, 0.39111303],
           [ 0.76736417, 0.8675532 , 0.39579749],
           [ 0.77580803, 0.86947917, 0.40071548],
           [ 0.78414804, 0.87142291, 0.40585059],
           [ 0.79237773, 0.87338865, 0.41118249],
           [ 0.80049763, 0.87537819, 0.41669356],
           [ 0.80852429, 0.87738718, 0.42237605],
           [ 0.81646307, 0.87941518, 0.42821863],
           [ 0.82431945, 0.88146161, 0.43421127],
           [ 0.83208604, 0.88353084, 0.44033585],
           [ 0.83975443, 0.88562785, 0.44657232],
           [ 0.8473544 , 0.88774214, 0.45293066],
           [ 0.85489132, 0.88987266, 0.45940532],
           [ 0.86234095, 0.89203075, 0.46596504],
           [ 0.86971917, 0.89421116, 0.47261258],
           [ 0.87704795, 0.89640559, 0.4793596 ],
           [ 0.88430614, 0.89862422, 0.48617718],
           [ 0.89149679, 0.90086694, 0.49305896],
           [ 0.89865066, 0.90312109, 0.50002982],
           [ 0.90573286, 0.90540326, 0.50704449],
           [ 0.91276817, 0.90770328, 0.51412293],
           [ 0.91977198, 0.91001483, 0.52127748],
           [ 0.92669995, 0.91235949, 0.52844799],
           [ 0.93360939, 0.91471118, 0.53569895],
           [ 0.94046103, 0.91708934, 0.5429753 ],
           [ 0.94728035, 0.91948254, 0.55030445],
           [ 0.95406597, 0.92189212, 0.55767999],
           [ 0.96080498, 0.92432523, 0.56507901],
           [ 0.96752874, 0.92676689, 0.57254139],
           [ 0.97419673, 0.92923821, 0.58000416],
           [ 0.9808627 , 0.93171248, 0.58754258],
           [ 0.98746841, 0.93422029, 0.59506489],
           [ 0.99408058, 0.93672758, 0.60267   ]]

test_cm = ListedColormap(cm_data, name=__file__)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    try:
        from viscm import viscm
        viscm(test_cm)
    except ImportError:
        print("viscm not found, falling back on simple display")
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',
                   cmap=test_cm)
    plt.show()
