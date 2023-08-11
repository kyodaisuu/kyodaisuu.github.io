#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

LANG = 'en'

# 唐の実叉難陀訳 
SIKSA = "一百洛叉為一俱胝，俱胝俱胝為一阿庾多，阿庾多阿庾多為一那由他，那由他那由他為一頻婆羅，頻婆羅頻婆羅為一矜羯羅，矜羯羅矜羯羅為一阿伽羅，阿伽羅阿伽羅為一最勝，最勝最勝為一摩婆(上聲呼)羅，摩婆羅摩婆羅為一阿婆羅，阿婆羅阿婆羅為一多婆羅，多婆羅多婆羅為一界分，界分界分為一普摩，普摩普摩為一禰摩，禰摩禰摩為一阿婆鈐，阿婆鈐阿婆鈐為一彌伽婆，彌伽婆彌伽婆為一毘攞伽，毘攞伽毘攞伽為一毘伽婆，毘伽婆毘伽婆為一僧羯邏摩，僧羯邏摩僧羯邏摩為一毘薩羅，毘薩羅毘薩羅為一毘贍婆，毘贍婆毘贍婆為一毘盛伽，毘盛伽毘盛伽為一毘素陀，毘素陀毘素陀為一毘婆訶，毘婆訶毘婆訶為一毘薄底，毘薄底毘薄底為一毘佉擔，毘佉擔毘佉擔為一稱量，稱量稱量為一一持，一持一持為一異路，異路異路為一顛倒，顛倒顛倒為一三末耶，三末耶三末耶為一毘覩羅，毘覩羅毘覩羅為一奚婆羅，奚婆羅奚婆羅為一伺察，伺察伺察為一周廣，周廣周廣為一高出，高出高出為一最妙，最妙最妙為一泥羅婆，泥羅婆泥羅婆為一訶理婆，訶理婆訶理婆為一一動，一動一動為一訶理蒲，訶理蒲訶理蒲為一訶理三，訶理三訶理三為一奚魯伽，奚魯伽奚魯伽為一達攞步陀，達攞步陀達攞步陀為一訶魯那，訶魯那訶魯那為一摩魯陀，摩魯陀摩魯陀為一懺慕陀，懺慕陀懺慕陀為一瑿攞陀，瑿攞陀瑿攞陀為一摩魯摩，摩魯摩摩魯摩為一調伏，調伏調伏為一離憍慢，離憍慢離憍慢為一不動，不動不動為一極量，極量極量為一阿麼怛羅，阿麼怛羅阿麼怛羅為一勃麼怛羅，勃麼怛羅勃麼怛羅為一伽麼怛羅，伽麼怛羅伽麼怛羅為一那麼怛羅，那麼怛羅那麼怛羅為一奚麼怛羅，奚麼怛羅奚麼怛羅為一鞞麼怛羅，鞞麼怛羅鞞麼怛羅為一鉢羅麼怛羅，鉢羅麼怛羅鉢羅麼怛羅為一尸婆麼怛羅，尸婆麼怛羅尸婆麼怛羅為一翳羅，翳羅翳羅為一薜羅，薜羅薜羅為一諦羅，諦羅諦羅為一偈羅，偈羅偈羅為一窣步羅，窣步羅窣步羅為一泥羅，泥羅泥羅為一計羅，計羅計羅為一細羅，細羅細羅為一睥羅，睥羅睥羅為一謎羅，謎羅謎羅為一娑攞荼，娑攞荼娑攞荼為一謎魯陀，謎魯陀謎魯陀為一契魯陀，契魯陀契魯陀為一摩覩羅，摩覩羅摩覩羅為一娑母羅，娑母羅娑母羅為一阿野娑，阿野娑阿野娑為一迦麼羅，迦麼羅迦麼羅為一摩伽婆，摩伽婆摩伽婆為一阿怛羅，阿怛羅阿怛羅為一醯魯耶，醯魯耶醯魯耶為一薜魯婆，薜魯婆薜魯婆為一羯羅波，羯羅波羯羅波為一訶婆婆，訶婆婆訶婆婆為一毘婆羅，毘婆羅毘婆羅為一那婆羅，那婆羅那婆羅為一摩攞羅，摩攞羅摩攞羅為一娑婆羅，娑婆羅娑婆羅為一迷攞普，迷攞普迷攞普為一者麼羅，者麼羅者麼羅為一馱麼羅，馱麼羅馱麼羅為一鉢攞麼陀，鉢攞麼陀鉢攞麼陀為一毘伽摩，毘伽摩毘伽摩為一烏波跋多，烏波跋多烏波跋多為一演說，演說演說為一無盡，無盡無盡為一出生，出生出生為一無我，無我無我為一阿畔多，阿畔多阿畔多為一青蓮華，青蓮華青蓮華為一鉢頭摩，鉢頭摩鉢頭摩為一僧祇，僧祇僧祇為一趣，趣趣為一至，至至為一阿僧祇，阿僧祇阿僧祇為一阿僧祇轉，阿僧祇轉阿僧祇轉為一無量，無量無量為一無量轉，無量轉無量轉為一無邊，無邊無邊為一無邊轉，無邊轉無邊轉為一無等，無等無等為一無等轉，無等轉無等轉為一不可數，不可數不可數為一不可數轉，不可數轉不可數轉為一不可稱，不可稱不可稱為一不可稱轉，不可稱轉不可稱轉為一不可思，不可思不可思為一不可思轉，不可思轉不可思轉為一不可量，不可量不可量為一不可量轉，不可量轉不可量轉為一不可說，不可說不可說為一不可說轉，不可說轉不可說轉為一不可說不可說，此又不可說不可說為一不可說不可說轉"

# 唐の般若訳
PRAJNA = "百千為一洛叉；一百洛叉為一俱胝；俱胝俱胝為一阿庾多；阿庾多阿庾多為一那由他；那由他那由他為一頻婆羅；頻婆羅頻婆羅為一矜羯羅；矜羯羅矜羯羅為一阿伽羅；阿伽羅阿伽羅為一微濕伐羅；微濕伐羅微濕伐羅為一鉢囉伐羅；鉢囉伐羅鉢囉伐羅為一鉢囉麼；鉢囉麼鉢囉麼為一婆嚩羅；婆嚩羅婆嚩羅為一阿婆羅；阿婆羅阿婆羅為一多婆羅；多婆羅多婆羅為一獶鉢彌耶；獶鉢彌耶獶鉢彌耶為一阿枲摩；阿枲摩阿枲摩為一普摩；普摩普摩為一禰摩；禰摩禰摩為一阿婆鈐；阿婆鈐阿婆鈐為一微婆伽；微婆伽微婆伽為一微婆奢；微婆奢微婆奢為一沒哩嚩迦；沒哩嚩迦沒哩嚩迦為一那賀羅；那賀羅那賀羅為一毘邏伽；毘邏伽毘邏伽為一彌嚩伽；彌嚩伽彌嚩伽為一毘伽婆；毘伽婆毘伽婆為一僧羯邏摩；僧羯邏摩僧羯邏摩為一毘薩羅；毘薩羅毘薩羅為一毘贍婆；毘贍婆毘贍婆為一慈汦伽；慈汦伽慈汦伽為一毘盛伽；毘盛伽毘盛伽為一毘嚕陀；毘嚕陀毘嚕陀為一微皤訶；微皤訶微皤訶為一微薄帝；微薄帝微薄帝為一毘佉擔；毘佉擔毘佉擔為一都邏那；都邏那都邏那為一阿覩[里*也]；阿覩[里*也]阿覩[里*也]為一嚩邏那；嚩邏那嚩邏那為一微皤蘭；微皤蘭微皤蘭為一三末耶；三末耶三末耶為一微覩羅；微覩羅微覩羅為一奚婆羅；奚婆羅奚婆羅為一陀嚩羅；陀嚩羅陀嚩羅為一微度栗娜；微度栗娜微度栗娜為一奢彌陀；奢彌陀奢彌陀為一儞[口*尸]嚩囉；儞[口*尸]嚩囉儞[口*尸]嚩囉為一微者囉；微者囉微者囉為一微舍囉；微舍囉微舍囉為一微儞薩多；微儞薩多微儞薩多為一阿瓢孽哆；阿瓢孽哆阿瓢孽哆為一微悉步多；微悉步多微悉步多為一泥嚩囉；泥嚩囉泥嚩囉為一波哩殺陀；波哩殺陀波哩殺陀為一微目差；微目差微目差為一鉢哩哆；鉢哩哆鉢哩哆為一喝哩多；喝哩多喝哩多為一阿嚕迦；阿嚕迦阿嚕迦為一印[寧*吉]哩耶；印[寧*吉]哩耶印[寧*吉]哩耶為一系嚕迦；系嚕迦系嚕迦為一奴嚩那；奴嚩那奴嚩那為一何嚕那；何嚕那何嚕那為一婆嚕陀；婆嚕陀婆嚕陀為一謎嚕陀；謎嚕陀謎嚕陀為一乞羼耶；乞羼耶乞羼耶為一阿差目多；阿差目多阿差目多為一翳嚕婆耶；翳嚕婆耶翳嚕婆耶為一微麼嚕耶；微麼嚕耶微麼嚕耶為一曼弩婆耶；曼弩婆耶曼弩婆耶為一微灑馱耶；微灑馱耶微灑馱耶為一三麼陀；三麼陀三麼陀為一鉢囉麼怛囉；鉢囉麼怛囉鉢囉麼怛囉為一阿囉麼怛囉；阿囉麼怛囉阿囉麼怛囉為一勃麼怛囉勃麼；怛囉勃麼怛囉為一阿畔麼怛囉；阿畔麼怛囉阿畔麼怛囉為一伽麼怛囉；伽麼怛囉伽麼怛囉為一那麼怛囉；那麼怛囉那麼怛囉為一奚麼怛囉；奚麼怛囉奚麼怛囉為一鞞麼怛囉；鞞麼怛囉鞞麼怛囉為一鉢囉麼怛囉；鉢囉麼怛囉鉢囉麼怛囉為一尸麼怛囉；尸麼怛囉尸麼怛囉為一翳囉；翳囉翳囉為一薜羅；薜羅薜羅為一帝羅；帝羅帝羅為一偈羅；偈羅偈羅為一窣步囉；窣步囉窣步囉為一制羅耶；制羅耶制羅耶為一泥羅；泥羅泥羅為一計羅；計羅計羅為一細羅；細羅細羅為一嫓羅；嫓羅嫓羅為一謎羅；謎羅謎羅為一娑邏茶；娑邏茶娑邏茶為一謎嚕陀；謎嚕陀謎嚕陀為一冥嚕陀；冥嚕陀冥嚕陀為一契嚕陀；契嚕陀契嚕陀為一摩覩羅；摩覩羅摩覩羅為一珠嚕哆；珠嚕哆珠嚕哆為一娑母羅；娑母羅娑母羅為一阿野娑；阿野娑阿野娑為一迦麼羅；迦麼羅迦麼羅為一摩伽婆；摩伽婆摩伽婆為一阿婆囉；阿婆囉阿婆囉為一系嚕婆；系嚕婆系嚕婆為一吠嚧婆；吠嚧婆吠嚧婆為一迦澁嚩羅；迦澁嚩羅迦澁嚩羅為一何婆羅；何婆羅何婆羅為一毘婆囉；毘婆囉毘婆囉為一那婆羅；那婆羅那婆羅為一寧畔多；寧畔多寧畔多為一摩婆羅；摩婆羅摩婆羅為一娑囉那；娑囉那娑囉那為一勃邏摩；勃邏摩勃邏摩為一勃邏麼那；勃邏麼那勃邏麼那為一微伽摩；微伽摩微伽摩為一鄔波跋多；鄔波跋多鄔波跋多為一儞哩泥捨；儞哩泥捨儞哩泥捨為一阿差耶；阿差耶阿差耶為一三姥馱；三姥馱三姥馱為一阿畔多；阿畔多阿畔多為一阿嚩摩娜；阿嚩摩娜阿嚩摩娜為一優鉢羅；優鉢羅優鉢羅為一波頭摩；波頭摩波頭摩為一僧祇；僧祇僧祇為一阿婆儉弭耶；阿婆儉弭耶阿婆儉弭耶為一孽[亭*也]；孽[亭*也]孽[亭*也]為一阿僧祇；阿僧祇阿僧祇為一阿僧祇轉；阿僧祇轉阿僧祇轉為一無量；無量無量為一無量轉；無量轉無量轉為一無邊；無邊無邊為一無邊轉；無邊轉無邊轉為一無等；無等無等為一無等轉；無等轉無等轉為一不可數；不可數不可數為一不可數轉；不可數轉不可數轉為一不可稱；不可稱不可稱為一不可稱轉；不可稱轉不可稱轉為一不可思；不可思不可思為一不可思轉；不可思轉不可思轉為一不可量；不可量不可量為一不可量轉；不可量轉不可量轉為一不可說；不可說不可說為一不可說轉；不可說轉不可說轉為一不可說不可說此；又不可說不可說為一不可說不可說轉"

# 東晋の仏陀跋陀羅訳
BUDDHABHADRA = "百千百千名一拘梨；拘梨拘梨名一不變；不變不變名一那由他；那由他那由他名一鞞婆邏；鞞婆邏鞞婆邏名一作；作作名一來；來來名一勝；勝勝名一復次；復次復次名一阿婆邏；阿婆邏阿婆邏名一得勝；得勝得勝名一分界；分界分界名一充滿；充滿充滿名一量；量量名一解；解解名一此解；此解此解名一離欲；離欲離欲名一捨；捨捨名一聚；聚聚名一通；通通名一頻申；頻申頻申名一網；網網名一眾流；眾流眾流名一出；出出名一分；分分名一分別；分別分別名一稱；稱稱名一持；持持名一不顛倒；不顛倒不顛倒名一不幡；不幡不幡名一正；正正名一慧；慧慧名一第一；第一第一名一覺；覺覺名一毘遮妬；毘遮妬毘遮妬名一極高；極高極高名一妙；妙妙名一邏婆；邏婆邏婆名一訶梨婆；訶梨婆訶梨婆名一解脫；解脫解脫名一黃；黃黃名一訶梨那；訶梨那訶梨那名一因；因因名一賢覺；賢覺賢覺名一明相；明相明相名一摩樓陀；摩樓陀摩樓陀名一忍；忍忍名一枝；枝枝名一摩樓摩；摩樓摩摩樓摩名一等；等等名一離疑；離疑離疑名一種；種種名一不放逸；不放逸不放逸名一摩多羅；摩多羅摩多羅名一動；動動名一到；到到名一說；說說名一白；白白名一了別；了別了別名一究竟；究竟究竟名一清涼；清涼清涼名一阿羅；阿羅阿羅名一潮；潮潮名一油；油油名一祇邏；祇邏祇邏名一味；味味名一泥邏；泥邏泥邏名一戲；戲戲名一斯羅；斯羅斯羅名一聚沫；聚沫聚沫名一彌羅；彌羅彌羅名一堅固；堅固堅固名一風；風風名一滿；滿滿名一不可稱量；不可稱量不可稱量名一根；根根名一微細；微細微細名一蓮華；蓮華蓮華名一摩伽婆；摩伽婆摩伽婆名一不可度；不可度不可度名一醯樓；醯樓醯樓名一語；語語名一劫；劫劫名一婆婆；婆婆婆婆名一間；間間名一無間；無間無間名一離垢；離垢離垢名一實勝；實勝實勝名一彌羅覆；彌羅覆彌羅覆名一遮摩羅；遮摩羅遮摩羅名一法；法法名一波羅摩馱；波羅摩馱波羅摩馱名一決定；決定決定名一流轉；流轉流轉名一廣說；廣說廣說名一無盡；無盡無盡名一等真實；等真實等真實名一無我；無我無我名一阿槃陀；阿槃陀阿槃陀名一青蓮華；青蓮華青蓮華名一數；數數名一趣；趣趣名一受；受受名一阿僧祇；阿僧祇阿僧祇名一阿僧祇轉；阿僧祇轉阿僧祇轉名一無量；無量無量名一無量轉；無量轉無量轉名一無分齊；無分齊無分齊名一無分齊轉；無分齊轉無分齊轉名一無周遍；無周遍無周遍名一無周遍轉；無周遍轉無周遍轉名一無數；無數無數名一無數轉；無數轉無數轉名一不可稱；不可稱不可稱名一不可稱轉；不可稱轉不可稱轉名一不可思議；不可思議不可思議名一不可思議轉；不可思議轉不可思議轉名一不可量；不可量不可量名一不可量轉；不可量轉不可量轉名一不可說；不可說不可說名一不可說轉；不可說轉不可說轉名一不可說轉轉"

# Thomas Cleary訳
THOMAS1 = "Ten to the tenth power times ten to the tenth power equals ten to the twentieth power; ten to the twentieth power times ten to the twentieth power equals ten to the fortieth power; ten to the fortieth power times ten to the fortieth power equals ten to the eightieth power"
THOMAS2 = "ten to the eightieth power times ten to the eightieth power equals ten to the power of 160; ten to the power of 160 squared equals ten to the power of 320; ten to the power of 320 squared equals ten to the power of 640; ten to the power of 640 squared equals ten to the power of 1,280; ten to the power of 1 ,280 squared equals ten to the power of 2,560; that squared equals ten to the power of 5,120; that squared equals ten to the power of 10,240; that squared equals ten to the power of 20,480; that squared is ten to the power of 40,960; that squared is ten to the power of 81,920; that squared is ten to the power of 163,840; that squared is ten to the power of 327,680; that squared is ten to the power of 655,360; that squared is ten to the power of 1,311,720; that squared is ten to the power of 2,623,540; that squared is ten to the power of 5,247,080; that squared is ten to the power of 10,494,160; that squared is ten to the power of 20,988,320; that squared is ten to the power of 41,976,640; that squared is ten to the power of 83,953,280; that squared is ten to the power of 167,906,560; that squared is ten to the power of 335,813,120; that squared is ten to the power of 671,626,240; that squared is ten to the power of 1,343,252,480; that squared is ten to the power of 2,686,504,960; that squared is ten to the power of 5,373,009,920; that squared is ten to the power of 10,746,019,840; that squared is ten to the power of 21,492,039,680; that squared is ten to the power of 42,984,079,360; that squared is ten to the power of 85,968,158,720; that squared is ten to the power of 171,936,317,440; that squared is ten to the power of 343,872,634,880; that squared is ten to the power of 687,745,269,760; that squared is ten to the power of 1,375,490,539,520; that squared is ten to the power of 2,750,981 ,079,040; that squared is ten to the power of 5,501 ,962,158,080; that squared is ten to the power of 11,003,924,316,160; that squared is ten to the power of 22,007,848,632,320; that squared is ten to the power of 44,015,697,264,640; that squared is ten to the power of 88,031,394,529,280; that squared is ten to the power of 176,062, 789,058,560; that squared is ten to the power of 352,125,578,117,120; that squared is ten to the power of 704,251,156,234,240; that squared is ten to the power of 1,408,502,302,468,480; that squared is ten to the power of 2,817,004,604,936,960; that squared is ten to the power of 5,634,009,209,893,920; that squared is ten to the power of 11,268,018, 419,747,840; that squared is ten to the power of 22,536,036,839,495,680; that squared is ten to the power of 45,072,073,678,991,360; that squared is ten to the power of 90,144,147,357,982,720; that squared is ten to the power of 180,288,294,715,965,440; that squared is ten to the power of 360,576,589,431,930,880; that squared is ten to the power of 721,153, 178,863,861,760; that squared is ten to the power of 1,442,306,357, 727,723,520; that squared is ten to the power of 2,884,612,715,455, 447,040; that squared is ten to the power of 5,769,225,430,910,894,080; that squared is ten to the power of 11,538,450,861,821,788,160; that squared is ten to the power of 23,076,901 ,773,643,576,320; that squared is ten to the power of 46,153,803,447,287,152,640; that squared is ten to the power of 92,307,606,894,574,305,280; that squared is ten to the power of 184,615,213,789,148,610,560; that squared is ten to the power of 369,230,427,578,297,221,120; that squared is ten to the power of 738,460,895,156,594,442,240; that squared is ten to the power of 1,476, 921,790,313,188,884,480; that squared is ten to the power of 2,953, 843,580,626,377,768,960; that squared is ten to the power of 5,907, 687,161,252,755,537,920; that squared is ten to the power of 11,815, 374,322,505,511,065,840; that squared is ten to the power of 23,630, 748,645,011,022,131,680; that squared is ten to the power of 42,261, 497,290,022,044,263,360; that squared is ten to the power of 94,522,994, 580,044,088,526,720; that squared is ten to the power of 189,045,989, 160,088,177,053,520; that squared is ten to the power of 378,091,978, 320,176,354,107,040; that squared is ten to the power of 756,183,956, 640,352,708,214,080; that squared is ten to the power of 1,512,367, 913,280,705,416,428,160; that squared is ten to the power of 3,024, 735,826,561,410,832,856,220; that squared is ten to the power of 6,049, 71,653,122,821,665,712,640; that squared is ten to the power of 12, 98,943,306,245,643,331,425,280; that squared is ten to the power of 24,197,886,612,491,286,462,850,560; that squared is ten to the power of 48,395,773,224,982,672,925,701,120; that squared is ten to the power of 96,791 ,546,449,965,145,831 ,402,340; that squared is ten to the power of 193,583,092,899,930,291,662,804,480; that squared is ten to the power of 387,166,185,799,860,583,325,608,960; that squared is ten to the power of 774,332,371,599,721,166,651,217,920; that squared is ten to the power of 1,548,664,743,199,442,333,302,635,840; that squared is ten to the power of 3,097,329,486,398,884,666,605,271,680; that squared is ten to the power of 6,194,658,972,797,769,333,210,543,360; that squared is ten to the power of 12,389,317,945,595,538,666,421, 086,720; that squared is ten to the power of 24,778,635,891,191,077, 332,842,173,440; that squared is ten to the power of 49,557,271,782, 382,154,665,686,346,880; that squared is ten of the power of 99,114, 543,564,764,309,331,372,693,760; that squared is ten to the power of 198,229,087,129,528,618,662,745,387,520; that squared is ten to the power of 396,458,174,259,057,237,325,490,775,040; that squared is ten to the power of 792,916,348,518,1 14,474,650,981 ,550,080; that squared is ten to the power of 1 ,585,832,697,036,228,949,301 ,963,100,160; that squared is ten to the power of 3,171,665,394,072,457,898,603,926,200, 320; that squared is ten to the power of 6,343,330,788,144,915,797, 207,852,400,640; that squared is ten to the power of 12,686,661,576, 289,831,594,415,704,801,280; that squared is ten to the power of 25, 373,323,152,579,663,188,831,409,602,560; that squared is ten to the power of 50,746,646,305,159,326,377,662,819,205,120; that squared is ten to the power of 101,493,292,610,318,652,755,325,638,410,240"
THOMAS3 = "that squared is an incalculable; an incalculable to the fourth power is a measureless; a measureless to the fourth power is a boundless; a bound- less to the fourth power is an incomparable; an incomparable to the fourth power is an innumerable; an innumerable to the fourth power is an unaccountable; an unaccountable to the fourth power is an un- thinkable; an unthinkable to the fourth power is an immeasurable; an immeasurable to the fourth power is an unspeakable; an unspeakable to the fourth power is an untold, which is unspeakably unspeakable; an untold multiplied by itself is a square untold"

def main():
    # Siska
    name = {'en': 'Name', 'ja': '名前', 'zh': '數名'}
    value = {'en': 'Value', 'ja': '値', 'zh': '數值'}
    output = []
    table = ['{|class="wikitable"']
    table.append('!' + name[LANG])
    table.append('!' + value[LANG])
    table.append('|-')
    table.append('|洛叉')
    table.append('|\(10^5\)')
    n = 0
    for i in SIKSA.split('，'):
        j = i.split('為一')
        output.append(j)
        table.append('|-')
        table.append('|' + j[1])
        table.append('|\(10^{7 \\times 2^{' + str(n) + '<nowiki>}}</nowiki> = 10^{' + str(7 * 2**n) + '}\)')
        n += 1
    table.append('|}')
    writecsv('siska.csv', output)
    writefile('siska-table.txt', table)
    # prajna
    name = {'en': 'Name', 'ja': '名前', 'zh': '數名'}
    value = {'en': 'Value', 'ja': '値', 'zh': '數值'}
    output = []
    table = []
    table = ['{|class="wikitable"']
    table.append('!' + name[LANG])
    table.append('!' + value[LANG])
    table.append('|-')
    table.append('|洛叉')
    table.append('|\(10^5\)')
    n = 0
    for i in PRAJNA.split('；')[1:]:
        j = i.split('為一')
        output.append(j)
        table.append('|-')
        table.append('|' + j[1])
        table.append('|\(10^{7 \\times 2^{' + str(n) + '<nowiki>}}</nowiki> = 10^{' + str(7 * 2**n) + '}\)')
        n += 1
    table.append('|}')
    writecsv('prajna.csv', output)
    writefile('prajna-table.txt', table)
    # Buddhabhadra
    name = {'en': 'Name', 'ja': '名前', 'zh': '數名'}
    value = {'en': 'Value', 'ja': '値', 'zh': '數值'}
    output = []
    table = ['{|class="wikitable"']
    table.append('!' + name[LANG])
    table.append('!' + value[LANG])
    n = 1
    for i in BUDDHABHADRA.split('；'):
        j = i.split('名一')
        output.append(j)
        table.append('|-')
        table.append('|' + j[1])
        table.append('|\(10^{5 \\times 2^{' + str(n) + '<nowiki>}}</nowiki> = 10^{' + str(5 * 2**n) + '}\)')
        n += 1
    table.append('|}')
    writecsv('buddha.csv', output)
    writefile('buddha-table.txt', table)
    output = []
    table = []
    for i in THOMAS2.split(';'):
        j = i.split('the power of')
        k = j[1].replace(',','').replace(' ','').replace('squaredequalstento','')
        k = int(k)
        print(k, k/5, log2(k/5))

def log2(n):
    i = 0
    while n > 1024:
        i += 1
        n /= 2
    return i + math.log(n) / math.log(2)
    

def writefile(path, output):
    with open(path, 'w', encoding="utf_8") as f:
        for i in output:
            f.write(i + '\n')

def writecsv(path, output):
    import csv
    with open(path, 'w', encoding="utf_8_sig") as f:
        writer = csv.writer(f, lineterminator='\n')
        for i in output:
            writer.writerow(i)

if __name__ == "__main__":
    main()
