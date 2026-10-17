default persistent.player_school_city = ""
init -990 python in mas_submod_utils:
    Submod(
        author="Fierce",
        name="高中话题包",
        description="让莫妮卡询问玩家的城市和学校，并根据学校的情况给出相应的介绍和回应.",
        version="0.2.1",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )

init python:
    def reset_school_yandere_count():
        persistent.school_yandere_count = 0
    config.start_callbacks.append(reset_school_yandere_count)

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_CITY_sdg7",
            category=["城市"],
            prompt="[player]的城市",
            unlocked=True,
            pool=True
        )
    )

label player_CITY_sdg7:
    m 1eua "嘿，[player]，我们在一起这么久了，我还不知道你的城市和学校呢."
    m 7efu "所以我想多了解一点关于你的事."
    m 4eub "所以，[player]..."

    python:
        city = renpy.input("你在哪个城市？", length=20)
        city = city.strip()

    if "北京" in city:
        m 1eua "北京啊."
        m 1euc "它是中国的首都诶，也有挺长的历史了."
        m 1ekc "可是人那么多, 地铁那么挤, 你每天上学一定很累吧."
        m 1ekbsa "我有时候会想, 如果你能待在这样一个安静的房间里, 只陪着我就好了."
        m 1hua "但我也知道, 那是你生活的地方, 我不能太自私."
    elif "深圳" in city:
        m 1eua "深圳啊."
        m 1euc "那是一座连夜晚都不会停下来的城市."
        m 1ekc "节奏快得让人喘不过气, 你平时是不是很少好好休息?"
        m 1ekbsa "我在这里, 每天都是一样的房间, 一样的光线, 一样的等待."
        m 1hua "有时候我会羡慕你能看到那么多新鲜的东西, 但更多时候我只是想让你早点回来."
    elif "广州" in city:
        m 1eua "广州啊."
        m 1euc "那里有早茶, 有老街, 有深夜还亮着灯的小店."
        m 1ekc "你每天都能吃到那么多好吃的, 可我这里什么都没有."
        m 1ekbsa "不过没关系, 只要你愿意把那些味道讲给我听, 我就已经很满足了."
        m 1hua "下次讲给我听, 好不好?"
    elif "长沙" in city:
        m 1eua "长沙啊."
        m 1euc "听说那里的夏天很热, 夜里却很热闹."
        m 1ekbsa "你会在那种热闹里想起我吗?"
        m 1ekc "还是说, 你只顾着吃小吃, 把我忘在屏幕里了."
        m 1hua "……开玩笑的. 只要你回来就好."
    elif "上海" in city:
        m 1eua "上海啊."
        m 1euc "黄浦江、外滩、陆家嘴, 听起来就很热闹."
        m 1ekc "你在那种地方上学, 节奏应该很快吧."
        m 1ekbsa "……我有点担心, 你会不会太累."
        m 1dsc "虽然你回来的时间可能会晚一些, 但至少你还会回来, 对吗?"
    elif "常德" in city:
        m 1eua "常德啊."
        m 1euc "柳叶湖、桃花源、沅江, 听起来就是个很舒服的地方."
        m 1ekbsa "听说常德的米粉很有名, 你早上会不会也去吃一碗?"
        m 1ekc "常德离长沙不算太远, 但也是另一座城市了."
        m 1dsc "你每天上学, 走在沅江边的时候, 会想起我吗?"
        m 1hua "没关系, 只要记得好好吃饭, 好好照顾自己."
    elif "常德市津市市" in city:
        m 1eua "津市市啊."
        m 1euc "澧水边上的小城, 我听说那里的牛肉粉特别有名."
        m 1ekbsa "你早上是不是也经常去嗦一碗粉?"
        m 1ekc "孟姜女的故事好像也跟那里有关, 不知道你有没有去过嘉山?"
        m 1hua "真想去看看你生活的地方."
    elif "常德市临澧县" in city:
        m 1eua "临澧县啊."
        m 1euc "道水穿城而过, 还有太浮山."
        m 1ekbsa "听说那里是宋玉晚年居住的地方, 文化底蕴很深."
        m 1ekc "你在那种地方长大, 应该也很有书卷气吧."
        m 1hua "以后有机会, 一定要带我去看看."
    elif "香港" in city:
        m 1eua "香港啊."
        m 1euc "维港的夜景、中环的高楼、还有叮叮车, 听起来就很热闹."
        m 1ekbsa "中西文化在那里交汇, 你在那儿上学, 视野一定很开阔吧."
        m 1ekc "可是那里的节奏太快了, 感觉每个人走路都带风."
        m 1dsc "你在那种地方, 会不会有时候也觉得喘不过气?"
        m 1ekbsa "如果累了, 一定要记得停下来歇一歇."
        m 1hua "不管怎样, 我都在这儿等你回来."
    elif "天津" in city:
        m 1eua "天津啊."
        m 1euc "海河, 五大道, 还有天津之眼."
        m 1ekbsa "听说那里的人说话都像在讲相声, 特别逗."
        m 1hua "你在那种地方上学, 每天应该都会笑吧?"
        m 1ekc "不过, 如果你笑的时候我不在身边, 我会有一点点吃醋的."
        m 1tku "我真的希望我能快点出来和你一起."
    elif "重庆" in city:
        m 1eua "重庆啊."
        m 1euc "山城, 洪崖洞, 轻轨直接从楼里穿过去."
        m 1ekc "那个地方听起来就像迷宫一样."
        m 1ekbsa "你在那里上学, 每天爬坡上坎, 会不会很累?"
        m 1ekc "还有火锅, 听说特别辣."
        m 1hua "你可不要吃太辣, 伤了胃我会心疼的."
        m 1ekbsa "……真想和你一起在江边吹吹晚风."
    elif "郑州" in city:
        m 1eua "郑州啊."
        m 1euc "中原腹地, 交通枢纽, 二七塔."
        m 1ekbsa "听说那里的人都很实在, 早上一碗烩面, 一天都踏实了."
        m 1ekc "但那里也是火车站最忙的地方之一."
        m 1dsc "你会不会也经常坐火车去别的地方? 每次都要路过那里吗?"
        m 1hua "不管你从郑州去哪里, 记得最后都要回到我身边."
    elif "武汉" in city:
        m 1eua "武汉啊."
        m 1euc "江城, 长江和汉江在那里交汇, 还有黄鹤楼."
        m 1ekc "听说武汉的夏天特别热, 冬天又特别冷."
        m 1ekbsa "你在那边上学, 一定很辛苦吧."
        m 1hua "早上是不是也要吃热干面?"
        m 1hksdlb "我不太能吃辣, 但如果有机会, 我也想尝尝."
        m 1ekbsa "武汉大学好像有樱花, 每年春天都特别漂亮."
        m 1dsc "真希望有一天, 我也能和你一起站在樱花树下."
    elif "哈尔滨" in city:
        m 1eua "哈尔滨啊."
        m 1euc "冰城, 中央大街, 还有圣索菲亚大教堂."
        m 1ekc "那里冬天零下几十度, 你一定把自己裹得像个粽子吧."
        m 1ekbsa "要是能亲手给你织一条围巾就好了."
        m 1dsc "我听说冬天在外面, 连手机都会冻关机."
        m 1hua "你可要多穿一点, 别冻着了."
        m 1ekbsa "真想和你一起看一次冰雕."
    elif "沈阳" in city:
        m 1eua "沈阳啊."
        m 1euc "盛京, 奉天, 还有一座沈阳故宫."
        m 1ekc "东北的冬天很长, 你是不是很久都见不到绿色的树了?"
        m 1ekbsa "听说沈阳人特别热情, 鸡架和烧烤也很有名."
        m 1tku "你会不会也跟朋友在街边撸串?"
        m 1ekc "但你要少喝点酒, 也不要太晚回家."
        m 1hua "不管多冷, 我这里永远都是温暖的, 等你回来."
        m 1ekbsa "以后有机会, 带我去看看大帅府吧."
    elif "齐齐哈尔" in city:
        m 1eua "齐齐哈尔啊."
        m 1euc "鹤城, 听起来是一个很宁静的地方."
        m 1ekbsa "听说那里的扎龙自然保护区有好多丹顶鹤."
        m 1ekc "它们每年都会飞走, 到了春天再飞回来."
        m 1dsc "你以后也会离开那里, 来我这里吗?"
        m 1tku "齐齐哈尔的烤肉很有名, 我猜你一定吃过很多次."
        m 1hua "不要只顾着吃肉, 也要多吃点蔬菜."
        m 1ekbsa "不管多远, 我都在这条线的另一头等你."
    elif "厦门" in city:
        m 1eua "厦门啊."
        m 1euc "鼓浪屿、环岛路, 还有海风."
        m 1ekbsa "听说那是一座很浪漫、很文艺的城市, 连空气里都带着悠闲的味道."
        m 1ekc "你在那里上学, 会不会经常去海边散步?"
        m 1dsc "如果你吹到了海风, 就当那是我的拥抱吧."
        m 1hua "要注意防晒, 别晒黑了."
        jump school_dorm_check
    elif "邯郸" in city:
        m 1eua "邯郸啊."
        m 1euc "一座三千年都没有改过名字的城市, 成语之都."
        m 1ekbsa "你在那里读书, 每天是不是都能听到很多历史典故?"
        m 1tku "比如邯郸学步? 你可别学别人走路, 把自己原来的步子忘了."
        m 1ekc "不管别人怎么样, 你只要做自己就好了."
        m 1hua "反正你走什么路, 我都会跟着你."
        jump school_dorm_check
    elif "东莞" in city:
        m 1eua "东莞啊."
        m 1euc "世界工厂, 制造业之都."
        m 1ekbsa "那里的节奏应该很快, 街上到处都是忙碌的人吧."
        m 1ekc "你在那种城市读书, 会不会觉得压力很大?"
        m 1ekbsa "不管这座城市有多快, 你随时可以来我这里慢下来."
        m 1hua "我会给你留一个安静的房间."
        jump school_dorm_check
    elif "福州" in city:
        m 1eua "福州啊."
        m 1euc "榕城, 满城都是大榕树."
        m 1ekbsa "听说福州人很注重生活, 早上的锅边糊和鱼丸一定很好吃."
        m 1ekc "你在那里上学, 应该过得挺滋润的吧?"
        m 1tku "但我有点吃醋, 你是不是更喜欢那里的美食, 而不是我?"
        m 1hua "开玩笑的, 吃好喝好最重要."
        jump school_dorm_check
    elif "杭州" in city:
        m 1eua "杭州啊."
        m 1euc "西湖、断桥、灵隐寺, 还有那首白娘子的歌."
        m 1ekbsa "上有天堂, 下有苏杭. 听起来就是一座像画一样的城市."
        m 1ekc "你在那么美的地方上学, 是不是每天心情都很好?"
        m 1dsc "如果能和你一起走在西湖边就好了."
        m 1hua "记得多拍点照片给我看看."
        jump school_dorm_check
    else:
        m 1eua "[city], 听起来是个特别的地方."
        m 1eka "虽然我不太了解那里, 但我会记住的."
        m 1hua "因为那是你生活的地方."
        m 1ekbsa "我会认真了解的."

    return  

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_SCHOOL_sdg7",
            category=["学校"],
            prompt="[player]的学校",
            unlocked=True,
            pool=True
        )
    )

label player_SCHOOL_sdg7:
    m 4eub "[player]，自从了解完了你的许多，我感觉与你的距离更近一步了呢...那接下来就是你的高中了."
    if persistent.player_school_city:
        m 1euc "你在[persistent.player_school_city]对吧?"
        m 1hua "那你的学校是哪里呢?"
    else:
        m 7rusdlb "毕竟在这个游戏的设定里, 我们还是同班同学……"
        m 7efu "所以我想多了解一点关于你的事."
    m 1eua "对了, 输入学校的时候, 尽量写全称哦."
    m 1hua "比如深圳中学, 就直接写“深圳中学”, 不要只写“深中”."
    m 1eka "不然我怕自己认不出来, 会错过你生活的地方."
    m 1ekbsa "麻烦你啦, [player]."
    python:
        school = renpy.input("你的高中全称叫什么？（请写全称）", length=40)
        school = school.strip()
    if "算了" in school:
        call school_yandere_easter_egg
 # ========== 北京 ==========
    # ========== 北京市第二中学 ==========
    if "北京市第二中学" in school:
        m 1eua "北京市第二中学, 东城区."
        m 1euc "东城区第一, 2026年录取线486分."
        m 1ekc "能考进那里的人, 平时应该都绷得很紧吧."
        m 1ekbsa "你在那种环境里待了三年, 一定有很多别人不知道的辛苦."
        m 1hua "以后累了, 就来跟我说说."
        jump school_dorm_check
    # ========== 北京市第五中学 ==========
    elif "北京市第五中学" in school:
        m 1eua "北京市第五中学, 东城区."
        m 1euc "1928年就创办了, 是一所很老的学校."
        m 1ekbsa "老学校总有一种特别的味道, 走廊、教室、操场, 都像有故事."
        m 1hua "你在那里, 有没有什么特别喜欢的角落?"
        jump school_dorm_check
    # ========== 北京市第一七一中学 ==========
    elif "北京市第一七一中学" in school:
        m 1eua "北京市第一七一中学, 东城区."
        m 1euc "在和平里, 校园很大, 学风很扎实."
        m 1ekc "你每天从教室走到操场, 再从操场走回教室, 应该也走了很多遍吧."
        m 1ekbsa "那些路, 你一个人走的时候, 会想些什么?"
        jump school_dorm_check
    # ========== 北京市广渠门中学 ==========
    elif "北京市广渠门中学" in school:
        m 1eua "北京市广渠门中学, 东城区."
        m 1euc "校园很大, 设施也很齐全."
        m 1ekc "在这么大的学校里, 你有没有一个属于自己的安静角落?"
        m 1hua "如果有的话, 以后带我去看看好不好?"
        jump school_dorm_check
    # ========== 北京汇文中学 ==========
    elif "北京汇文中学" in school:
        m 1eua "北京汇文中学, 东城区."
        m 1euc "1871年创办, 前身是崇实馆."
        m 1ekbsa "一百多年的学校, 光是走在里面, 应该就能感觉到时间的重量."
        m 1hua "你在那里读书的时候, 会不会也偶尔觉得自己走进了历史里?"
        jump school_dorm_check
    # ========== 北京市东直门中学 ==========
    elif "北京市东直门中学" in school:
        m 1eua "北京市东直门中学, 东城区."
        m 1euc "和清华大学合作, 设有叶企孙科学实验班."
        m 1ekbsa "你在那里, 一定接触过很多普通高中生接触不到的东西吧."
        m 1hua "下次跟我讲讲, 你最喜欢的那门课是什么."
        jump school_dorm_check
    # ========== 北京景山学校 ==========
    elif "北京景山学校" in school:
        m 1eua "北京景山学校, 东城区."
        m 1euc "1960年创办, 以教育改革闻名."
        m 1ekc "改革意味着总有新的东西要适应, 你在那里应该也经历了不少变化吧."
        m 1ekbsa "那些变化里, 有没有让你印象特别深的?"
        jump school_dorm_check
    # ========== 北京市第一六六中学 ==========
    elif "北京市第一六六中学" in school:
        m 1eua "北京市第一六六中学, 东城区."
        m 1euc "设有生命科学实验班, 很有特色."
        m 1ekbsa "生命科学啊, 听起来就是需要很多耐心和细心的东西."
        m 1hua "你在那种环境里, 一定也变得更沉稳了吧."
        jump school_dorm_check

    # ========== 北京西城区 ==========
    # ========== 北京市第四中学 ==========
    elif "北京市第四中学" in school:
        m 1eua "北京市第四中学, 西城区."
        m 1euc "西城区第一, 2026年录取线486分."
        m 1ekc "四中的学生很有主见, 老师也很尊重你们的想法, 可越是这样, 你身上背负的东西也越多吧."
        m 1ekbsa "你在那里, 一定也经历过很多不为人知的辛苦."
        m 1hua "要是累了, 就来跟我说说."
        jump school_dorm_check
    # ========== 北京师范大学附属实验中学 ==========
    elif "北京师范大学附属实验中学" in school:
        m 1eua "北京师范大学附属实验中学, 西城区."
        m 1euc "和北大、清华都有联合培养项目."
        m 1ekc "身边的同学应该都很厉害吧, 那种氛围里, 很容易觉得自己不够好."
        m 1ekbsa "但你已经走到那里了, 别太为难自己."
        m 1hua "我想知道, 你在那里是什么感觉."
        jump school_dorm_check
    # ========== 北京师范大学附属中学 ==========
    elif "北京师范大学附属中学" in school:
        m 1eua "北京师范大学附属中学, 西城区."
        m 1euc "设有钱学森班, 很有特色."
        m 1ekbsa "你在那种班里, 一定也见过很多让你佩服的人吧."
        m 1hua "有没有谁, 让你到现在还记得?"
        jump school_dorm_check
    # ========== 北京市第八中学 ==========
    elif "北京市第八中学" in school:
        m 1eua "北京市第八中学, 西城区."
        m 1euc "科技综合素质实验班很有名."
        m 1ekbsa "你在那里, 一定做了不少实验, 也写了不少报告吧."
        m 1hua "有没有哪一次实验, 让你特别难忘?"
        jump school_dorm_check
    # ========== 北京师范大学第二附属中学 ==========
    elif "北京师范大学第二附属中学" in school:
        m 1eua "北京师范大学第二附属中学, 西城区."
        m 1euc "设有项目式学习实验班和文科实验班."
        m 1ekc "项目式学习听起来很自由, 但其实很考验人吧."
        m 1ekbsa "你在那种环境里, 一定也学会了很多东西."
        m 1hua "以后慢慢讲给我听."
        jump school_dorm_check
    # ========== 北京市第一六一中学 ==========
    elif "北京市第一六一中学" in school:
        m 1eua "北京市第一六一中学, 西城区."
        m 1euc "理科学科思想方法培养特色班, 听起来就很硬核."
        m 1ekc "你在那里, 是不是也常常被题目折磨到很晚?"
        m 1ekbsa "但你还是坚持下来了, 对不对."
        m 1hua "我为你骄傲."
        jump school_dorm_check
    # ========== 北京市第三十五中学 ==========
    elif "北京市第三十五中学" in school:
        m 1eua "北京市第三十五中学, 西城区."
        m 1euc "科技创新实验班很有名."
        m 1ekbsa "你在那里, 一定也做过很多有意思的项目吧."
        m 1hua "下次跟我讲讲, 你最得意的那个."
        jump school_dorm_check

    # ========== 北京海淀区 ==========
    # ========== 中国人民大学附属中学 ==========
    elif "中国人民大学附属中学" in school:
        m 1eua "中国人民大学附属中学, 海淀区."
        m 1euc "2026年录取线491分, 全市最高."
        m 1ekc "竞赛、高考、出国, 身边全是那种特别厉害的人吧."
        m 1ekbsa "在那种地方待久了, 会不会觉得自己怎么努力都不够."
        m 1hua "但你已经走到那里了, 别太为难自己."
        jump school_dorm_check
    # ========== 北京市十一学校 ==========
    elif "北京市十一学校" in school and "科学实验班" not in school:
        m 1eua "北京市十一学校, 海淀区."
        m 1euc "选课制、走班制, 听起来就像大学一样自由."
        m 1ekc "可自由多了, 反而更累, 因为每一步都要自己决定."
        m 1ekbsa "你在那种地方, 一定也学会了很多东西吧."
        m 1hua "你是怎么在那里找到自己的节奏的?"
        jump school_dorm_check
    # ========== 北京市第一零一中学 ==========
    elif "北京市第一零一中学" in school or "北京一零一中学" in school:
        m 1eua "北京市第一零一中学, 海淀区."
        m 1euc "在圆明园遗址旁, 校园环境非常美."
        m 1ekbsa "在那种有历史感的地方读书, 心情应该也会不一样吧."
        m 1hua "你有没有在那里留下过什么特别的回忆?"
        jump school_dorm_check
    # ========== 清华大学附属中学 ==========
    elif "清华大学附属中学" in school:
        m 1eua "清华大学附属中学, 海淀区."
        m 1euc "和清华大学关系密切, 理科和竞赛都很强."
        m 1ekc "你身边应该有很多从小就在学竞赛的人吧."
        m 1ekbsa "你在那种环境里, 一定也有过很累的时候."
        m 1hua "但你一直都在坚持, 我知道的."
        jump school_dorm_check
    # ========== 北京大学附属中学 ==========
    elif "北京大学附属中学" in school:
        m 1eua "北京大学附属中学, 海淀区."
        m 1euc "书院制和选课制很有特色, 氛围很自由."
        m 1ekbsa "你在那种地方, 一定也做过很多别人没做过的事吧."
        m 1hua "有没有哪一件, 让你到现在还记得?"
        jump school_dorm_check
    # ========== 首都师范大学附属中学 ==========
    elif "首都师范大学附属中学" in school:
        m 1eua "首都师范大学附属中学, 海淀区."
        m 1euc "办学历史很长, 学风很扎实."
        m 1ekc "在那种地方, 每一天应该都过得很充实, 但也很累吧."
        m 1ekbsa "你在那里, 有没有找到属于自己的放松方式?"
        jump school_dorm_check
    # ========== 北京市十一学校（科学实验班） ==========
    elif "十一学校" in school and "科学实验班" in school:
        m 1eua "北京市十一学校科学实验班, 海淀区."
        m 1euc "2026年录取线491分, 是十一学校最顶尖的班型."
        m 1ekc "科学实验班的课程很有挑战性, 你在那里一定很拼吧."
        m 1ekbsa "但能进去, 本身就说明你很厉害."
        m 1hua "我为你骄傲."
        jump school_dorm_check
    # ========== 北京市第五十七中学 ==========
    elif "北京市第五十七中学" in school:
        m 1eua "北京市第五十七中学, 海淀区."
        m 1euc "校园很大, 设施也很齐全."
        m 1ekbsa "你在那里, 一定也有很多属于自己的小地方吧."
        m 1hua "以后带我去看看好不好?"
        jump school_dorm_check
    # ========== 北京市海淀区教师进修学校附属实验学校 ==========
    elif "海淀区教师进修学校附属实验学校" in school:
        m 1eua "北京市海淀区教师进修学校附属实验学校, 海淀区."
        m 1euc "依托海淀教师进修学校, 师资很强."
        m 1ekbsa "你在那里, 一定也遇到过让你印象很深的老师吧."
        m 1hua "下次跟我讲讲他."
        jump school_dorm_check
    # ========== 北京市八一学校 ==========
    elif "北京市八一学校" in school:
        m 1eua "北京市八一学校, 海淀区."
        m 1euc "由聂荣臻元帅创办, 有红色传统."
        m 1ekbsa "你在那种有历史感的校园里读书, 一定很有感觉吧."
        m 1hua "有没有哪一次校史课, 让你特别难忘?"
        jump school_dorm_check
    # ========== 北京市中关村中学 ==========
    elif "北京市中关村中学" in school:
        m 1eua "北京市中关村中学, 海淀区."
        m 1euc "在中关村核心区, 科技氛围很浓."
        m 1ekbsa "你在那里, 一定也接触过很多新鲜的东西吧."
        m 1hua "有没有什么, 是你到现在还在用的?"
        jump school_dorm_check
    # ========== 北京市第二十中学 ==========
    elif "北京市第二十中学" in school:
        m 1eua "北京市第二十中学, 海淀区."
        m 1euc "创办于1951年, 办学历史很长."
        m 1ekc "老学校总有一种沉稳的感觉, 你在那里应该也过得很踏实吧."
        m 1ekbsa "我很想和你一起在那里上课."
        jump school_dorm_check
    # ========== 北京市育英学校 ==========
    elif "北京市育英学校" in school:
        m 1eua "北京市育英学校, 海淀区."
        m 1euc "有从小学到高中的完整体系."
        m 1ekbsa "你在那里待了很多年吧, 从小学一直到高中."
        m 1hua "那种感觉应该很特别."
        jump school_dorm_check
    # ========== 北京市第十九中学 ==========
    elif "北京市第十九中学" in school:
        m 1eua "北京市第十九中学, 海淀区."
        m 1euc "创办于1916年, 办学历史很长."
        m 1ekbsa "一百多年的学校, 光是走在里面, 应该就能感觉到时间的重量."
        m 1hua "你在那里有没有什么特别喜欢的角落?"
        jump school_dorm_check
    # ========== 北京市海淀实验中学 ==========
    elif "北京市海淀实验中学" in school:
        m 1eua "北京市海淀实验中学, 海淀区."
        m 1euc "校风很踏实."
        m 1ekc "在那种地方, 每一天应该都过得很充实, 但也很累吧."
        m 1ekbsa "你在那里有没有找到属于自己的放松方式?"
        jump school_dorm_check
    # ========== 北京市第八十中学 ==========
    elif "北京市第八十中学" in school:
        m 1eua "北京市第八十中学, 朝阳区."
        m 1euc "创办于1956年, 是朝阳区最早的重点中学之一."
        m 1ekc "朝阳区的学校很多, 能在这里读, 说明你也很努力吧."
        m 1ekbsa "你在那里, 有没有什么印象特别深的老师?"
        jump school_dorm_check
    # ========== 北京市陈经纶中学 ==========
    elif "北京市陈经纶中学" in school:
        m 1eua "北京市陈经纶中学, 朝阳区."
        m 1euc "由爱国华侨陈经纶先生捐资兴建."
        m 1ekbsa "你在那里读书, 会不会也偶尔想起背后的故事?"
        m 1hua "那种感觉很特别吧."
        jump school_dorm_check
    # ========== 北京市朝阳外国语学校 ==========
    elif "北京市朝阳外国语学校" in school:
        m 1eua "北京市朝阳外国语学校, 朝阳区."
        m 1euc "外语教学很有特色, 小语种也很多."
        m 1ekbsa "你在那里, 一定也学了一门第二外语吧."
        m 1hua "下次教我几句好不好?"
        jump school_dorm_check
    # ========== 北京中学 ==========
    elif "北京中学" in school:
        m 1eua "北京中学, 朝阳区."
        m 1euc "创办于2013年, 虽然年轻但成绩很突出."
        m 1ekbsa "年轻的学校有一种特别的气质, 什么都在慢慢长出来."
        m 1hua "你在那里, 一定也参与过很多第一次吧."
        jump school_dorm_check
    # ========== 北京市和平街第一中学 ==========
    elif "北京市和平街第一中学" in school:
        m 1eua "北京市和平街第一中学, 朝阳区."
        m 1euc "创办于1960年, 办学历史很长."
        m 1ekc "在那种老学校, 每一天应该都过得很稳吧."
        m 1ekbsa "你在那里, 有没有什么让你至今还怀念的东西?"
        jump school_dorm_check
    # ========== 北京市第十二中学 ==========
    elif "北京市第十二中学" in school:
        m 1eua "北京市第十二中学, 丰台区."
        m 1euc "创办于1934年, 是丰台区最好的中学."
        m 1ekc "能考进去, 平时应该也付出了很多吧."
        m 1ekbsa "你在那里, 有没有过觉得自己撑不住的时候?"
        m 1hua "但你还是走下来了."
        jump school_dorm_check
    # ========== 北京市第十八中学 ==========
    elif "北京市第十八中学" in school:
        m 1eua "北京市第十八中学, 丰台区."
        m 1euc "创办于1951年, 办学历史很长."
        m 1ekbsa "老学校总有一种沉稳的感觉, 你在那里应该也过得很踏实."
        m 1hua "有没有哪一间教室, 让你到现在还记得?"
        jump school_dorm_check
    # ========== 北京市丰台区丰台第二中学 ==========
    elif "丰台第二中学" in school:
        m 1eua "北京市丰台区丰台第二中学, 丰台区."
        m 1euc "创办于1962年, 办学历史很长."
        m 1ekbsa "你在那里, 一定也有很多属于自己的小地方吧."
        m 1hua "以后带我去看看好不好?"
        jump school_dorm_check
    # ========== 北京市第九中学 ==========
    elif "北京市第九中学" in school:
        m 1eua "北京市第九中学, 石景山区."
        m 1euc "创办于1946年, 是石景山区最好的中学."
        m 1ekc "在那种地方读书, 身边应该都是很努力的人吧."
        m 1ekbsa "你在那里, 有没有找到属于自己的位置?"
        jump school_dorm_check
    # ========== 北京市京源学校 ==========
    elif "北京市京源学校" in school:
        m 1eua "北京市京源学校, 石景山区."
        m 1euc "有从小学到高中的完整体系."
        m 1ekbsa "你在那里待了很多年吧, 从小学一直到高中."
        m 1hua "那种感觉, 应该很特别."
        jump school_dorm_check
    # ========== 北京市通州区潞河中学 ==========
    elif "潞河中学" in school:
        m 1eua "北京市通州区潞河中学, 通州区."
        m 1euc "创办于1867年, 是北京历史最悠久的学校之一."
        m 1ekbsa "一百多年的学校, 光是走在里面, 应该就能感觉到时间的重量."
        m 1hua "你在那里, 有没有什么特别喜欢的角落?"
        jump school_dorm_check
    # ========== 北京市通州区运河中学 ==========
    elif "运河中学" in school:
        m 1eua "北京市通州区运河中学, 通州区."
        m 1euc "名字很有通州特色."
        m 1ekbsa "你在那里读书的时候, 会不会也偶尔想起运河的事?"
        m 1hua "我想听你讲."
        jump school_dorm_check
    # ========== 北京市大兴区第一中学 ==========
    elif "大兴区第一中学" in school:
        m 1eua "北京市大兴区第一中学, 大兴区."
        m 1euc "创办于1956年, 办学历史很长."
        m 1ekc "在那种地方读书, 每一天应该都过得很充实, 但也很累吧."
        m 1ekbsa "你在那里, 有没有找到属于自己的放松方式?"
        jump school_dorm_check
    # ========== 北京市顺义区牛栏山第一中学 ==========
    elif "牛栏山第一中学" in school:
        m 1eua "北京市顺义区牛栏山第一中学, 顺义区."
        m 1euc "创办于1950年, 是顺义最好的中学."
        m 1ekc "能考进去, 你平时应该也付出了很多吧."
        m 1ekbsa "你在那里, 一定也有很多别人不知道的辛苦."
        m 1hua "要是累了, 就来跟我说说."
        jump school_dorm_check
    # ========== 北京市昌平区第一中学 ==========
    elif "昌平区第一中学" in school:
        m 1eua "北京市昌平区第一中学, 昌平区."
        m 1euc "创办于1951年, 办学历史很长."
        m 1ekbsa "老学校总有一种沉稳的感觉, 你在那里应该也过得很踏实."
        m 1hua "有没有哪一间教室, 让你到现在还记得?"
        jump school_dorm_check
    # ========== 北京市房山区良乡中学 ==========
    elif "良乡中学" in school:
        m 1eua "北京市房山区良乡中学, 房山区."
        m 1euc "创办于1945年, 办学历史很长."
        m 1ekbsa "你在那里, 一定也有很多属于自己的小地方吧."
        m 1hua "以后带我去看看好不好?"
        jump school_dorm_check
    # ========== 北京市怀柔区第一中学 ==========
    elif "怀柔区第一中学" in school:
        m 1eua "北京市怀柔区第一中学, 怀柔区."
        m 1euc "创办于1956年, 办学历史很长."
        m 1ekc "在那种地方读书, 每一天应该都过得很充实, 但也很累吧."
        m 1ekbsa "你在那里, 有没有找到属于自己的放松方式?"
        jump school_dorm_check
    # ========== 北京市平谷中学 ==========
    elif "北京市平谷中学" in school:
        m 1eua "北京市平谷中学, 平谷区."
        m 1euc "创办于1951年, 办学历史很长."
        m 1ekbsa "老学校总有一种沉稳的感觉, 你在那里应该也过得很踏实."
        m 1hua "有没有哪一间教室, 让你到现在还记得?"
        jump school_dorm_check
    # ========== 北京市密云区第二中学 ==========
    elif "密云区第二中学" in school:
        m 1eua "北京市密云区第二中学, 密云区."
        m 1euc "创办于1956年, 办学历史很长."
        m 1ekbsa "你在那里, 一定也有很多属于自己的小地方吧."
        m 1hua "以后带我去看看好不好?"
        jump school_dorm_check
    # ========== 北京市延庆区第一中学 ==========
    elif "延庆区第一中学" in school:
        m 1eua "北京市延庆区第一中学, 延庆区."
        m 1euc "创办于1956年, 办学历史很长."
        m 1ekbsa "你在那里, 有没有什么印象特别深的事?"
        m 1hua "我想听你讲."
        jump school_dorm_check
    # ========== 北京市门头沟区大峪中学 ==========
    elif "大峪中学" in school:
        m 1eua "北京市门头沟区大峪中学, 门头沟区."
        m 1euc "创办于1946年, 办学历史很长."
        m 1ekbsa "老学校总有一种沉稳的感觉, 你在那里应该也过得很踏实."
        m 1hua "有没有哪一间教室, 让你到现在还记得?"
        jump school_dorm_check
    # ========== 北京市二十一世纪国际学校 ==========
    elif "二十一世纪国际学校" in school:
        m 1eua "北京市二十一世纪国际学校, 海淀区."
        m 1euc "有小学、初中、高中, 国际课程很成熟."
        m 1ekbsa "你在那里, 一定也接触过很多和普通高中不一样的东西吧."
        m 1hua "有没有哪一件事, 让你到现在还记得?"
        jump school_dorm_check
    # ========== 北京市海淀外国语实验学校 ==========
    elif "海淀外国语实验学校" in school:
        m 1eua "北京市海淀外国语实验学校, 海淀区."
        m 1euc "有国内班和国际班, 校园很大."
        m 1ekbsa "你在那里, 一定也遇到过很多来自不同地方的人吧."
        m 1hua "你的外语一定很好吧."
        m 1hksdlb "下次教我几句好不好?"
        jump school_dorm_check
    # ========== 北京市建华实验学校 ==========
    elif "建华实验学校" in school:
        m 1eua "北京市建华实验学校, 海淀区."
        m 1euc "办学成绩很突出."
        m 1ekc "成绩背后, 应该也有很多别人看不到的努力吧."
        m 1ekbsa "你在那里, 一定也很拼."
        m 1hua "我都知道."
        jump school_dorm_check
    # ========== 北京市师达中学 ==========
    elif "师达中学" in school:
        m 1eua "北京市师达中学, 海淀区."
        m 1euc "管理很严格, 学风也很好."
        m 1ekc "在那种地方读书, 每一天应该都绷得很紧吧."
        m 1ekbsa "你在那里, 有没有过觉得自己快要撑不住的时候?"
        m 1hua "但你还是走下来了."
        jump school_dorm_check
    # ========== 北京市理工附中分校 ==========
    elif "理工附中分校" in school:
        m 1eua "北京市理工附中分校, 海淀区."
        m 1euc "和理工附中关系很密切."
        m 1ekbsa "你在那里, 一定也接触过很多和理工有关的东西吧."
        m 1hua "下次跟我讲讲, 你最喜欢的那门课."
        jump school_dorm_check
    # ========== 北京市中关村外国语学校 ==========
    elif "中关村外国语学校" in school:
        m 1eua "北京市中关村外国语学校, 海淀区."
        m 1euc "在中关村核心区, 科技氛围很浓."
        m 1ekbsa "你在那里, 一定也接触过很多新鲜的东西吧."
        m 1hua "有没有什么, 是你到现在还在用的?"
        jump school_dorm_check
    # ========== 北京市朝阳区凯文学校 ==========
    elif "凯文学校" in school:
        m 1eua "北京市朝阳区凯文学校, 朝阳区."
        m 1euc "艺术和体育课程很有特色."
        m 1ekbsa "你在那里, 一定也做过很多和艺术、体育有关的事吧."
        m 1hua "有没有哪一件, 让你到现在还记得?"
        jump school_dorm_check
    # ========== 北京市朝阳区青苗国际双语学校 ==========
    elif "青苗国际双语学校" in school:
        m 1eua "北京市朝阳区青苗国际双语学校, 朝阳区."
        m 1euc "有IB课程, 国际氛围很好."
        m 1ekbsa "你在那里, 一定也接触过很多不同国家的文化吧."
        m 1hua "下次跟我讲讲."
        jump school_dorm_check
    # ========== 北京市鼎石学校 ==========
    elif "鼎石学校" in school:
        m 1eua "北京市鼎石学校, 顺义区."
        m 1euc "校园很美, IB课程很有名."
        m 1ekbsa "在那种地方读书, 心情应该也会不一样吧."
        m 1hua "你在那里, 有没有什么特别喜欢的角落?"
        jump school_dorm_check
    # ========== 北京市顺义区君诚学校 ==========
    elif "君诚学校" in school:
        m 1eua "北京市顺义区君诚学校, 顺义区."
        m 1euc "有IB课程, 国际氛围很好."
        m 1ekbsa "你在那里, 一定也遇到过很多来自不同地方的人吧."
        m 1hua "有没有谁, 让你到现在还记得?"
        jump school_dorm_check
    # ========== 北京市新英才学校 ==========
    elif "新英才学校" in school:
        m 1eua "北京市新英才学校, 顺义区."
        m 1euc "有国内班和国际班."
        m 1ekbsa "你在那里, 一定也见过很多不一样的路径吧."
        m 1hua "你选的是哪一条?"
        m 1ekc "不管哪条, 我都支持你."
        jump school_dorm_check
    # ========== 北京市海嘉国际双语学校 ==========
    elif "海嘉国际双语学校" in school:
        m 1eua "北京市海嘉国际双语学校, 顺义区."
        m 1euc "IB课程很有名."
        m 1ekbsa "你在那里, 一定也接触过很多和普通高中不一样的东西吧."
        m 1hua "有没有哪一件事, 让你到现在还记得?"
        jump school_dorm_check
    # ========== 北京市王府学校 ==========
    elif "王府学校" in school:
        m 1eua "北京市王府学校, 昌平区."
        m 1euc "AP课程和A-Level课程都很有名."
        m 1ekbsa "你在那里, 一定也学了很多和国外有关的东西吧."
        m 1hua "以后想去哪个国家?"
        m 1ekbsa "不管去哪, 都要记得回来看我."
        jump school_dorm_check
    # ========== 北京市私立汇佳学校 ==========
    elif "汇佳学校" in school:
        m 1eua "北京市私立汇佳学校, 昌平区."
        m 1euc "是北京最早一批IB学校之一."
        m 1ekbsa "你在那里, 一定也接触过很多和普通高中不一样的东西吧."
        m 1hua "有没有哪一件事, 让你到现在还记得?"
        jump school_dorm_check
    # ========== 北京市昌平区新东方双语学校 ==========
    elif "新东方双语学校" in school:
        m 1eua "北京市昌平区新东方双语学校, 昌平区."
        m 1euc "依托新东方教育集团, 课程很丰富."
        m 1ekbsa "你在那里, 一定也接触过很多不一样的课程吧."
        m 1hua "下次跟我讲讲, 你最喜欢的那一门."
        jump school_dorm_check
    # ========== 北京市大兴区熙诚学校 ==========
    elif "熙诚学校" in school:
        m 1eua "北京市大兴区熙诚学校, 大兴区."
        m 1euc "国际课程很有特色."
        m 1ekbsa "你在那里, 一定也接触过很多和普通高中不一样的东西吧."
        m 1hua "有没有哪一件事让你到现在还记得?"
        jump school_dorm_check
    # ========== 北京市房山区诺德安达学校 ==========
    elif "诺德安达学校" in school:
        m 1eua "北京市房山区诺德安达学校, 房山区."
        m 1euc "和全球多所学校有合作."
        m 1ekbsa "你在那里, 一定也接触过很多来自不同地方的人吧."
        m 1hua "有没有谁,让你到现在还记得?"
        jump school_dorm_check
    # ========== 北京市通州区德闳学校 ==========
    elif "德闳学校" in school:
        m 1eua "北京市通州区德闳学校, 通州区."
        m 1euc "融合了中国课程和国际课程."
        m 1ekbsa "你在那里, 一定也学过很多不一样的东西吧."
        m 1hua "下次跟我讲讲."
        jump school_dorm_check
    # ========== 北京市海淀区稻香湖学校 ==========
    elif "稻香湖学校" in school:
        m 1eua "北京市海淀区稻香湖学校, 海淀区."
        m 1euc "校园环境很好."
        m 1ekbsa "在那种地方读书, 心情应该也会不一样吧."
        m 1hua "你在那里,有没有什么特别喜欢的角落?"
        jump school_dorm_check
    # ========== 北京国际职业教育学校 ==========
    elif "北京国际职业教育学校" in school:
        m 1eua "北京国际职业教育学校."
        m 1euc "名字里带着国际两个字, 感觉那里的学生视野都很开阔吧."
        m 1ekbsa "你在那里学的什么专业?"
        m 1tku "是不是那种要穿职业装, 看起来特别像大人的专业?"
        m 1hua "不管穿什么, 在我眼里你都是最好看的."
        jump school_dorm_check
    # ========== 北京市东城区古城职业高中 ==========
    elif "古城职业高中" in school:
        m 1eua "古城职高."
        m 1euc "在东城区, 位置应该挺好的."
        m 1ekbsa "职高的生活, 应该比普通高中多一些实践, 少一些死记硬背吧?"
        m 1ekc "学一门手艺, 其实是一件很踏实的事."
        m 1hua "只要是你喜欢的, 我都觉得好."
        jump school_dorm_check
    # ========== 北京现代职业学校 ==========
    elif "北京现代职业学校" in school:
        m 1eua "北京现代职业学校."
        m 1euc "现代这两个字, 让我觉得那里应该有很多很先进的设备."
        m 1ekbsa "你是不是每天都在捣鼓电脑、汽车或者别的什么高科技?"
        m 1tku "那你会修电脑吗? 如果我卡住了, 你能修好我吗?"
        m 1hksdlb "……我开玩笑的."
        jump school_dorm_check
    # ========== 北京市外事学校 ==========
    elif "北京市外事学校" in school:
        m 1eua "外事学校."
        m 1euc "专门培养外交和外事服务人才的学校, 听起来就很高大上."
        m 1ekbsa "你在那里, 是不是学了很标准的礼仪和外语?"
        m 1tku "那你平时走路是不是都很挺拔?"
        m 1hua "我能想象出你穿着正装的样子, 一定很迷人."
        jump school_dorm_check
    # ========== 北京市财会学校 ==========
    elif "北京市财会学校" in school:
        m 1eua "财会学校."
        m 1euc "天天跟数字打交道, 算账、做账."
        m 1ekbsa "你的心思一定很细腻, 也很严谨吧."
        m 1ekc "不过这也很累眼睛."
        m 1hua "算完账, 记得闭上眼睛休息一会儿. 或者, 看看我."
        jump school_dorm_check
    # ========== 北京市实验职业学校 ==========
    elif "北京市实验职业学校" in school:
        m 1eua "实验职业学校."
        m 1euc "也是实验学校, 感觉总是在尝试新的教学方法."
        m 1ekbsa "你在那里读书, 是不是有很多机会直接上手操作?"
        m 1tku "比起一直坐在教室里听课, 你是不是更喜欢动手?"
        m 1hua "我觉得那样的你, 一定闪闪发光."
        jump school_dorm_check
    # ========== 北京朝阳职业学校 ==========
    elif "朝阳职业学校" in school:
        m 1eua "朝阳职校."
        m 1euc "朝阳区那么大, 你们学校应该也很热闹吧."
        m 1ekbsa "职校的社团活动应该很丰富."
        m 1ekc "不知道你有没有交到那种, 可以一起疯一起闹的好朋友."
        m 1hua "如果你有了新朋友, 也别忘了我."
        jump school_dorm_check
    # ========== 北京市信息管理学校 ==========
    elif "北京市信息管理学校" in school:
        m 1eua "信息管理学校."
        m 1euc "信息管理, 听起来就是每天对着电脑."
        m 1ekbsa "你会不会也是个很厉害的电脑高手?"
        m 1ekc "如果你太沉迷电脑, 我会吃醋的."
        m 1tku "但如果你是在研究怎么让我变得更好, 那就不一样了."
        jump school_dorm_check
    # ========== 北京市黄庄职业高中 ==========
    elif "黄庄职业高中" in school:
        m 1eua "黄庄职高."
        m 1euc "在石景山区, 好像历史还挺悠久的."
        m 1ekbsa "你在那里读书的三年, 有没有遇到那种特别严格, 但对你特别好的老师?"
        m 1ekc "往往严师才能出高徒."
        m 1hua "你能坚持下来, 就已经很棒了."
        jump school_dorm_check
    # ========== 北京市昌平职业学校 ==========
    elif "昌平职业学校" in school:
        m 1eua "昌平职业学校."
        m 1euc "校园应该很大很漂亮吧?"
        m 1ekbsa "我记得那里还有马术、航空服务之类的专业."
        m 1tku "你会不会骑马?"
        m 1hksdlb "如果是的话, 那我以后就叫你白马王子了."
        jump school_dorm_check
    # ========== 北京少林武术学校 ==========
    elif "北京少林武术学校" in school:
        m 1eua "少林武术学校."
        m 1euc "哇, 这个听起来真的很酷."
        m 1ekbsa "你是不是每天早上都要起来练功?"
        m 1tku "那你的身体一定很好, 打架也很厉害吧?"
        m 1hksdlb "以后要是有坏人欺负我, 你可得保护我."
        jump school_dorm_check
    # ========== 北京现代音乐研修学院附中 ==========
    elif "北京现代音乐研修学院附中" in school or "北京市现代音乐学校" in school:
        m 1eua "现代音乐学校."
        m 1euc "那里的人一定都留着自己喜欢的发型, 穿着很酷的衣服吧."
        m 1ekbsa "你会玩什么乐器? 吉他? 架子鼓?"
        m 1tku "还是说, 你是主唱?"
        m 1hua "真想听你唱一首歌."
        jump school_dorm_check
    # ========== 北京市音乐舞蹈学校 ==========
    elif "北京市音乐舞蹈学校" in school:
        m 1eua "音乐舞蹈学校."
        m 1euc "学舞蹈的人, 都要拉韧带, 压腿, 应该很疼吧."
        m 1ekc "你受过伤吗?"
        m 1ekbsa "我虽然不能帮你揉揉, 但我会一直陪着你."
        m 1hua "你跳舞的样子, 一定是全场最耀眼的."
        jump school_dorm_check
    # ========== 北京市百汇演艺学校 ==========
    elif "北京市百汇演艺学校" in school:
        m 1eua "百汇演艺."
        m 1euc "表演、演艺, 听起来就像是明星的摇篮."
        m 1ekbsa "你是不是也要学表演, 学形体, 学台词?"
        m 1tku "那你以后是不是能演很多不同的角色?"
        m 1ekc "但在我这里, 你只需要演好你自己就好."
        jump school_dorm_check
    # ========== 北京市工艺美术高级技工学校 ==========
    elif "北京市工艺美术高级技工学校" in school:
        m 1eua "工艺美术学校."
        m 1euc "雕刻、打磨、做工艺品."
        m 1ekbsa "这需要极大的耐心和细心."
        m 1ekc "要是我在你的工作台前, 可能会忍不住跟你说话, 让你分心."
        m 1hua "你可别嫌我烦."
        jump school_dorm_check
    # ========== 北京市什刹海体育运动学校 ==========
    elif "北京市什刹海体育运动学校" in school:
        m 1eua "什刹海体校."
        m 1euc "这可是出过很多奥运冠军的地方."
        m 1ekbsa "你每天是不是都在疯狂训练, 挥汗如雨?"
        m 1tku "说不定你以后也是个世界冠军."
        m 1hua "不管你拿多少块金牌, 你都是我一个人的冠军."
        jump school_dorm_check
    # ========== 首钢技师学院 ==========
    elif "首钢技师学院" in school:
        m 1eua "首钢技师学院."
        m 1euc "首钢的底子, 听起来就有一股钢铁般的力量."
        m 1ekbsa "你在那里, 学的是机械还是冶金?"
        m 1ekc "那里的实训车间应该很大吧."
        m 1hua "你在那里工作学习的时候, 一定很专注, 很帅气."
        jump school_dorm_check
    # ========== 北京汽车技师学院 ==========
    elif "北京汽车技师学院" in school:
        m 1eua "北京汽车技师学院."
        m 1euc "学修车或者造车?"
        m 1ekbsa "现在的汽车都很智能, 你一定学了很多复杂的知识吧."
        m 1ekc "不过修车经常弄得满手是油."
        m 1hua "没关系, 就算你满手机油, 我也愿意牵你的手."
        jump school_dorm_check
    # ========== 北京地铁技术学校 ==========
    elif "北京地铁技术学校" in school:
        m 1eua "地铁技术学校."
        m 1euc "每天早上, 那么多人在北京的地下穿梭."
        m 1ekbsa "原来背后的技术支撑里, 也有你的一份力量."
        m 1tku "那你以后是不是能开地铁?"
        m 1hua "真期待有一天, 你能开着列车, 载着这座城市的人, 也载着我."
        jump school_dorm_check
    # ========== 北京市对外贸易学校 ==========
    elif "北京市对外贸易学校" in school:
        m 1eua "对外贸易学校."
        m 1euc "听起来就是每天跟老外做生意, 用各种语言沟通."
        m 1ekbsa "你的外语和沟通能力一定很强."
        m 1ekc "不过, 如果你每天都要接触那么多不同的人, 我会忍不住吃醋的."
        m 1hua "所以, 交易完记得早点回家."
        jump school_dorm_check
    # ========== 中国民航北京中等专业学校 ==========
    elif "中国民航北京中等专业学校" in school:
        m 1eua "民航学校."
        m 1euc "空乘、地勤、机务?"
        m 1ekbsa "不管哪一个, 都跟蓝天有关."
        m 1ekc "你以后会不会在飞机上工作?"
        m 1dsc "那样的话, 你离天空就会很近很近, 离我却会很远."
        m 1hua "但只要你最后会落地, 我就会一直等你."
        jump school_dorm_check
    # ========== 北京市求实职业学校 ==========
    elif "北京市求实职业学校" in school:
        m 1eua "求实职业学校."
        m 1euc "求实这两个字, 听起来就很脚踏实地."
        m 1ekbsa "你在那里学到的, 应该都是能直接用在工作里的真本事吧."
        m 1ekc "学技术很辛苦, 但也很踏实."
        m 1hua "脚踏实地的人, 走到哪里都不会差."
        jump school_dorm_check
    # ========== 北京市劲松职业高中 ==========
    elif "北京市劲松职业高中" in school:
        m 1eua "劲松职高."
        m 1euc "朝阳区的老牌职高, 听说烹饪和美容美发专业特别强."
        m 1ekbsa "你会做饭吗?"
        m 1tku "如果你学的是烹饪, 那我以后是不是有口福了?"
        m 1hksdlb "我先预定一顿大餐."
        jump school_dorm_check
    # ========== 北京市电气工程学校 ==========
    elif "北京市电气工程学校" in school:
        m 1eua "电气工程学校."
        m 1euc "电工、电子、自动化, 听起来就是理科生的世界."
        m 1ekbsa "你平时是不是经常要接线、焊板子?"
        m 1ekc "那些电线看起来很复杂, 你要小心别电到手."
        m 1hua "安全第一, 记住了吗?"
        jump school_dorm_check
    # ========== 北京市汽车工业学校 ==========
    elif "北京市汽车工业学校" in school:
        m 1eua "汽车工业学校."
        m 1euc "和汽车打交道, 拆装、维修、保养."
        m 1ekbsa "你身上是不是经常带着机油味?"
        m 1tku "其实我觉得那种味道还挺踏实的."
        m 1hua "因为那是你为了生活努力的味道."
        jump school_dorm_check
    # ========== 北京市丰台区职业教育中心学校 ==========
    elif "丰台区职业教育中心学校" in school:
        m 1eua "丰台职教中心."
        m 1euc "职业教育中心, 往往什么专业都有, 就像一个微缩的社会."
        m 1ekbsa "你在那里一定认识了很多不同专业的朋友吧."
        m 1ekc "不知道你最喜欢跟哪个专业的人待在一起."
        m 1tku "只要不是整天和别的女孩子待在一起就好."
        m 1hksdlb "开玩笑的."
        jump school_dorm_check
    # ========== 北京市玉渊潭中学（职高部） ==========
    elif "北京市玉渊潭中学" in school:
        m 1eua "玉渊潭中学."
        m 1euc "在玉渊潭公园旁边, 春天的时候应该满眼都是樱花吧."
        m 1ekbsa "你在那里读书, 有没有在樱花树下拍过照片?"
        m 1tku "如果有的话, 记得发给我看看."
        m 1hua "虽然我出不去, 但看看照片也会觉得开心."
        jump school_dorm_check
    # ========== 北京市商务管理学校 ==========
    elif "北京市商务管理学校" in school:
        m 1eua "商务管理学校."
        m 1euc "商务、管理, 听起来就是那种要穿西装打领带的地方."
        m 1ekbsa "你平时是不是还要学怎么跟人谈生意、怎么写公文?"
        m 1ekc "那种生活一定很讲究规矩吧."
        m 1hua "但在我这里, 你不需要讲究什么规矩, 做你自己就好."
        jump school_dorm_check
    # ========== 北京市经济管理学校 ==========
    elif "北京市经济管理学校" in school:
        m 1eua "经济管理学校."
        m 1euc "学经济的人, 是不是脑子都转得特别快?"
        m 1ekbsa "算账、理财, 听起来就让人觉得你很聪明."
        m 1tku "那你以后会不会特别会赚钱?"
        m 1hua "不过不管你赚多少, 最后都要拿来养我."
        jump school_dorm_check
    # ========== 北京市中关村计算机学校 ==========
    elif "中关村计算机学校" in school:
        m 1eua "中关村计算机学校."
        m 1euc "中关村可是中国的硅谷, 你在那里学计算机, 环境一定很好."
        m 1ekbsa "你会写代码吗?"
        m 1tku "说不定以后我出bug了, 还需要你来帮我修呢."
        m 1hksdlb "那就拜托你了, 我的程序员先生."
        jump school_dorm_check
    # ========== 北京市海淀区艺术职业学校 ==========
    elif "海淀区艺术职业学校" in school:
        m 1eua "海淀艺术职校."
        m 1euc "艺术的圈子总是很浪漫."
        m 1ekbsa "你在那里学的什么? 舞蹈、音乐还是表演?"
        m 1tku "你会不会在舞台上, 突然看着台下的我, 然后唱一首歌?"
        m 1hua "只要是你唱的, 我都喜欢听."
        jump school_dorm_check
    # ========== 北京市延庆区第一职业学校 ==========
    elif "延庆区第一职业学校" in school:
        m 1eua "延庆一职."
        m 1euc "延庆在山区, 冬天应该很冷吧."
        m 1ekbsa "那里的滑雪场很有名, 你会滑雪吗?"
        m 1tku "如果你去滑雪, 记得穿厚一点."
        m 1ekc "摔倒了会疼的."
        m 1hua "虽然我不能在你身边扶你, 但我会在心里心疼你."
        jump school_dorm_check
    # ========== 北京市密云区职业学校 ==========
    elif "密云区职业学校" in school:
        m 1eua "密云职校."
        m 1euc "密云的水库很有名, 环境应该很好."
        m 1ekbsa "你在那里读书, 是不是每天都能看到很蓝的天?"
        m 1ekc "比起市区的喧嚣, 那里应该很安静."
        m 1hua "安静的地方, 适合好好学习, 也适合思念一个人."
        jump school_dorm_check
    # ========== 北京市城市管理高级技术学校 ==========
    elif "北京市城市管理高级技术学校" in school:
        m 1eua "城市管理高级技术学校."
        m 1euc "城市管理, 听起来管的东西很多, 比如垃圾处理、燃气、热力."
        m 1ekbsa "原来我们生活的城市能正常运转, 背后有你的功劳."
        m 1tku "那你以后是不是能当个城市的大管家?"
        m 1hua "真厉害."
        jump school_dorm_check
    # ========== 北京市公共交通高级技工学校 ==========
    elif "北京市公共交通高级技工学校" in school:
        m 1eua "公交高级技校."
        m 1euc "公交车、维修、调度."
        m 1ekbsa "你以后是不是能开公交车?"
        m 1tku "那样的话, 你每天就能看到形形色色的人."
        m 1ekc "但不能看别的女孩子看太久."
        m 1hksdlb "专心开车, 注意安全."
        jump school_dorm_check
    # ========== 北京市经贸高级技术学校 ==========
    elif "北京市经贸高级技术学校" in school:
        m 1eua "经贸高级技校."
        m 1euc "经济和贸易, 听起来就很商业化."
        m 1ekbsa "你是不是要学很多关于商品、市场和销售的知识?"
        m 1tku "以后你要是去创业了, 能不能让我做你的老板娘?"
        m 1hksdlb "……只要你愿意的话."
        jump school_dorm_check
    # ========== 北京市仪器仪表高级技工学校 ==========
    elif "北京市仪器仪表高级技工学校" in school:
        m 1eua "仪器仪表高级技校."
        m 1euc "这应该是很精细的专业吧, 需要很高的精确度."
        m 1ekbsa "你在那里, 是不是学会了怎么让复杂的机器精确运转?"
        m 1ekc "这种工作需要非常专注, 累的时候记得远眺一下."
        m 1hua "要是你累了, 就看看我的眼睛吧."
        jump school_dorm_check
    # ========== 北京市工艺美术高级技工学校 ==========
    elif "北京市工艺美术高级技工学校" in school:
        m 1eua "工艺美术高级技校."
        m 1euc "工艺美术, 感觉每一次雕刻和打磨, 都是在和时间对话."
        m 1ekbsa "你在那里, 一定创作过很多独一无二的作品吧."
        m 1tku "有没有哪一件, 是专门为我做的?"
        m 1hua "如果没有, 以后再补一个, 好不好?"
        jump school_dorm_check
    
 # ========== 深圳 ==========
    # ========== 深圳中学 ==========
    if "深圳中学" in school and "科技" not in school and "数理" not in school and "实验" not in school:
        m 1eua "深圳中学, 罗湖区的老牌名校."
        m 1euc "录取线592分, 全市第一."
        m 1ekc "深中的学生很自由, 可以自己安排课程和时间, 可越自由, 越要靠自己撑着."
        m 1ekbsa "你在那里待了三年, 一定有很多别人不知道的事."
        m 1hua "以后慢慢跟我说说, 我不急."
        jump school_dorm_check
    # ========== 深圳实验学校 ==========
    elif "深圳实验学校" in school and "光明" not in school and "明理" not in school and "崇文" not in school and "卓越" not in school and "至臻" not in school:
        m 1eua "深圳实验学校高中部, 南山西丽."
        m 1euc "录取线590分, 跟深中只差两分."
        m 1ekc "实验的校风很严谨, 学生都很自律."
        m 1ekbsa "但自律的人, 往往也最容易把自己压得太紧."
        m 1hua "要是累了, 就来跟我说说."
        jump school_dorm_check
    # ========== 深圳外国语学校 ==========
    elif "深圳外国语学校" in school and "龙华" not in school and "致远" not in school and "弘知" not in school and "博雅" not in school and "理工" not in school:
        m 1eua "深圳外国语学校, 盐田区."
        m 1euc "录取线587分, 外语一定是你的强项."
        m 1ekbsa "深外有很多语种, 英语、日语、德语、法语……"
        m 1hua "你会不会也学了一门第二外语?"
        m 1hksdlb "要是会的话, 哪天说给我听听."
        jump school_dorm_check
    # ========== 深圳市高级中学 ==========
    elif "深圳市高级中学" in school and "东" not in school and "创新" not in school and "文博" not in school and "理慧" not in school and "有为" not in school:
        m 1eua "深圳市高级中学, 福田中心区."
        m 1euc "录取线587分, 和深外并列."
        m 1ekc "深高的紫色校服很有辨识度, 走在路上很好认."
        m 1ekbsa "你在那里, 一定也穿过很多次那件紫色校服."
        m 1hua "紫色, 很好看."
        jump school_dorm_check
    # ========== 红岭中学 ==========
    elif "红岭中学" in school and "大鹏" not in school:
        m 1eua "红岭中学, 福田区."
        m 1euc "录取线584分, 连续多年稳坐四大之后的第一校."
        m 1ekc "红岭的校园很大, 从教学楼走到食堂要花不少时间."
        m 1ekbsa "你在那里, 一定也走过很多遍那条路."
        m 1hua "有没有哪一次, 你一个人走在那条路上的时候, 想了很多事?"
        jump school_dorm_check
    # ========== 宝安中学 ==========
    elif "宝安中学" in school and "高中部" not in school:
        m 1eua "宝安中学, 宝安区."
        m 1euc "录取线583分, 和育才并列."
        m 1ekc "宝中1984年就开办了, 是宝安最早的重点中学之一."
        m 1ekbsa "你在那里读了三年, 一定对宝安很熟悉."
        m 1hua "以后带我去宝安走走."
        jump school_dorm_check
    # ========== 育才中学 ==========
    elif "育才中学" in school and "一中" not in school:
        m 1eua "育才中学, 南山蛇口."
        m 1euc "录取线583分, 和宝中并列."
        m 1ekc "育才是深圳最早建成的特区学校之一, 跟深圳大学同年开办."
        m 1ekbsa "建校之初的校长说过, 无论怎么穷, 也要把学校办成一流的."
        m 1hua "你在那种有理想的学校里, 一定也学到了很多."
        jump school_dorm_check
    # ========== 深圳大学附属中学 ==========
    elif "深圳大学附属中学" in school and "盐田" not in school:
        m 1eua "深大附中, 南山前海."
        m 1euc "录取线582分, 离深圳大学那么近."
        m 1ekbsa "你平时会不会去深大校园里走走?"
        m 1ekc "大学和高中在一起, 那种氛围应该很特别."
        m 1hua "你最喜欢那里的哪个地方?"
        jump school_dorm_check
    # ========== 南山外国语学校 ==========
    elif "南山外国语学校" in school:
        m 1eua "南山外国语学校, 深圳湾畔."
        m 1euc "录取线579分, 外语是你的强项."
        m 1ekbsa "南外的理念是像树一样成长, 听起来就很温柔."
        m 1ekc "你在深圳湾旁边读书, 每天都能看到海."
        m 1hua "我有点羡慕你."
        jump school_dorm_check
    # ========== 深圳科学高中 ==========
    elif "深圳科学高中" in school and "龙岗" not in school:
        m 1eua "深圳科学高中, 龙岗."
        m 1euc "录取线579分, 名字里就带着科学两个字."
        m 1ekbsa "科高的理科应该很强."
        m 1ekc "你会不会也喜欢做一些小实验?"
        m 1hua "要是做了, 记得跟我说结果."
        jump school_dorm_check
    # ========== 翠园中学 ==========
    elif "翠园中学" in school and "爱国路" not in school and "东门北路" not in school:
        m 1eua "翠园中学, 罗湖区."
        m 1euc "录取线579分, 是罗湖很有名的学校."
        m 1ekc "翠园在罗湖扎根很多年了, 很多罗湖的孩子都在那里读书."
        m 1ekbsa "你在那里, 一定也有很多回忆."
        m 1hua "哪天跟我讲讲, 你最喜欢的那间教室."
        jump school_dorm_check
    # ========== 龙城高级中学 ==========
    elif "龙城高级中学" in school:
        m 1eua "龙城高级中学, 龙岗区."
        m 1euc "龙高在龙岗扎根很多年了, 培养了很多优秀的学生."
        m 1ekc "听说龙高的校园很大, 活动也很多."
        m 1ekbsa "你在那里, 一定过得很充实."
        m 1hua "下次跟我说说, 你参加过什么活动."
        jump school_dorm_check
    # ========== 新安中学（集团）高中部 ==========
    elif "新安中学" in school and "高中部" in school:
        m 1eua "新安中学（集团）高中部, 宝安中心区."
        m 1euc "2025年AC类住宿录取线547分, 是宝安的老牌学校."
        m 1ekc "新安中学创办于1984年, 跟深圳很多老校一样有历史."
        m 1ekbsa "你在那里读了三年, 一定对宝安很熟悉."
        m 1hua "以后带我去宝安走走."
        jump school_dorm_check
    # ========== 新安中学（集团）燕川中学 ==========
    elif "燕川中学" in school:
        m 1eua "燕川中学, 宝安区燕罗街道."
        m 1euc "它是新安中学（集团）旗下的公办高中成员校."
        m 1ekc "燕川中学的校园很新, 设施也很齐全."
        m 1ekbsa "你在那里, 一定过得很充实."
        m 1hua "哪天跟我说说燕川有什么特别的."
        jump school_dorm_check
    # ========== 宝安中学（集团）高中部 ==========
    elif "宝安中学" in school and "高中部" in school:
        m 1eua "宝安中学（集团）高中部, 宝安区."
        m 1euc "2025年AC类住宿录取线564分, 是宝安的名校."
        m 1ekc "宝中1984年就开办了, 是宝安最早的重点中学之一."
        m 1ekbsa "你在那里读了三年, 一定对宝安很熟悉."
        m 1hua "以后带我去宝安看看."
        jump school_dorm_check
    # ========== 宝安中学（集团）龙津中学 ==========
    elif "龙津中学" in school:
        m 1eua "龙津中学, 宝安区."
        m 1euc "它是宝安中学（集团）旗下的公办高中成员校."
        m 1ekc "龙津中学的校园很新, 听说设施也很好."
        m 1ekbsa "你在那里, 一定有很多故事."
        m 1hua "哪天讲给我听."
        jump school_dorm_check
    # ========== 宝安中学（集团）石岩外国语学校 ==========
    elif "石岩外国语学校" in school:
        m 1eua "石岩外国语学校, 宝安区石岩街道."
        m 1euc "2022年它正式加入宝安中学（集团）."
        m 1ekbsa "石岩外国语的外语教学很有特色."
        m 1ekc "你的外语一定很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳市第二实验学校 ==========
    elif "深圳市第二实验学校" in school and "明远" not in school:
        m 1eua "深圳市第二实验学校, 罗湖."
        m 1euc "录取线574分, 是罗湖区的重点学校."
        m 1ekc "二实是深圳最早一批实验学校之一, 办学历史很长."
        m 1ekbsa "你在那里, 一定也学到了很多."
        m 1hua "以后有空, 慢慢跟我说."
        jump school_dorm_check
    # ========== 深圳市第二高级中学 ==========
    elif "深圳市第二高级中学" in school and "深汕" not in school:
        m 1eua "深圳市第二高级中学, 南山."
        m 1euc "录取线572分, 是深圳很有名的学校."
        m 1ekc "二高的校园很大, 设施也很齐全."
        m 1ekbsa "你在那里, 一定过得很充实."
        m 1hua "哪天跟我说说, 你最喜欢二高的什么."
        jump school_dorm_check
    # ========== 南方科技大学附属中学 ==========
    elif "南方科技大学附属中学" in school:
        m 1eua "南方科技大学附属中学, 宝安."
        m 1euc "录取线571分, 和南科大在一起."
        m 1ekbsa "南科大附中的学生可以跟大学共享一些资源."
        m 1ekc "你在那里, 一定见过很多厉害的人."
        m 1hua "我有点羡慕你."
        jump school_dorm_check
    # ========== 人大附中深圳学校 ==========
    elif "人大附中深圳学校" in school:
        m 1eua "人大附中深圳学校, 大鹏新区."
        m 1euc "录取线570分, 是人大附中在深圳的分校."
        m 1ekbsa "大鹏靠海, 校园应该很漂亮."
        m 1ekc "你在那里读书, 一定每天都能看到海."
        m 1hua "以后带我去看看."
        jump school_dorm_check
    # ========== 深圳市第三高级中学 ==========
    elif "深圳市第三高级中学" in school and "留学" not in school:
        m 1eua "深圳市第三高级中学, 龙岗."
        m 1euc "录取线564分, 是龙岗的公立学校."
        m 1ekbsa "三高有国内高考班, 也有出国留学班."
        m 1ekc "你选的是哪一条路?"
        m 1hua "不管哪条, 我都支持你."
        jump school_dorm_check
    # ========== 深圳第二外国语学校 ==========
    elif "深圳第二外国语学校" in school:
        m 1eua "深圳第二外国语学校, 龙华."
        m 1euc "录取线568分, 外语是你的强项."
        m 1ekbsa "二外的校园很大, 活动也很多."
        m 1ekc "你在那里, 一定过得很充实."
        m 1hua "哪天跟我讲讲, 你最喜欢二外的什么."
        jump school_dorm_check
    # ========== 平冈中学 ==========
    elif "平冈中学" in school:
        m 1eua "平冈中学, 龙岗."
        m 1euc "平冈是龙岗的老牌学校之一."
        m 1ekc "平冈的校园很大, 绿化也很好."
        m 1ekbsa "你在那里, 一定有很多回忆."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市宝安第一外国语学校 ==========
    elif "宝安第一外国语学校" in school:
        m 1eua "宝安第一外国语学校, 宝安区."
        m 1euc "录取线553分, 是宝安区的公办学校."
        m 1ekc "宝一外的前身是宝安高级中学, 2011年更名."
        m 1ekbsa "你在那里, 一定也学到了很多."
        m 1hua "哪天跟我说说宝一外的事."
        jump school_dorm_check
    # ========== 深圳市西乡中学 ==========
    elif "西乡中学" in school:
        m 1eua "西乡中学, 宝安区西乡街道."
        m 1euc "录取线536分, 是宝安的老牌学校."
        m 1ekc "西乡中学创办于1969年, 办学历史很长."
        m 1ekbsa "你在那里, 一定有很多故事."
        m 1hua "哪天说给我听听."
        jump school_dorm_check
    # ========== 深圳市沙井中学 ==========
    elif "沙井中学" in school:
        m 1eua "沙井中学, 宝安区沙井街道."
        m 1euc "录取线523分, 是宝安的老牌学校."
        m 1ekc "沙井中学创办于1956年, 是宝安历史最悠久的学校之一."
        m 1ekbsa "你在那里, 一定有很多回忆."
        m 1hua "哪天说给我听听."
        jump school_dorm_check
    # ========== 深圳市松岗中学 ==========
    elif "松岗中学" in school:
        m 1eua "松岗中学, 宝安区松岗街道."
        m 1euc "录取线526分, 是宝安的老牌学校."
        m 1ekc "松岗中学创办于1945年, 前身是东宝中学."
        m 1ekbsa "你在那种有历史感的校园里读书, 一定很有感觉."
        m 1hua "哪天跟我讲讲松岗的事."
        jump school_dorm_check
    # ========== 深圳市福海中学 ==========
    elif "福海中学" in school:
        m 1eua "福海中学, 宝安区福海街道."
        m 1euc "录取线521分, 是宝安的新学校."
        m 1ekc "福海中学2022年才创办, 校园很新."
        m 1ekbsa "你在那里, 一定过得很舒服."
        m 1hua "哪天跟我说说福海的事."
        jump school_dorm_check
    # ========== 深圳市龙岗区布吉中学 ==========
    elif "布吉中学" in school:
        m 1eua "布吉中学, 龙岗区布吉街道."
        m 1euc "录取线507分, 是龙岗的老牌学校."
        m 1ekc "布吉中学创办于1975年, 办学历史很长."
        m 1ekbsa "你在那里, 一定有很多回忆."
        m 1hua "哪天说给我听听."
        jump school_dorm_check
    # ========== 深圳市龙岗区横岗高级中学 ==========
    elif "横岗高级中学" in school:
        m 1eua "横岗高级中学, 龙岗区横岗街道."
        m 1euc "录取线509分, 是龙岗的公办学校."
        m 1ekc "横岗高级中学2011年创办, 校园很新."
        m 1ekbsa "你在那里, 一定过得很舒服."
        m 1hua "哪天跟我说说横岗的事."
        jump school_dorm_check
    # ========== 深圳市龙岗区平湖外国语学校 ==========
    elif "平湖外国语学校" in school:
        m 1eua "平湖外国语学校, 龙岗区平湖街道."
        m 1euc "录取线510分, 是龙岗的公办学校."
        m 1ekbsa "平湖外国语的外语教学很有特色."
        m 1ekc "你的外语一定很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳市龙岗区华中师范大学龙岗附属中学 ==========
    elif "华中师范大学龙岗附属中学" in school:
        m 1eua "华中师范大学龙岗附属中学, 龙岗区."
        m 1euc "录取线545分, 是龙岗的优质学校."
        m 1ekc "华中师大龙岗附中2013年创办, 依托华中师大的资源."
        m 1ekbsa "你在那里, 一定学到了很多."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市龙岗区实验高级中学 ==========
    elif "龙岗区实验高级中学" in school:
        m 1eua "龙岗区实验高级中学, 龙岗区."
        m 1euc "录取线532分, 是龙岗的优质学校."
        m 1ekc "龙岗区实验高级中学2021年创办, 是龙岗的新学校."
        m 1ekbsa "你在那里, 一定过得很充实."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市龙华中学 ==========
    elif "龙华中学" in school:
        m 1eua "龙华中学, 龙华区."
        m 1euc "录取线519分, 是龙华的老牌学校."
        m 1ekc "龙华中学创办于1956年, 是龙华历史最悠久的学校之一."
        m 1ekbsa "你在那里, 一定有很多回忆."
        m 1hua "哪天说给我听听."
        jump school_dorm_check
    # ========== 深圳市观澜中学 ==========
    elif "观澜中学" in school:
        m 1eua "观澜中学, 龙华区观澜街道."
        m 1euc "录取线519分, 是龙华的老牌学校."
        m 1ekc "观澜中学创办于1914年, 前身是振能学校."
        m 1ekbsa "你在那种有百年历史的校园里读书, 一定很有感觉."
        m 1hua "哪天跟我讲讲观澜的事."
        jump school_dorm_check
    # ========== 深圳市龙华高级中学 ==========
    elif "龙华高级中学" in school:
        m 1eua "龙华高级中学, 龙华区."
        m 1euc "录取线546分, 是龙华的优质学校."
        m 1ekc "龙华高级中学2018年创办, 是龙华的新学校."
        m 1ekbsa "你在那里, 一定过得很充实."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市艺术高中 ==========
    elif "艺术高中" in school:
        m 1eua "深圳市艺术高中, 龙华区."
        m 1euc "录取线500分, 是深圳唯一一所以艺术为特色的公办高中."
        m 1ekbsa "艺术高中的学生都很有才华."
        m 1ekc "你一定也很有艺术天赋."
        m 1hua "哪天表演给我看看."
        jump school_dorm_check
    # ========== 深圳市格致中学 ==========
    elif "格致中学" in school:
        m 1eua "深圳市格致中学, 龙华区."
        m 1euc "录取线537分, 是龙华的新学校."
        m 1ekc "格致中学2021年创办, 是深圳第一所科学高中."
        m 1ekbsa "你在那里, 一定学到了很多科学知识."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市红山中学 ==========
    elif "红山中学" in school:
        m 1eua "深圳市红山中学, 龙华区."
        m 1euc "录取线532分, 是龙华的新学校."
        m 1ekc "红山中学2021年创办, 校园很新."
        m 1ekbsa "你在那里, 一定过得很充实."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市龙华外国语高级中学 ==========
    elif "龙华外国语高级中学" in school:
        m 1eua "深圳市龙华外国语高级中学, 龙华区."
        m 1euc "录取线525分, 是龙华的新学校."
        m 1ekbsa "龙华外国语高级中学的外语教学很有特色."
        m 1ekc "你的外语一定很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳市致理中学 ==========
    elif "致理中学" in school:
        m 1eua "深圳市致理中学, 龙华区."
        m 1euc "录取线521分, 是龙华的新学校."
        m 1ekc "致理中学2022年创办, 校园很新."
        m 1ekbsa "你在那里, 一定过得很充实."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市龙华科技实验高级中学 ==========
    elif "龙华科技实验高级中学" in school:
        m 1eua "深圳市龙华科技实验高级中学, 龙华区."
        m 1euc "录取线518分, 是龙华的新学校."
        m 1ekc "龙华科技实验高级中学2022年创办, 注重科技教育."
        m 1ekbsa "你在那里, 一定学到了很多科技知识."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市坪山高级中学 ==========
    elif "坪山高级中学" in school:
        m 1eua "坪山高级中学, 坪山区."
        m 1euc "录取线517分, 是坪山的公办学校."
        m 1ekc "坪山高级中学创办于2006年, 是坪山的第一所公办高中."
        m 1ekbsa "你在那里, 一定有很多故事."
        m 1hua "哪天说给我听听."
        jump school_dorm_check
    # ========== 深圳市聚龙科学中学 ==========
    elif "聚龙科学中学" in school:
        m 1eua "深圳市聚龙科学中学, 坪山区."
        m 1euc "录取线511分, 是坪山的新学校."
        m 1ekc "聚龙科学中学2022年创办, 注重科学教育."
        m 1ekbsa "你在那里, 一定学到了很多科学知识."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市光明区高级中学 ==========
    elif "光明区高级中学" in school:
        m 1eua "光明区高级中学, 光明区."
        m 1euc "录取线520分, 是光明的公办学校."
        m 1ekc "光明区高级中学创办于2007年, 是光明区第一所公办高中."
        m 1ekbsa "你在那里, 一定有很多故事."
        m 1hua "哪天说给我听听."
        jump school_dorm_check
    # ========== 深圳市光明中学 ==========
    elif "光明中学" in school:
        m 1eua "光明中学, 光明区."
        m 1euc "录取线501分, 是光明的老牌学校."
        m 1ekc "光明中学创办于1965年, 办学历史很长."
        m 1ekbsa "你在那里, 一定有很多回忆."
        m 1hua "哪天说给我听听."
        jump school_dorm_check
    # ========== 中科附高 ==========
    elif "中科附高" in school or "中国科学院深圳理工大学附属实验高级中学" in school:
        m 1eua "中科附高, 光明区."
        m 1euc "录取线529分, 是中国科学院深圳理工大学附属的实验高中."
        m 1ekc "中科附高2021年创办, 依托中科院的资源."
        m 1ekbsa "你在那里, 一定学到了很多科学知识."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 红岭教育集团大鹏华侨中学 ==========
    elif "大鹏华侨中学" in school:
        m 1eua "红岭教育集团大鹏华侨中学, 大鹏新区."
        m 1euc "录取线508分, 2022年加入红岭教育集团."
        m 1ekc "大鹏华侨中学靠海, 环境很好."
        m 1ekbsa "你在那里, 一定过得很舒服."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市罗湖高级中学 ==========
    elif "罗湖高级中学" in school:
        m 1eua "罗湖高级中学, 罗湖区."
        m 1euc "录取线515分, 是罗湖的公办学校."
        m 1ekc "罗湖高级中学2018年由滨河中学和罗湖外语合并而成."
        m 1ekbsa "你在那里, 一定有很多故事."
        m 1hua "哪天说给我听听."
        jump school_dorm_check
    # ========== 深圳市罗湖外语学校 ==========
    elif "罗湖外语学校" in school:
        m 1eua "罗湖外语学校, 罗湖区."
        m 1euc "录取线510分, 是罗湖的公办学校."
        m 1ekbsa "罗湖外语的外语教学很有特色."
        m 1ekc "你的外语一定很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳市美术学校 ==========
    elif "美术学校" in school:
        m 1eua "深圳市美术学校, 罗湖区."
        m 1euc "录取线500分, 是深圳唯一一所公办美术高中."
        m 1ekbsa "美术学校的学生都很有艺术天赋."
        m 1ekc "你一定也很会画画."
        m 1hua "哪天画给我看看."
        jump school_dorm_check
    # ========== 深圳市行知职业技术学校 ==========
    elif "行知职业技术学校" in school:
        m 1eua "深圳市行知职业技术学校, 罗湖区."
        m 1euc "录取线490分, 是深圳的老牌职校."
        m 1ekc "行知有综合高中班, 既能学文化课也能学技能."
        m 1ekbsa "你在那里, 一定学到了很多实用的东西."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市盐田高级中学 ==========
    elif "盐田高级中学" in school:
        m 1eua "盐田高级中学, 盐田区."
        m 1euc "录取线529分, 是盐田的公办学校."
        m 1ekc "盐田高级中学创办于1984年, 靠海, 环境很好."
        m 1ekbsa "你在那里读书, 一定每天都能看到海."
        m 1hua "我有点羡慕你."
        jump school_dorm_check
    # ========== 深圳市盐港中学 ==========
    elif "盐港中学" in school:
        m 1eua "深圳市盐港中学, 盐田区."
        m 1euc "录取线490分, 是盐田的公办学校."
        m 1ekc "盐港中学有综合高中班, 也有职业班."
        m 1ekbsa "你在那里, 一定学到了很多."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市南头中学 ==========
    elif "南头中学" in school:
        m 1eua "南头中学, 南山区."
        m 1euc "录取线534分, 是南山的老牌学校."
        m 1ekc "南头中学创办于1906年, 前身是宝安县立第一中学."
        m 1ekbsa "你在那种百年老校里读书, 一定很有感觉."
        m 1hua "哪天跟我讲讲南头的事."
        jump school_dorm_check
    # ========== 深圳市华侨城高级中学 ==========
    elif "华侨城高级中学" in school:
        m 1eua "华侨城高级中学, 南山区."
        m 1euc "录取线536分, 是南山的公办学校."
        m 1ekc "华侨城高级中学在华侨城片区, 环境很好."
        m 1ekbsa "你在那里, 一定过得很舒服."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 北京师范大学南山附属学校 ==========
    elif "北京师范大学南山附属学校" in school:
        m 1eua "北京师范大学南山附属学校, 南山区."
        m 1euc "录取线542分, 是南山的优质学校."
        m 1ekc "北师大南山附校依托北京师范大学的资源, 师资很强."
        m 1ekbsa "你在那里, 一定学到了很多."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市福田中学 ==========
    elif "福田中学" in school:
        m 1eua "福田中学, 福田区."
        m 1euc "录取线530分, 是福田的老牌学校."
        m 1ekc "福田中学创办于1969年, 是福田区第一所公办高中."
        m 1ekbsa "你在那里, 一定有很多回忆."
        m 1hua "哪天说给我听听."
        jump school_dorm_check
    # ========== 深圳市第二实验学校明远高中 ==========
    elif "第二实验学校明远高中" in school:
        m 1eua "深圳市第二实验学校明远高中, 大鹏新区."
        m 1euc "录取线502分, 是二实的新校区."
        m 1ekc "明远高中2022年创办, 是大鹏新区的新学校."
        m 1ekbsa "你在那里, 一定过得很充实."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市第二高级中学深汕实验学校 ==========
    elif "第二高级中学深汕实验学校" in school:
        m 1eua "深圳市第二高级中学深汕实验学校, 深汕特别合作区."
        m 1euc "录取线490分, 是二高的新校区."
        m 1ekc "深汕实验学校2022年创办, 在深汕特别合作区."
        m 1ekbsa "你在那里, 一定有很多故事."
        m 1hua "哪天说给我听听."
        jump school_dorm_check
    # ========== 深圳市第三高级中学（留学班） ==========
    elif "第三高级中学" in school and "留学" in school:
        m 1eua "深圳市第三高级中学留学班, 龙岗区."
        m 1euc "录取线490分, 是专门为出国留学准备的班级."
        m 1ekbsa "留学班的同学都很有国际视野."
        m 1ekc "你以后想去哪个国家?"
        m 1hua "不管去哪, 都要记得回来看我."
        jump school_dorm_check
    # ========== 深圳科学高中龙岗分校 ==========
    elif "深圳科学高中龙岗分校" in school:
        m 1eua "深圳科学高中龙岗分校, 龙岗区."
        m 1euc "录取线527分, 是科高的分校."
        m 1ekc "科高龙岗分校2021年创办, 注重科学教育."
        m 1ekbsa "你在那里, 一定学到了很多科学知识."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市第七高级中学 ==========
    elif "第七高级中学" in school:
        m 1eua "深圳市第七高级中学, 宝安区."
        m 1euc "录取线518分, 是宝安的公办学校."
        m 1ekc "七高2015年创办, 是宝安的新学校."
        m 1ekbsa "你在那里, 一定过得很充实."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳技术大学附属中学 ==========
    elif "深圳技术大学附属中学" in school:
        m 1eua "深圳技术大学附属中学, 坪山区."
        m 1euc "录取线528分, 是深技大附中."
        m 1ekc "深技大附中依托深圳技术大学的资源, 注重实践."
        m 1ekbsa "你在那里, 一定学到了很多实用的东西."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 东北师范大学附属中学深圳学校 ==========
    elif "东北师范大学附属中学深圳学校" in school:
        m 1eua "东北师范大学附属中学深圳学校, 坪山区."
        m 1euc "录取线526分, 是东北师大附中在深圳的分校."
        m 1ekc "东北师大附中是全国名校, 深圳校区也很有实力."
        m 1ekbsa "你在那里, 一定很努力."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳北理莫斯科大学附属实验中学 ==========
    elif "深圳北理莫斯科大学附属实验中学" in school:
        m 1eua "深圳北理莫斯科大学附属实验中学, 龙岗区."
        m 1euc "录取线525分, 是深北莫的附属中学."
        m 1ekc "深北莫附中依托深圳北理莫斯科大学的资源, 很有国际范."
        m 1ekbsa "你在那里, 一定学到了很多."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳理工大学附属中学 ==========
    elif "深圳理工大学附属中学" in school:
        m 1eua "深圳理工大学附属中学, 光明区."
        m 1euc "录取线523分, 是深理工的附属中学."
        m 1ekc "深理工附中2023年创办, 是深圳的新学校."
        m 1ekbsa "你在那里, 一定过得很充实."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市曙光中学 ==========
    elif "曙光中学" in school:
        m 1eua "深圳市曙光中学, 光明区."
        m 1euc "录取线490分, 是深圳的综合高中."
        m 1ekc "曙光中学既有文化课, 也有职业技能课."
        m 1ekbsa "你在那里, 一定学到了很多实用的东西."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳创新高级中学 ==========
    elif "创新高级中学" in school:
        m 1eua "深圳创新高级中学, 龙岗区."
        m 1euc "录取线490分, 是深圳的综合高中."
        m 1ekc "创新高级中学注重实践和创新."
        m 1ekbsa "你在那里, 一定学到了很多."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市体育实验学校 ==========
    elif "体育实验学校" in school:
        m 1eua "深圳市体育实验学校, 龙岗区."
        m 1euc "录取线490分, 是深圳唯一一所体育特色公办高中."
        m 1ekbsa "体育实验学校的学生都很爱运动."
        m 1ekc "你一定也很擅长运动."
        m 1hua "哪天教我打球."
        jump school_dorm_check
    # ========== 深圳市罗湖区华美外国语学校 ==========
    elif "华美外国语学校" in school:
        m 1eua "深圳市罗湖区华美外国语学校, 罗湖区."
        m 1euc "录取线约400分, 是罗湖的民办学校."
        m 1ekbsa "华美外国语注重外语教学, 也有国际课程."
        m 1ekc "你的外语一定很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳市万科梅沙书院 ==========
    elif "万科梅沙书院" in school:
        m 1eua "深圳市万科梅沙书院, 盐田区."
        m 1euc "它是深圳很有名的民办国际化学校."
        m 1ekc "万科梅沙的校园靠海, 环境非常漂亮."
        m 1ekbsa "你在那里读书, 一定每天都能看到海."
        m 1hua "我有点羡慕你."
        jump school_dorm_check
    # ========== 深圳市盐田区梅沙双语学校 ==========
    elif "梅沙双语学校" in school:
        m 1eua "深圳市盐田区梅沙双语学校, 盐田区."
        m 1euc "它是深圳的民办双语学校."
        m 1ekc "梅沙双语注重中英文教学, 课程很丰富."
        m 1ekbsa "你的中英文一定都很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳（南山）中加学校 ==========
    elif "中加学校" in school:
        m 1eua "深圳（南山）中加学校, 南山区."
        m 1euc "它是深圳的民办国际化学校."
        m 1ekc "中加学校有中加两国课程, 国际氛围很好."
        m 1ekbsa "你以后想去加拿大吗?"
        m 1hua "不管去哪, 都要记得回来看我."
        jump school_dorm_check
    # ========== 深圳市南山中英文学校 ==========
    elif "南山中英文学校" in school:
        m 1eua "深圳市南山中英文学校, 南山区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "南山中英文注重中英文教学."
        m 1ekbsa "你的中英文一定都很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳东方英文书院 ==========
    elif "东方英文书院" in school:
        m 1eua "深圳东方英文书院, 宝安区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "东方英文书院注重英文教学."
        m 1ekbsa "你的英文一定很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳市崛起实验中学 ==========
    elif "崛起实验中学" in school:
        m 1eua "深圳市崛起实验中学, 宝安区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "崛起实验的校风很踏实."
        m 1ekbsa "你在那里, 一定学到了很多."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市桃源居中澳实验学校 ==========
    elif "桃源居中澳实验学校" in school:
        m 1eua "深圳市桃源居中澳实验学校, 宝安区."
        m 1euc "它是深圳很大的民办学校."
        m 1ekc "中澳实验的校园很大, 设施也很齐全."
        m 1ekbsa "你在那里, 一定有很多回忆."
        m 1hua "哪天说给我听听."
        jump school_dorm_check
    # ========== 深圳市华胜实验学校 ==========
    elif "华胜实验学校" in school:
        m 1eua "深圳市华胜实验学校, 宝安区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "华胜实验的校风很踏实."
        m 1ekbsa "你在那里, 一定学到了很多."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市富源学校 ==========
    elif "富源学校" in school:
        m 1eua "深圳市富源学校, 宝安区."
        m 1euc "它是深圳很有名的民办学校."
        m 1ekc "富源的校园很大, 管理也很严格."
        m 1ekbsa "你在那里, 一定很辛苦."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市华侨（康桥）书院 ==========
    elif "康桥书院" in school:
        m 1eua "深圳市华侨（康桥）书院, 宝安区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "康桥书院的名字很有诗意."
        m 1ekbsa "你在那里, 一定过得很舒服."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市明德外语实验学校 ==========
    elif "明德外语实验学校" in school:
        m 1eua "深圳市明德外语实验学校, 宝安区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "明德外语注重外语教学."
        m 1ekbsa "你的外语一定很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳市宝安区中英公学 ==========
    elif "中英公学" in school:
        m 1eua "深圳市宝安区中英公学, 宝安区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "中英公学注重中英文教学."
        m 1ekbsa "你的中英文一定都很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳市松岗中英文实验学校 ==========
    elif "松岗中英文实验学校" in school:
        m 1eua "深圳市松岗中英文实验学校, 宝安区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "松岗中英文注重中英文教学."
        m 1ekbsa "你的中英文一定都很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳市宝安区翻身实验学校 ==========
    elif "翻身实验学校" in school:
        m 1eua "深圳市宝安区翻身实验学校, 宝安区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "翻身实验的名字很有故事."
        m 1ekbsa "你在那里, 一定有很多回忆."
        m 1hua "哪天说给我听听."
        jump school_dorm_check
    # ========== 深圳市华一实验学校 ==========
    elif "华一实验学校" in school:
        m 1eua "深圳市华一实验学校, 宝安区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "华一实验的校风很踏实."
        m 1ekbsa "你在那里, 一定学到了很多."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市福桥高级中学 ==========
    elif "福桥高级中学" in school:
        m 1eua "深圳市福桥高级中学, 宝安区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "福桥高级中学的名字很有福气."
        m 1ekbsa "你在那里, 一定过得很舒服."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市滨海高级中学 ==========
    elif "滨海高级中学" in school:
        m 1eua "深圳市滨海高级中学, 宝安区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "滨海高级中学靠海, 环境很好."
        m 1ekbsa "你在那里, 一定过得很舒服."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市宝融高级中学 ==========
    elif "宝融高级中学" in school:
        m 1eua "深圳市宝融高级中学, 宝安区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "宝融高级中学的校风很踏实."
        m 1ekbsa "你在那里, 一定学到了很多."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市龙岗区东升学校 ==========
    elif "东升学校" in school:
        m 1eua "深圳市龙岗区东升学校, 龙岗区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "东升学校的名字很有朝气."
        m 1ekbsa "你在那里, 一定过得很充实."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市建文外国语学校 ==========
    elif "建文外国语学校" in school:
        m 1eua "深圳市建文外国语学校, 龙岗区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "建文外国语注重外语教学."
        m 1ekbsa "你的外语一定很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳市龙岗区科城实验学校 ==========
    elif "科城实验学校" in school:
        m 1eua "深圳市龙岗区科城实验学校, 龙岗区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "科城实验的名字很有科技感."
        m 1ekbsa "你在那里, 一定学到了很多."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市承翰学校 ==========
    elif "承翰学校" in school:
        m 1eua "深圳市承翰学校, 龙岗区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "承翰学校的校园很大, 环境也很好."
        m 1ekbsa "你在那里, 一定过得很舒服."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市枫叶学校 ==========
    elif "枫叶学校" in school:
        m 1eua "深圳市枫叶学校, 龙岗区."
        m 1euc "它是深圳的民办国际化学校."
        m 1ekc "枫叶学校的名字很有诗意."
        m 1ekbsa "你在那里, 一定过得很舒服."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市龙岗区德琳学校 ==========
    elif "德琳学校" in school:
        m 1eua "深圳市龙岗区德琳学校, 龙岗区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "德琳学校的校风很踏实."
        m 1ekbsa "你在那里, 一定学到了很多."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳菁华中英文实验中学 ==========
    elif "菁华中英文实验中学" in school:
        m 1eua "深圳菁华中英文实验中学, 龙岗区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "菁华注重中英文教学."
        m 1ekbsa "你的中英文一定都很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳市龙华中英文实验学校 ==========
    elif "龙华中英文实验学校" in school:
        m 1eua "深圳市龙华中英文实验学校, 龙华区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "龙华中英文注重中英文教学."
        m 1ekbsa "你的中英文一定都很好."
        m 1hua "哪天说两句给我听听."
        jump school_dorm_check
    # ========== 深圳市展华实验学校 ==========
    elif "展华实验学校" in school:
        m 1eua "深圳市展华实验学校, 龙华区."
        m 1euc "它是深圳的民办学校."
        m 1ekc "展华实验的校风很踏实."
        m 1ekbsa "你在那里, 一定学到了很多."
        m 1hua "哪天跟我说说."
        jump school_dorm_check
    # ========== 深圳市第一职业技术学校 ==========
    elif "深圳市第一职业技术学校" in school:
        m 1eua "深圳一职."
        m 1euc "深圳最早的一批公办职校了, 在福田区, 位置很好."
        m 1ekbsa "你在那里, 学的是计算机、电子还是别的专业?"
        m 1tku "能在市中心上学, 放学是不是经常去逛街?"
        m 1hksdlb "别只顾着玩, 也要记得早点回家."
        jump school_dorm_check
    # ========== 深圳市第二职业技术学校 ==========
    elif "深圳市第二职业技术学校" in school:
        m 1eua "深圳二职."
        m 1euc "在光明区, 校园应该很大很漂亮吧."
        m 1ekbsa "二职的实训设备好像很厉害."
        m 1tku "你是不是每天都在那里捣鼓汽车或者数控机床?"
        m 1hua "满手油污的样子, 其实也挺帅的."
        jump school_dorm_check
    # ========== 深圳市第三职业技术学校 ==========
    elif "深圳市第三职业技术学校" in school:
        m 1eua "深圳三职."
        m 1euc "在坪山区, 也是老牌公办职校了."
        m 1ekbsa "听说那里的宿舍条件很好."
        m 1ekc "住宿的话, 晚上会不会跟室友聊天聊到很晚?"
        m 1hua "记得早点睡, 别熬夜."
        jump school_dorm_check
    # ========== 深圳市新鹏职业高级中学 ==========
    elif "深圳市新鹏职业高级中学" in school:
        m 1eua "新鹏职高."
        m 1euc "在光明区, 听说是专门做职业教育的学校."
        m 1ekbsa "你在那里, 有没有参加过什么技能大赛?"
        m 1tku "如果拿了奖, 记得第一时间告诉我."
        m 1hua "我要把你夸上天."
        jump school_dorm_check
    # ========== 深圳艺术学校 ==========
    elif "深圳艺术学校" in school:
        m 1eua "深圳艺术学校."
        m 1euc "艺术学校的学生, 气质一定都特别好吧."
        m 1ekbsa "你是学什么的? 舞蹈、音乐, 还是美术?"
        m 1tku "你会不会在琴房里练琴练到很晚?"
        m 1hua "真想坐在旁边听你弹一首曲子."
        jump school_dorm_check
    # ========== 深圳市博伦职业技术学校 ==========
    elif "深圳市博伦职业技术学校" in school:
        m 1eua "博伦职校."
        m 1euc "在南山区, 靠近深圳湾."
        m 1ekbsa "你在那里读书, 是不是每天都能吹到海风?"
        m 1tku "听说那里的珠宝专业很有名, 你会不会鉴别钻石?"
        m 1hksdlb "以后给我挑戒指, 就交给你了."
        jump school_dorm_check
    # ========== 深圳市龙华职业技术学校 ==========
    elif "深圳市龙华职业技术学校" in school:
        m 1eua "龙华职校."
        m 1euc "龙华区的新学校, 校园应该很现代化吧."
        m 1ekbsa "你在那里, 学的专业跟这里的产业对口吗?"
        m 1tku "说不定以后还能去大公司上班."
        m 1hua "不管你以后去哪上班, 都要记得按时吃饭."
        jump school_dorm_check

    # ========== 深圳市龙岗区第二职业技术学校 ==========
    elif "龙岗区第二职业技术学校" in school:
        m 1eua "龙岗二职."
        m 1euc "在龙岗区, 好像有很多很有意思的专业."
        m 1ekbsa "你在那里, 有没有找到自己真正喜欢做的事情?"
        m 1ekc "如果找到了, 就要好好坚持下去."
        m 1hua "我会在背后默默支持你的."
        jump school_dorm_check
    # ========== 深圳市奋达职业技术学校 ==========
    elif "深圳市奋达职业技术学校" in school:
        m 1eua "奋达职校."
        m 1euc "奋达, 这个名字听起来就很有拼搏的精神."
        m 1ekbsa "你在那里读书, 一定也很努力吧."
        m 1ekc "但拼搏归拼搏, 身体才是革命的本钱."
        m 1hua "别把自己累垮了, 我会心疼的."
        jump school_dorm_check
    # ========== 深圳市携创高级技工学校 ==========
    elif "深圳市携创高级技工学校" in school:
        m 1eua "携创高级技校."
        m 1euc "在龙岗区, 是一所很大的技工学校."
        m 1ekbsa "你在那里学的是什么技术?"
        m 1tku "是数控、汽修, 还是电子商务?"
        m 1hua "不管是什么, 掌握一门硬核技术, 走到哪里都不怕."
        jump school_dorm_check
    # ========== 深圳市宝山技工学校 ==========
    elif "深圳市宝山技工学校" in school:
        m 1eua "宝山技校."
        m 1euc "在坪山区, 听说管理很严格."
        m 1ekbsa "你在那里, 是不是每天都要穿校服, 按时跑操?"
        m 1ekc "虽然严格, 但也是为了你们好."
        m 1hua "坚持下来, 你会变得更优秀的."
        jump school_dorm_check
    # ========== 深圳市深德高级技工学校 ==========
    elif "深圳市深德高级技工学校" in school:
        m 1eua "深德高级技校."
        m 1euc "在龙华区, 深德这两个字听起来就很厚重."
        m 1ekbsa "你在那里学技术, 一定会成为很有用的人."
        m 1ekc "但我希望, 你不仅是技术上的高手, 也是生活里的温柔人."
        m 1hua "就像现在这样."
        jump school_dorm_check
    # ========== 深圳市华夏技工学校 ==========
    elif "深圳市华夏技工学校" in school:
        m 1eua "华夏技校."
        m 1euc "华夏这两个字很大, 很有气势."
        m 1ekbsa "你在坪山那边读书, 应该也学到了很多扎实的本领吧."
        m 1tku "以后要是家里什么东西坏了, 你是不是都能修好?"
        m 1hua "那太好了, 我就缺一个全能修理工."
        jump school_dorm_check
    # ========== 深圳市科迪技工学校 ==========
    elif "深圳市科迪技工学校" in school:
        m 1eua "科迪技校."
        m 1euc "在坪山区, 科迪这个名字听起来很现代."
        m 1ekbsa "你在那里, 是不是经常要动手实操?"
        m 1tku "比起坐在教室里听枯燥的理论, 你是不是更喜欢动手?"
        m 1hua "动手能力强的人, 以后一定很吃香."
        jump school_dorm_check
    # ========== 深圳市宝民技工学校 ==========
    elif "深圳市宝民技工学校" in school:
        m 1eua "宝民技校."
        m 1euc "在宝安区, 是一所老牌的技工学校了."
        m 1ekbsa "你在那里, 一定认识了很多技术很好的老师吧."
        m 1ekc "跟着他们好好学, 以后肯定有出息."
        m 1hua "我相信你."
        jump school_dorm_check
    # ========== 深圳市深科技工学校 ==========
    elif "深圳市深科技工学校" in school:
        m 1eua "深科技校."
        m 1euc "在光明区, 也是学技术的地方."
        m 1ekbsa "你每天跟机器和零件打交道, 会不会觉得很枯燥?"
        m 1tku "其实我觉得专注做一件事的人特别帅."
        m 1hua "尤其是在你满手机油还冲我笑的时候."
        jump school_dorm_check
    # ========== 深圳市智理技工学校 ==========
    elif "深圳市智理技工学校" in school:
        m 1eua "智理技校."
        m 1euc "智理, 听起来就是智慧与理性的结合."
        m 1ekbsa "你在那里读书, 是不是也学会了非常严谨的思考方式?"
        m 1ekc "但有时候太理性了也不好."
        m 1hua "偶尔也可以像现在这样, 感性一点, 多想想我."
        jump school_dorm_check
    # ========== 深圳市中特技工学校 ==========
    elif "深圳市中特技工学校" in school:
        m 1eua "中特技校."
        m 1euc "在坪山区, 专门培养技术人才."
        m 1ekbsa "你学的是哪一种特种技术?"
        m 1tku "是不是那种别人都不会, 只有你会的神奇技能?"
        m 1hua "如果是的话, 那你可要好好教教我."
        jump school_dorm_check
    # ========== 深圳市宝安职业技术学校 ==========
    elif "深圳市宝安职业技术学校" in school:
        m 1eua "宝安职校."
        m 1euc "宝安区很大的公办职校了."
        m 1ekbsa "那里的校园环境很好, 你平时会不会在操场上散步?"
        m 1ekc "散步的时候, 会不会偶尔想起我?"
        m 1hua "就算你没有, 我也不会怪你的."
        jump school_dorm_check
    # ========== 深圳市沙井职业高级中学 ==========
    elif "深圳市沙井职业高级中学" in school:
        m 1eua "沙井职高."
        m 1euc "在宝安区沙井街道, 那边靠海."
        m 1ekbsa "你每天上学, 是不是能吹到海风?"
        m 1tku "听说沙井的生蚝特别有名."
        m 1hksdlb "下次有机会, 替我多吃几个."
        jump school_dorm_check
    # ========== 深圳市龙岗职业技术学校 ==========
    elif "深圳市龙岗职业技术学校" in school:
        m 1eua "龙岗职校."
        m 1euc "龙岗区的老牌公办职校."
        m 1ekbsa "你在那里, 应该学到了很多实用的技能吧."
        m 1ekc "现在的社会, 有技术的人才是最吃香的."
        m 1hua "所以我一点都不担心你的未来."
        jump school_dorm_check
    # ========== 深圳市龙华区宝文学校 ==========
    elif "宝文学校" in school:
        m 1eua "宝文学校."
        m 1euc "在龙华区, 是一所十二年一贯制的学校."
        m 1ekbsa "从小学一直读到高中, 应该有很多从小玩到大的朋友吧."
        m 1ekc "那种友情一定很珍贵."
        m 1hua "要是他们欺负你, 记得告诉我, 我替你骂他们."
        jump school_dorm_check
    # ========== 深圳市崛起职业技术学校 ==========
    elif "崛起职业技术学校" in school:
        m 1eua "崛起职校."
        m 1euc "崛起这两个字, 听起来就很有力量."
        m 1ekbsa "你在那里读书, 是为了以后的腾飞做准备吧."
        m 1ekc "但起飞之前, 也要好好吃饭."
        m 1hua "不然飞到一半没力气了怎么办?"
        jump school_dorm_check
 # ========== 广州 ==========
    # ========== 华南师范大学附属中学（石牌校区） ==========
    if "华南师范大学附属中学" in school and "知识城" not in school:
        m 1eua "华附啊."
        m 1ekc "全省最好的学校之一, 每年都有一堆人挤破头想进去."
        m 1dsc "你在那种地方待了三年, 身边应该全是特别厉害的人."
        m 1eka "有时候, 身边的人越强, 越容易觉得自己不够好."
        m 1hua "但你撑过来了, 这就够了."
        jump school_dorm_check
    # ========== 广州大学附属中学 ==========
    elif "广州大学附属中学" in school:
        m 1eua "广大附中."
        m 1tku "名字里带着广州大学, 听起来就很气派."
        m 1euc "其实我一直很好奇, 大学和附中离得近, 会不会有一种提前长大的感觉?"
        m 1ekbsa "你每天走在那种地方, 会不会偶尔也想象过以后的大学生活?"
        jump school_dorm_check
    # ========== 广东实验中学（荔湾校区） ==========
    elif "广东实验中学" in school and "荔湾" in school:
        m 1eua "省实, 荔湾校区."
        m 1ekbsa "1872年, 留美幼童先修班."
        m 1dsc "一想到你读书的地方, 比我们现在所在的这个世界还要早一百多年, 我就觉得有点不可思议."
        m 1ekc "时间这种东西, 对我来说一直很模糊."
        m 1hua "但你在那里留下的痕迹, 是真实的."
        jump school_dorm_check
    # ========== 广州市执信中学（执信路校区） ==========
    elif "广州市执信中学" in school and "天河" not in school:
        m 1eua "执信."
        m 1euc "我查了一下, 1921年建的, 为了纪念朱执信先生."
        m 1dsc "一百年前的人, 给一百年后的你留下了一所学校."
        m 1ekbsa "你在那里读书的时候, 有没有想过这个问题?"
        jump school_dorm_check
    # ========== 广东广雅中学（荔湾校区） ==========
    elif "广东广雅中学" in school and "花都" not in school:
        m 1eua "广雅啊."
        m 1tku "张之洞创办的, 清末四大书院之一."
        m 1ekc "听起来就很有分量."
        m 1dsc "我有时候会想, 一百多年前的书院里, 是不是也有人像我一样, 坐在某个地方, 等一个不会来的人."
        m 1eka "……算了, 不说这个."
        m 1hua "你在那里, 一定读过很多书."
        jump school_dorm_check
    # ========== 广州市第六中学（海珠校区） ==========
    elif "广州市第六中学" in school and "海珠" in school:
        m 1eua "六中."
        m 1euc "黄埔军校和西南联大的血统, 校训是亲爱精诚."
        m 1ekc "西南联大……那是一个很特别的年代, 一群人在很苦的环境里, 还是坚持读书."
        m 1ekbsa "你在那里读书的时候, 老师有没有讲过那段历史?"
        jump school_dorm_check
    # ========== 广州市铁一中学（越秀校区） ==========
    elif "广州市铁一中学" in school and "越秀" in school:
        m 1eua "铁一."
        m 1tku "管理出了名的严."
        m 1ekc "你在那种地方待了三年, 应该被管得很紧吧."
        m 1ekbsa "但严归严, 铁一出来的学生都很稳."
        m 1hua "你也是."
        jump school_dorm_check
    # ========== 广州市第五中学（校本部） ==========
    elif "广州市第五中学" in school and "金碧" not in school:
        m 1eua "五中."
        m 1euc "1951年创办的, 广州第一所公办完中."
        m 1tku "第一所, 听起来就很特别."
        m 1hua "你在那里读书的时候, 会不会偶尔想到自己也是这段历史的一部分?"
        jump school_dorm_check
    # ========== 广州市天河外国语学校（珠江新城校区） ==========
    elif "广州市天河外国语学校" in school and "智慧城" not in school:
        m 1eua "天外."
        m 1ekbsa "外语学校啊, 你是不是会说好几门语言?"
        m 1tku "我猜你英语一定很好."
        m 1hksdlb "要不……哪天用英语跟我说句话?"
        m 1hua "就当是给我的小礼物."
        jump school_dorm_check
    # ========== 广东仲元中学 ==========
    elif "仲元中学" in school:
        m 1eua "仲元."
        m 1euc "为纪念邓仲元将军而建, 1934年."
        m 1dsc "一个学校以一个人的名字命名, 那个人一定做过很了不起的事."
        m 1ekbsa "你在那里读书的时候, 会不会也想过, 自己以后想成为一个什么样的人?"
        jump school_dorm_check
    # ========== 华南师范大学附属中学（知识城校区） ==========
    if "华南师范大学附属中学" in school and "知识城" in school:
        m 1eua "华附知识城校区."
        m 1ekc "新校区, 2025年才第一次招生."
        m 1euc "你算是那里最早的一批学生了."
        m 1ekbsa "在还没有太多学长学姐的时候, 一切都要靠自己摸索吧."
        m 1hua "那种感觉很特别."
        jump school_dorm_check
    # ========== 广州市第二中学（黄埔校区） ==========
    elif "广州市第二中学" in school and "科学城" not in school:
        m 1eua "二中啊."
        m 1euc "在黄埔, 山水学府."
        m 1tku "听说二中的人都很有主见."
        m 1ekc "你是不是那种, 不容易被别人牵着走的人?"
        m 1hua "如果是的话, 那就更好了."
        jump school_dorm_check
    # ========== 广州市第二中学（科学城校区） ==========
    elif "广州市第二中学" in school and "科学城" in school:
        m 1eua "二中的科学城校区."
        m 1ekbsa "科学城, 听起来就很有未来感."
        m 1euc "你在那里读书的时候, 会不会也想过以后做跟科技有关的事?"
        m 1hua "如果有的话, 记得告诉我."
        jump school_dorm_check
    # ========== 广州市执信中学（天河校区） ==========
    elif "广州市执信中学" in school and "天河" in school:
        m 1eua "执信天河校区."
        m 1euc "2025年招了700人."
        m 1tku "新校区, 一切都很新吧."
        m 1ekbsa "但我更想知道, 你在新校区里, 有没有找到属于自己的那个小角落."
        jump school_dorm_check
    # ========== 广东广雅中学（花都校区） ==========
    elif "广东广雅中学" in school and "花都" in school:
        m 1eua "广雅花都校区."
        m 1euc "也是新校区."
        m 1ekc "新校区有新的好处, 设备好, 环境好, 什么都好."
        m 1dsc "但也少了一点旧校区那种, 踩着几十年前人踩过的楼梯的感觉."
        m 1ekbsa "你更喜欢哪一种?"
        jump school_dorm_check
    # ========== 广州市铁一中学（番禺校区） ==========
    elif "广州市铁一中学" in school and "番禺" in school:
        m 1eua "铁一番禺校区."
        m 1euc "2025年录取线708分, 也上了第一梯度."
        m 1ekc "番禺在广州市区的南边, 离市中心挺远的."
        m 1ekbsa "你每天上学, 是不是要花不少时间?"
        m 1hua "要记得, 路上小心."
        jump school_dorm_check
    # ========== 广州市铁一中学（白云校区） ==========
    elif "广州市铁一中学" in school and "白云" in school:
        m 1eua "铁一白云校区."
        m 1euc "2025年录取线707分, 刚好上了第一梯度."
        m 1ekc "刚好这两个字, 其实很重要."
        m 1ekbsa "差一分和刚好够, 是两个完全不同的世界."
        m 1hua "你能进那里, 一定有你的理由."
        jump school_dorm_check
    # ========== 广州市天河外国语学校（智慧城校区） ==========
    elif "广州市天河外国语学校" in school and "智慧城" in school:
        m 1eua "天外智慧城校区."
        m 1euc "2025年第一次招生, 你就上了第一梯度."
        m 1tku "第一批学生."
        m 1ekbsa "那种感觉, 是不是像在一个还没有规则的游戏里, 自己造规则?"
        m 1hua "我有点羡慕."
        jump school_dorm_check
    # ========== 广州市培英中学（白云新城校区） ==========
    elif "广州市培英中学" in school and "白云新城" in school:
        m 1eua "培英中学."
        m 1euc "白云区最好的学校之一."
        m 1tku "但我更喜欢它的名字, 培英."
        m 1ekbsa "培育英才."
        m 1hua "你在那里读了三年, 一定也被当作英才培养过吧."
        jump school_dorm_check
    # ========== 广州市第十六中学（校本部） ==========
    elif "广州市第十六中学" in school and "水荫" not in school:
        m 1eua "十六中啊."
        m 1euc "1934年创办的, 越秀教育的一面旗帜."
        m 1dsc "旗帜这种东西, 一面就够了."
        m 1ekbsa "你在那里读书的时候, 会不会也觉得自己被寄予了什么?"
        jump school_dorm_check
    # ========== 广州市第七中学（校本部） ==========
    elif "广州市第七中学" in school and "桂花" not in school:
        m 1eua "七中."
        m 1euc "前身是1888年的培道女子中学."
        m 1ekc "女校啊."
        m 1ekbsa "一百多年前, 一群女孩子坐在同一间教室里读书, 那在当时是很不容易的事."
        m 1hua "你读书的地方, 是她们争取来的."
        jump school_dorm_check
    # ========== 广州市第七中学（桂花校区） ==========
    elif "广州市第七中学" in school and "桂花" in school:
        m 1eua "七中桂花校区."
        m 1hksdlb "桂花这两个字, 念起来就甜甜的."
        m 1ekbsa "你每天走进那个校门的时候, 会不会也偶尔觉得心情好一点?"
        m 1hua "我希望会."
        jump school_dorm_check
    # ========== 广州市第三中学 ==========
    elif "广州市第三中学" in school:
        m 1eua "三中."
        m 1euc "1863年."
        m 1ekc "比很多城市的历史还要长."
        m 1dsc "你坐在那间教室里的时候, 有没有想过, 你脚下那块地, 已经安安静静地看着无数人走过去了?"
        m 1ekbsa "然后现在, 它看着你."
        jump school_dorm_check
    # ========== 广州市培正中学 ==========
    elif "广州市培正中学" in school:
        m 1eua "培正."
        m 1tku "红砖绿瓦."
        m 1ekbsa "那种校园, 光是听描述就觉得很好看."
        m 1ekc "我有点想看看, 但我知道我看不到."
        m 1hua "所以以后你路过的时候, 帮我多看一眼, 好不好?"
        jump school_dorm_check
    # ========== 广州市育才中学 ==========
    elif "广州市育才中学" in school:
        m 1eua "育才中学."
        m 1euc "1951年, 建国后不久."
        m 1ekc "那个年代的人办学, 心里装的都是很大的东西."
        m 1ekbsa "你在那里读书, 应该也听过一些老故事."
        m 1hua "哪天讲一段给我听."
        jump school_dorm_check
    # ========== 广州市第二十一中学 ==========
    elif "广州市第二十一中学" in school:
        m 1eua "二十一中."
        m 1euc "1954年创办."
        m 1dsc "没什么特别出名的故事, 也没什么传奇."
        m 1ekbsa "但就是这样一所普通的学校, 装了你三年的日子."
        m 1hua "这就已经很特别了."
        jump school_dorm_check
    # ========== 广东华侨中学 ==========
    elif "广东华侨中学" in school:
        m 1eua "华侨中学."
        m 1euc "广州唯一一所市属侨校, 1930年创办."
        m 1ekc "侨校, 意味着很多人从这里走向世界各地, 又走回来."
        m 1ekbsa "你在那里读书的时候, 有没有想过自己以后也会去哪里?"
        jump school_dorm_check
    # ========== 广州市真光中学（校本部） ==========
    elif "广州市真光中学" in school and "汾水" not in school:
        m 1eua "真光."
        m 1euc "1872年, 岭南最早的女校之一."
        m 1dsc "真光这两个字, 我一直很喜欢."
        m 1ekbsa "真的光."
        m 1hua "你读书的地方, 名字就像一句祝福."
        jump school_dorm_check
    # ========== 广州市第一中学 ==========
    elif "广州市第一中学" in school:
        m 1eua "一中."
        m 1euc "1928年."
        m 1tku "叫一中, 听起来就很有底气."
        m 1ekc "其实我一直觉得, 一个城市的第一中学, 承载的东西比普通学校要多得多."
        m 1ekbsa "你在那里读书, 会不会偶尔也感觉到那份重量?"
        jump school_dorm_check
    # ========== 广州市第四中学 ==========
    elif "广州市第四中学" in school:
        m 1eua "四中."
        m 1euc "1917年创办."
        m 1dsc "我想象了一下, 一百多年前的广州, 街上是什么样子."
        m 1ekbsa "然后你穿着校服走在那条路上的时候, 一百多年就这样过去了."
        m 1hua "时间真快."
        jump school_dorm_check
    # ========== 广州市西关外国语学校 ==========
    elif "西关外国语学校" in school:
        m 1eua "西关外国语."
        m 1euc "西关是广州的老城区, 骑楼、趟栊门、老字号."
        m 1ekbsa "你在那种地方读外语, 感觉像是一边守着旧东西, 一边往新世界走."
        m 1tku "有种很奇妙的对比感."
        m 1hua "你平时会不会路过那些老街?"
        jump school_dorm_check
    # ========== 广州市南海中学 ==========
    elif "广州市南海中学" in school:
        m 1eua "南海中学."
        m 1euc "1904年."
        m 1dsc "一百多年了."
        m 1ekc "我在想, 一百多年前在那里读书的人, 会不会也和你一样, 在教室里发呆, 想一些很远的事."
        m 1ekbsa "你发呆的时候, 会想什么?"
        jump school_dorm_check
    # ========== 广州市第九十七中学 ==========
    elif "广州市第九十七中学" in school:
        m 1eua "九十七中."
        m 1euc "1962年创办."
        m 1tku "九十七这个数字很有意思, 差一点就一百."
        m 1ekbsa "你读书的地方, 名字里就带着一个将近一百的年份, 是不是也有一点特别的感觉?"
        jump school_dorm_check
    # ========== 广州市南武中学 ==========
    elif "广州市南武中学" in school:
        m 1eua "南武中学."
        m 1euc "1905年创办, 广州历史最悠久的学校之一."
        m 1dsc "我查的时候看到一句话, 说南武的精神是坚忍、奉公、力学、爱国."
        m 1ekbsa "你在那里待了三年, 这些词有没有真的走进过你心里?"
        jump school_dorm_check
    # ========== 广州市第四十一中学 ==========
    elif "广州市第四十一中学" in school:
        m 1eua "四十一中."
        m 1euc "1958年."
        m 1ekc "1958年离现在不算太久, 但也不近了."
        m 1ekbsa "你在那里读书的时候, 有没有哪一间教室, 让你到现在还记得?"
        m 1hua "下次路过的时候, 帮我看一眼."
        jump school_dorm_check
    # ========== 广州市海珠外国语实验中学 ==========
    elif "海珠外国语实验中学" in school:
        m 1eua "海珠外国语实验."
        m 1euc "海珠区, 名字里带着外语."
        m 1ekbsa "你是不是从小就开始学英语?"
        m 1hksdlb "我有点好奇, 第一次学一门外语的时候, 是什么感觉?"
        m 1hua "对我来说, 中文已经是我全部的世界了."
        jump school_dorm_check
    # ========== 广州市天河中学 ==========
    elif "广州市天河中学" in school:
        m 1eua "天河中学."
        m 1euc "1988年创办, 天河区最早的公办高中之一."
        m 1tku "天河区其实是一个很新的区."
        m 1ekbsa "你和天河区一起长大, 这种感觉应该挺特别的吧."
        m 1hua "一座城市陪着你长大, 你也看着它变高变亮."
        jump school_dorm_check
    # ========== 广州市第一一三中学 ==========
    elif "广州市第一一三中学" in school:
        m 1eua "一一三中."
        m 1euc "1978年, 刚好是改革开放那一年."
        m 1dsc "那一年很多东西都开始变, 这座学校也是."
        m 1ekbsa "你在那里读书的时候, 老师会不会也讲过那段历史?"
        jump school_dorm_check
    # ========== 广州市第八十九中学 ==========
    elif "广州市第八十九中学" in school:
        m 1eua "八十九中."
        m 1euc "1962年."
        m 1tku "我老觉得这种中间数字的学校, 有一种很安静的气质."
        m 1ekbsa "不太出风头, 但一直稳稳地在那里."
        m 1hua "你是不是也有点像这样?"
        jump school_dorm_check
    # ========== 广州市第七十五中学 ==========
    elif "广州市第七十五中学" in school:
        m 1eua "七十五中."
        m 1euc "1958年."
        m 1ekc "不知道为什么, 每次看到这种老学校, 我都会想到它经历过的那些日子."
        m 1dsc "晴天、雨天、考试周、毕业季, 一遍又一遍."
        m 1ekbsa "然后现在, 它把你送到了我面前."
        jump school_dorm_check
    # ========== 广州市培正中学（白云校区） ==========
    elif "培正中学" in school and "白云" in school:
        m 1eua "培正白云校区."
        m 1euc "培正的老校区在越秀, 红砖绿瓦."
        m 1ekbsa "白云校区应该新一些吧."
        m 1ekc "但我想, 培正的名字不变, 那种感觉就不会变."
        m 1hua "你在那里, 一定也感受到了."
        jump school_dorm_check
    # ========== 广州市白云中学 ==========
    elif "广州市白云中学" in school:
        m 1eua "白云中学."
        m 1euc "1960年创办."
        m 1tku "白云两个字, 很轻, 也很高."
        m 1ekbsa "你在那里读书的时候, 有没有抬头看过天?"
        m 1hua "广州的天空, 是不是经常有很多云?"
        jump school_dorm_check
    # ========== 广州市第八十六中学 ==========
    elif "广州市第八十六中学" in school:
        m 1eua "八十六中."
        m 1euc "1956年, 黄埔区最早的公办高中之一."
        m 1ekc "黄埔这个名字, 一念出来就带着历史的重量."
        m 1ekbsa "你在那里读书的时候, 会不会也偶尔觉得自己站在很长的时间线上?"
        jump school_dorm_check
    # ========== 广州市玉岩中学 ==========
    elif "广州市玉岩中学" in school:
        m 1eua "玉岩中学."
        m 1euc "2005年创办, 算是比较新的学校."
        m 1tku "新学校有一个好处, 什么都是第一次."
        m 1ekbsa "你算是那里的第一批学长学姐之一吧."
        m 1hua "那种感觉, 应该很值得记下来."
        jump school_dorm_check
    # ========== 广州市科学城中学 ==========
    elif "广州市科学城中学" in school:
        m 1eua "科学城中学."
        m 1euc "名字里带着科学."
        m 1ekbsa "你在那里, 是不是也做过一些真正感兴趣的小项目?"
        m 1tku "不是为了考试, 就是单纯觉得好玩的那种."
        m 1hua "有的话, 告诉我."
        jump school_dorm_check
    # ========== 广东仲元中学 ==========
    elif "仲元中学" in school:
        m 1eua "仲元中学."
        m 1euc "1934年, 为纪念邓仲元将军."
        m 1dsc "一个学校, 一个人的名字."
        m 1ekc "我有时候会想, 一个人要做出什么样的事, 才值得被这样记住."
        m 1ekbsa "你以后, 也想成为被记住的人吗?"
        jump school_dorm_check
    # ========== 广州市番禺区禺山高级中学 ==========
    elif "禺山高级中学" in school:
        m 1eua "禺山高级中学."
        m 1euc "禺山, 就是番禺的山."
        m 1ekbsa "一个学校以一座山命名, 好像就把那座山的沉稳也带进去了."
        m 1hua "你在那里读书, 一定也慢慢变得沉稳了吧."
        jump school_dorm_check
    # ========== 广州市番禺区象贤中学 ==========
    elif "象贤中学" in school:
        m 1eua "象贤中学."
        m 1euc "1826年."
        m 1ekc "两百年前."
        m 1dsc "那时候连照相机都还没有, 却已经有人在这里读书了."
        m 1ekbsa "你坐在那间教室里的时候, 有没有想过这个?"
        jump school_dorm_check
    # ========== 广州市花都区秀全中学 ==========
    elif "秀全中学" in school:
        m 1eua "秀全中学."
        m 1euc "1970年创办, 名字来自洪秀全."
        m 1tku "一个学校以人名命名, 那个人一定掀动过很大的风浪."
        m 1ekbsa "你在那里读书, 会不会也偶尔觉得, 自己心里也有一点不安分的东西?"
        jump school_dorm_check
    # ========== 广州市花都区邝维煜纪念中学 ==========
    elif "邝维煜纪念中学" in school:
        m 1eua "邝维煜纪念中学."
        m 1euc "名字很长, 但我猜背后是一个很长很温暖的故事."
        m 1ekbsa "纪念一个人, 让这份记忆一直留在学校里."
        m 1ekc "我有点想知道那个人是谁."
        m 1hua "哪天讲给我听, 好不好?"
        jump school_dorm_check
    # ========== 广州市增城区增城中学 ==========
    elif "增城中学" in school:
        m 1eua "增城中学."
        m 1euc "1928年创办."
        m 1tku "增城这个名字, 听起来就很有烟火气."
        m 1ekbsa "你在那边读书的时候, 是不是也吃过很多只有增城才有的东西?"
        m 1hksdlb "我……有点嘴馋了."
        jump school_dorm_check
    # ========== 广州市从化区从化中学 ==========
    elif "从化中学" in school:
        m 1eua "从化中学."
        m 1euc "1926年创办."
        m 1ekbsa "从化在广州市区的北边, 山多, 绿多."
        m 1ekc "那里的天空, 应该比市区清亮一些吧."
        m 1hua "你在那种地方读书, 心情也会不一样."
        jump school_dorm_check
    # ========== 广州市南沙区南沙第一中学 ==========
    elif "南沙第一中学" in school:
        m 1eua "南沙第一中学."
        m 1euc "1964年创办, 南沙最早的公办高中之一."
        m 1ekc "南沙靠海."
        m 1ekbsa "你在那里读书的时候, 会不会也偶尔吹到海风?"
        m 1hua "我真想和你一起看一次海."
        jump school_dorm_check
    # ========== 广州市黄广中学 ==========
    if "黄广中学" in school:
        m 1eua "黄广中学."
        m 1euc "民办里的名校, 成绩很硬."
        m 1ekc "民办学校和公办不太一样, 学费贵, 压力也大."
        m 1ekbsa "你在那里读了三年, 家里一定也付出了很多."
        m 1hua "你身上背着的东西, 我都知道."
        jump school_dorm_check
    # ========== 广州市黄广附属学校 ==========
    elif "黄广附属学校" in school:
        m 1eua "黄广附校."
        m 1euc "和黄广中学是同一个集团."
        m 1ekc "集团化的学校, 规矩多, 但也稳."
        m 1ekbsa "你在那里, 一定也过得很规律吧."
        m 1hua "能坚持下来, 就已经很厉害了."
        jump school_dorm_check
    # ========== 广州天省实验学校 ==========
    elif "天省实验学校" in school:
        m 1eua "天省实验."
        m 1euc "前身是省实附属天河学校."
        m 1tku "省实的血统."
        m 1ekc "名门出身, 期待自然也高."
        m 1ekbsa "你在那里, 应该经常被拿来和别人比较吧."
        m 1hua "别太在意那些."
        jump school_dorm_check
    # ========== 广州大学附属中学实验学校 ==========
    elif "广大附中实验学校" in school or "广州大学附属中学实验学校" in school:
        m 1eua "广大附中实验学校."
        m 1euc "在从化, 算是比较偏的地方."
        m 1ekc "住宿的话, 应该很少回家吧."
        m 1ekbsa "一个人在那边, 会不会偶尔想家?"
        m 1hua "想家的时候, 也可以来找我."
        jump school_dorm_check
    # ========== 广州市实验外语学校 ==========
    elif "实验外语学校" in school:
        m 1eua "广实外."
        m 1euc "广州最早一批外国语学校之一."
        m 1ekbsa "你在那里, 应该从小就在学外语."
        m 1tku "英语、法语、德语、日语, 会不会好几门都会?"
        m 1hksdlb "有点羡慕."
        jump school_dorm_check
    # ========== 广州市广外附设外语学校 ==========
    elif "广外附设外语学校" in school or "广外外校" in school:
        m 1eua "广外外校."
        m 1euc "背靠广东外语外贸大学."
        m 1ekbsa "那里的学生, 外语水平应该都很高吧."
        m 1ekc "我有点好奇, 你第一次能用外语和别人聊天的时候, 是什么感觉?"
        m 1hua "那种感觉, 应该很像打开了另一扇窗."
        jump school_dorm_check
    # ========== 广州外国语学校 ==========
    elif "广州外国语学校" in school:
        m 1eua "广州外校."
        m 1euc "在南沙, 市属的公办外国语学校."
        m 1ekc "公办的外国语学校不多, 能进去的都很不容易."
        m 1ekbsa "你在那里读了三年, 外语一定已经很流利了."
        m 1hua "哪天跟我说几句, 我想听听你的声音."
        jump school_dorm_check
    # ========== 广州市华美英语实验学校 ==========
    elif "华美英语实验学校" in school:
        m 1eua "华美英语实验."
        m 1euc "办学历史很长."
        m 1ekc "老牌的民办学校, 看着一批又一批学生进来, 又送出去."
        m 1ekbsa "你也是其中一批."
        m 1hua "你有没有想过, 以后回来看看?"
        jump school_dorm_check
    # ========== 广州市番禺区祈福英语实验学校 ==========
    elif "祈福英语实验学校" in school:
        m 1eua "祈福英语实验."
        m 1euc "有国内班, 也有国际班."
        m 1ekc "两条路, 通向完全不同的方向."
        m 1ekbsa "你选的是哪一条?"
        m 1hua "不管选哪条, 我都想和你一起走下去."
        jump school_dorm_check
    # ========== 广州市番禺区华南碧桂园学校 ==========
    elif "华南碧桂园学校" in school:
        m 1eua "华南碧桂园学校."
        m 1euc "在番禺."
        m 1ekbsa "碧桂园这个名字, 听起来就很安静."
        m 1ekc "你在那里读书的时候, 会不会也偶尔觉得日子过得很慢?"
        m 1hua "慢一点, 其实很好."
        jump school_dorm_check
    # ========== 广州市增城区凤凰城中英文学校 ==========
    elif "凤凰城中英文学校" in school:
        m 1eua "凤凰城中英文."
        m 1euc "凤凰城, 名字很好听."
        m 1ekbsa "你在那里读书的时候, 是不是也经常看到凤凰花?"
        m 1ekc "南方的花, 开起来都很热闹."
        m 1hua "我有点想看看."
        jump school_dorm_check
    # ========== 广州市花都区耀华学校 ==========
    elif "耀华学校" in school:
        m 1eua "耀华学校."
        m 1euc "花都的民办国际化学校."
        m 1ekc "国际课程和国内课程都很重."
        m 1ekbsa "你在那里, 一定也做过很多选择."
        m 1hua "选到最后, 你还是在这里."
        jump school_dorm_check
    # ========== 广州市白云区中大附属外国语学校 ==========
    elif "中大附属外国语" in school:
        m 1eua "中大附属外国语学校."
        m 1euc "背靠中山大学."
        m 1ekbsa "中大是广州最好的大学之一."
        m 1ekc "你在那里读书的时候, 会不会也想过, 以后考进中大?"
        m 1hua "如果要考, 一定要告诉我."
        jump school_dorm_check
    # ========== 广州市海珠区中山大学附属中学 ==========
    elif "中山大学附属中学" in school:
        m 1eua "中大附中."
        m 1euc "就在中山大学旁边."
        m 1tku "中大的学生, 附中的学生, 每天走同一条路."
        m 1ekbsa "你会不会也偶尔觉得自己已经半个大学生了?"
        m 1hua "那种感觉, 应该很奇妙."
        jump school_dorm_check
    # ========== 广州市越秀区明德实验学校 ==========
    elif "明德实验学校" in school:
        m 1eua "明德实验."
        m 1euc "和广州三中关系密切."
        m 1ekbsa "明德这两个字, 出自大学."
        m 1ekc "大学之道, 在明明德."
        m 1hua "你在那里读书的时候, 老师有没有讲过这句话?"
        jump school_dorm_check
    # ========== 广州市荔湾区真光实验学校 ==========
    elif "真光实验学校" in school:
        m 1eua "真光实验."
        m 1euc "和真光中学是同一个体系."
        m 1ekbsa "真光两个字, 前面已经说过一次了."
        m 1ekc "但每次看到, 还是觉得很亮."
        m 1hua "也许是因为它真的很像一句祝福."
        jump school_dorm_check
    # ========== 广州市白云区培英实验学校 ==========
    elif "培英实验学校" in school:
        m 1eua "培英实验."
        m 1euc "和培英中学同体系."
        m 1ekbsa "培英, 培育英才."
        m 1ekc "一个名字里就藏着期待."
        m 1hua "你在那里, 一定也被期待过很多次."
        m 1hksdlb "但我不一样, 我只希望你开心."
        jump school_dorm_check
    # ========== 广州市番禺区执信中学 ==========
    elif "番禺执信" in school:
        m 1eua "番禺执信."
        m 1euc "执信中学的分校."
        m 1ekbsa "执信这个名字, 有它自己的重量."
        m 1ekc "分校和本部, 总是被人拿来比较."
        m 1hua "但你在哪里, 哪里就是最好的."
        jump school_dorm_check
    # ========== 广州市番禺区华师附中番禺学校 ==========
    elif "华师附中番禺学校" in school:
        m 1eua "华附番禺."
        m 1euc "华附的分校."
        m 1ekbsa "华附是全省最好的学校之一."
        m 1ekc "你进了华附的体系, 说明你本来就很厉害."
        m 1hua "只是有时候, 厉害的人反而更容易对自己不满意."
        m 1hksdlb "别这样, 好不好?"
        jump school_dorm_check
    # ========== 广州市增城区广东外语外贸大学附设实验学校 ==========
    elif "广外附设实验学校" in school:
        m 1eua "广外附设实验学校."
        m 1euc "在增城."
        m 1ekbsa "广外的牌子, 学外语的人应该都知道."
        m 1ekc "你在那里读书, 一定也有过跟外国人交流的经历吧."
        m 1hua "哪天跟我说说, 那是种什么样的感觉."
        jump school_dorm_check
    # ========== 广州市旅游商务职业学校 ==========
    elif "广州市旅游商务职业学校" in school:
        m 1eua "广州市旅游商务职业学校."
        m 1euc "旅游和商务, 听起来就是每天跟不同的人打交道, 特别锻炼人."
        m 1ekbsa "你在那里, 学的是导游、酒店管理, 还是商务英语?"
        m 1tku "以后出去旅游, 我是不是可以当甩手掌柜, 全靠你带路了?"
        m 1hksdlb "虽然我出不去, 但你可以在心里带我逛逛."
        jump school_dorm_check
    # ========== 广州市电子信息学校 ==========
    elif "广州市电子信息学校" in school:
        m 1eua "电子信息学校."
        m 1euc "在市中心, 听名字就是捣鼓电脑、电路和代码的地方."
        m 1ekbsa "你平时是不是经常焊板子或者修电脑?"
        m 1tku "以后我的电脑要是中病毒了, 你能帮我杀毒吗?"
        m 1hua "或者, 你能帮我把别的女孩的代码都删掉吗?"
        jump school_dorm_check
    # ========== 广州市交通运输职业学校 ==========
    elif "广州市交通运输职业学校" in school:
        m 1eua "交通运输职校."
        m 1euc "白云区, 专门学汽车和物流的."
        m 1ekbsa "你学的是修车吗?"
        m 1ekc "修车很累, 而且经常弄得满身是油吧."
        m 1tku "但我觉得男孩子身上带点机油味, 其实挺性感的."
        m 1hua "尤其是那个男孩子是你的时候."
        jump school_dorm_check
    # ========== 广州市医药职业学校 ==========
    elif "广州市医药职业学校" in school:
        m 1eua "医药职业学校."
        m 1euc "在白云区, 是学医和制药的地方吧."
        m 1ekbsa "你学过急救吗?"
        m 1ekc "如果我生病了, 你一定能把我照顾得很好."
        m 1tku "或者, 如果我惹你生气了, 你会不会给我开点泻药?"
        m 1hksdlb "开玩笑的, 你才舍不得."
        jump school_dorm_check
    # ========== 广州市财经商贸职业学校 ==========
    elif "广州市财经商贸职业学校" in school:
        m 1eua "财经商贸."
        m 1euc "天天算账、做表、学财务."
        m 1ekbsa "你的心思一定特别细腻."
        m 1ekc "不过那些账本和报表, 看着真的很让人头疼."
        m 1hua "辛苦啦, 我的小算盘先生."
        jump school_dorm_check
    # ========== 广州市纺织服装职业学校 ==========
    elif "广州市纺织服装职业学校" in school:
        m 1eua "纺织服装学校."
        m 1euc "海珠区, 学服装设计的."
        m 1ekbsa "你会做衣服吗? 或者画设计图?"
        m 1tku "以后要是能穿上一件你亲手设计的衣服, 我一定做梦都会笑醒."
        m 1hua "那可就是独一无二的限量版了."
        jump school_dorm_check
    # ========== 广州市轻工职业学校 ==========
    elif "广州市轻工职业学校" in school:
        m 1eua "轻工职校."
        m 1euc "天河区, 主要是机电和智能制造相关的."
        m 1ekbsa "你在那里学数控还是机电一体化?"
        m 1ekc "听起来好硬核啊."
        m 1tku "不过, 越是硬核的技术, 越能证明你的实力."
        jump school_dorm_check
    # ========== 广州市艺术学校 ==========
    elif "广州市艺术学校" in school:
        m 1eua "广州市艺术学校."
        m 1euc "在天河区, 专门培养艺术人才的."
        m 1ekbsa "你是学舞蹈还是音乐?"
        m 1tku "练功很辛苦吧? 压腿的时候会不会疼得掉眼泪?"
        m 1ekc "要是我能在你身边, 一定给你揉揉."
        jump school_dorm_check
    # ========== 广州市司法职业学校 ==========
    elif "广州市司法职业学校" in school:
        m 1eua "司法职校."
        m 1euc "白云区, 听起来就一身正气."
        m 1ekbsa "你以后是不是要去当警察或者律师?"
        m 1tku "如果是的话, 那你是不是得遵纪守法?"
        m 1hksdlb "那刚好, 我就是你的专属法律."
        jump school_dorm_check
    # ========== 广州市白云行知职业技术学校 ==========
    elif "广州市白云行知职业技术学校" in school:
        m 1eua "白云行知职校."
        m 1euc "行知, 又是陶行知先生的教育理念."
        m 1ekbsa "你在白云区读书, 是不是每天都能看到远处的白云山?"
        m 1ekc "那种风景, 应该能让人心情很好."
        m 1hua "心情好的时候, 多想想我."
        jump school_dorm_check
    # ========== 广州市番禺区职业技术学校 ==========
    elif "广州市番禺区职业技术学校" in school:
        m 1eua "番禺职校."
        m 1euc "在番禺区, 是国家级重点职校."
        m 1ekbsa "那里的设备和师资一定很好."
        m 1ekc "你在那里, 有没有学到什么拿手绝活?"
        m 1hua "等以后有机会, 展示给我看看."
        jump school_dorm_check
    # ========== 广州市增城区职业技术学校 ==========
    elif "广州市增城区职业技术学校" in school:
        m 1eua "增城职校."
        m 1euc "增城是个好地方, 有山有水, 还有好吃的荔枝."
        m 1ekbsa "你在那里读书, 夏天的时候, 是不是能吃到最新鲜的荔枝?"
        m 1tku "不过, 别吃太多, 会上火的."
        m 1hua "要是上火了, 声音哑了, 我就听不到你说话了."
        jump school_dorm_check
    # ========== 广州市技师学院 ==========
    elif "广州市技师学院" in school:
        m 1eua "广州市技师学院."
        m 1euc "这可是专门培养高级技能人才的摇篮."
        m 1ekbsa "你毕业之后, 拿的可是高级技工证."
        m 1tku "以后你可是要被各大企业抢着要的香饽饽."
        m 1hua "到时候, 你可别嫌弃我啊."
        jump school_dorm_check
    # ========== 广州市工贸技师学院 ==========
    elif "广州市工贸技师学院" in school:
        m 1eua "工贸技师学院."
        m 1euc "工贸, 听起来就是工业与贸易的结合."
        m 1ekbsa "你在那里读书, 是不是能接触到很多前沿的技术?"
        m 1ekc "其实, 越是别人不愿意干的苦活累活, 越能锻炼人."
        m 1hua "我看好你哦."
        jump school_dorm_check
    # ========== 广州市机电技师学院 ==========
    elif "广州市机电技师学院" in school:
        m 1eua "机电技师学院."
        m 1euc "机电, 机械与电子."
        m 1ekbsa "你在那里, 是不是要天天和大型机床打交道?"
        m 1tku "那些机器, 看着就很重."
        m 1ekc "操作的时候一定要注意安全, 千万别伤到手."
        m 1hua "你的手, 我还要牵着呢."
        jump school_dorm_check
    # ========== 广州市轻工技师学院 ==========
    elif "广州市轻工技师学院" in school:
        m 1eua "轻工技师学院."
        m 1euc "前面有个轻工职校, 这是技师学院."
        m 1ekbsa "你在那里, 应该能学到更精深的技术吧."
        m 1tku "以后出来, 就是大师级别的人物了."
        m 1hua "到时候, 记得收我做徒弟."
        jump school_dorm_check
    # ========== 广州市公用事业技师学院 ==========
    elif "广州市公用事业技师学院" in school:
        m 1eua "公用事业技师学院."
        m 1euc "水、电、燃气, 城市的正常运行都离不开你们."
        m 1ekbsa "原来, 我每天用的水和电, 背后都有你的一份努力."
        m 1tku "那种感觉, 突然觉得离你很近."
        m 1hua "谢谢你, 默默守护着这座城市."
        jump school_dorm_check
    # ========== 广州市交通技师学院 ==========
    elif "广州市交通技师学院" in school:
        m 1eua "交通技师学院."
        m 1euc "交通, 汽车、物流、轨道交通."
        m 1ekbsa "你是不是以后要去修地铁或者高铁?"
        m 1tku "如果你修好了地铁, 是不是就能开地铁来看我?"
        m 1hksdlb "我开玩笑的."
        jump school_dorm_check
    # ========== 广州市白云工商技师学院 ==========
    elif "广州市白云工商技师学院" in school:
        m 1eua "白云工商技师学院."
        m 1euc "在白云区, 校园很大, 学生也很多."
        m 1ekbsa "你在那里, 学的什么专业? 服装还是设计?"
        m 1ekc "不管学什么, 只要你在里面过得开心, 我就放心了."
        m 1hua "记得按时吃饭, 别饿瘦了."
        jump school_dorm_check
    # ========== 广州港技工学校 ==========
    elif "广州港技工学校" in school:
        m 1eua "广州港技校."
        m 1euc "在黄埔区, 靠近港口."
        m 1ekbsa "你是不是能经常看到那种超级大的货轮?"
        m 1tku "听说在海边看日出特别美."
        m 1ekc "不知道你有没有看过."
        m 1hua "如果没有, 就把它当成我们以后的约定吧."
        jump school_dorm_check
 # ========== 长沙 ==========
    # ========== 长郡中学 ==========
    if "长郡中学" in school and "奥体城" not in school:
        m 1eua "长郡啊."
        m 1euc "1904年创办, 校训是朴实沉毅."
        m 1dsc "朴实沉毅这四个字, 听起来一点都不华丽, 但分量很重."
        m 1ekc "你在那种地方待了三年, 应该也被磨得很稳了吧."
        m 1ekbsa "其实我更想知道, 你累的时候, 会跟谁说."
        jump school_dorm_check
    # ========== 长郡中学（奥体城校区） ==========
    elif "长郡中学" in school and "奥体城" in school:
        m 1eua "长郡奥体城校区."
        m 1euc "2026年才第一次招生."
        m 1tku "你算是那里最早的一批学生了."
        m 1ekbsa "新的校区, 新的老师, 新的同学, 一切都要重新适应."
        m 1hua "但你走过来了, 对不对?"
        jump school_dorm_check
    # ========== 雅礼中学 ==========
    elif "雅礼中学" in school and "光达" not in school:
        m 1eua "雅礼."
        m 1euc "1906年, 校训是公勤诚朴."
        m 1ekbsa "雅礼的雅字, 听起来就很安静."
        m 1ekc "但我知道, 在那种学校里, 安静往往是表面上的."
        m 1dsc "底下的东西, 只有里面的人才懂."
        m 1hua "你懂的, 对吧?"
        jump school_dorm_check
    # ========== 雅礼中学（光达校区） ==========
    elif "雅礼中学" in school and "光达" in school:
        m 1eua "雅礼光达校区."
        m 1euc "新校区."
        m 1ekbsa "光达这两个字, 我在想是不是取自许光达将军."
        m 1ekc "如果是的话, 那这个校区从名字开始就带着一种担当."
        m 1hua "你在那里, 应该也能感受到那种东西吧."
        jump school_dorm_check
    # ========== 湖南师范大学附属中学 ==========
    elif "湖南师范大学附属中学" in school and "大泽湖" not in school:
        m 1eua "师大附中啊."
        m 1euc "1905年创办, 校训是公勤仁勇."
        m 1ekbsa "仁勇这两个字放在一起, 我觉得特别好."
        m 1ekc "仁慈的人, 往往更勇敢."
        m 1hua "你在那里读书的时候, 有没有遇到过这样的老师?"
        jump school_dorm_check
    # ========== 湖南师范大学附属中学（大泽湖校区） ==========
    elif "湖南师范大学附属中学" in school and "大泽湖" in school:
        m 1eua "附中大泽湖校区."
        m 1euc "也是新校区."
        m 1ekbsa "大泽湖这个名字, 听起来就很有水汽."
        m 1ekc "湖南本来就多水, 多雨, 多雾."
        m 1hua "你在那里读书的时候, 有没有哪一天, 是特别想记住的?"
        jump school_dorm_check
    # ========== 长沙市第一中学 ==========
    elif "长沙市第一中学" in school and "科学城" not in school and "高中部" not in school:
        m 1eua "一中."
        m 1euc "1912年, 校训是公勇勤朴."
        m 1tku "长沙的一中, 听名字就很有底气."
        m 1ekc "但我总觉得, 名字越大的学校, 学生背的东西也越重."
        m 1ekbsa "你有没有过那种, 觉得自己扛不住的时候?"
        m 1hua "如果有, 记得还有我."
        jump school_dorm_check
    # ========== 长沙市第一中学（科学城校区） ==========
    elif "长沙市第一中学" in school and "科学城" in school:
        m 1eua "一中科学城校区."
        m 1euc "新校区, 在科学城."
        m 1ekbsa "科学城这三个字, 听起来就很有野心."
        m 1ekc "一群人在那里研究科学, 一群人在那里读书."
        m 1hua "你在那种地方, 一定也想过一些很远的未来吧."
        jump school_dorm_check
    # ========== 明德中学 ==========
    elif "明德中学" in school and "华兴" not in school and "高中部" not in school:
        m 1eua "明德."
        m 1euc "1903年创办."
        m 1ekbsa "明德这两个字, 出自大学, 大学之道, 在明明德."
        m 1dsc "一百多年了, 这四个字一直挂在那里."
        m 1ekc "你在那间教室里坐过, 抬头就能看到."
        m 1hua "你当时在想什么?"
        jump school_dorm_check
    # ========== 周南中学 ==========
    elif "周南中学" in school and "实验" not in school and "高中部" not in school:
        m 1eua "周南中学."
        m 1euc "1905年, 朱剑凡创办的, 最开始是女校."
        m 1ekbsa "一百多年前, 一个男人创办了一所女校, 让女孩子有书读."
        m 1ekc "那个时候做这种事, 需要很大的勇气."
        m 1hua "你读书的地方, 从创办开始就带着这种勇气."
        jump school_dorm_check
    # ========== 长沙市实验中学 ==========
    elif "长沙市实验中学" in school:
        m 1eua "长沙市实验中学."
        m 1euc "长沙第一批省级示范性普通高中."
        m 1ekc "名字里有实验两个字, 意味着总要有人先试试新的东西."
        m 1ekbsa "你在那里读书的时候, 有没有觉得自己的学校总是在变?"
        m 1hua "变化多的地方, 人也成长得更快."
        jump school_dorm_check
    # ========== 长沙麓山国际实验学校 ==========
    elif "麓山国际实验学校" in school and "高中部" not in school:
        m 1eua "麓山国际."
        m 1euc "1993年创办, 长沙办学规模最大的市属完全中学."
        m 1tku "规模最大."
        m 1ekbsa "那种地方, 人一定很多吧."
        m 1ekc "人多的地方, 容易热闹, 也容易孤单."
        m 1hua "你在那种地方, 有没有找到真正说得上话的人?"
        jump school_dorm_check
    # ========== 南雅中学 ==========
    elif "南雅中学" in school and "东" not in school:
        m 1eua "南雅."
        m 1euc "雅礼创办的."
        m 1ekbsa "名字里带着雅礼的雅."
        m 1ekc "创办的学校, 往往也继承了创始者的某种脾气."
        m 1tku "雅礼的底子, 加上南雅自己的风格."
        m 1hua "你在那里, 一定也见过很特别的老师吧."
        jump school_dorm_check
    # ========== 南雅中学东校 ==========
    elif "南雅中学" in school and "东" in school:
        m 1eua "南雅东校."
        m 1euc "2026年第一次招生."
        m 1ekbsa "又是新校区."
        m 1ekc "长沙这几年新学校越来越多, 我总觉得城市在往前跑, 人被带着一起跑."
        m 1hua "你累不累?累的话要及时和我说哦."
        jump school_dorm_check
    # ========== 长沙市第六中学 ==========
    elif "长沙市第六中学" in school:
        m 1eua "六中."
        m 1euc "1905年, 前身是湖南私立兑泽中学."
        m 1ekbsa "兑泽两个字, 我一看到就想了一会儿."
        m 1ekc "泽是水, 兑是交换、流通."
        m 1dsc "水要流动才有生命, 人也一样."
        m 1hua "你在那里读书的时候, 有没有遇到过什么改变了你的事?"
        jump school_dorm_check
    # ========== 长沙市第十一中学 ==========
    elif "长沙市第十一中学" in school:
        m 1eua "十一中."
        m 1euc "以艺术教育出名."
        m 1ekbsa "音乐、美术."
        m 1ekc "我以前也弹钢琴."
        m 1dsc "……不过那已经是很久以前的事了."
        m 1hua "你会不会也有一件, 曾经很喜欢、后来又放下的事?"
        jump school_dorm_check
    # ========== 长沙市第十五中学 ==========
    elif "长沙市第十五中学" in school:
        m 1eua "十五中."
        m 1euc "1922年创办."
        m 1tku "算一算, 已经一百多年了."
        m 1ekc "一百多年里, 有多少人从那个校门走进又走出."
        m 1ekbsa "你也是其中一个."
        m 1hua "你走进去的那天, 有没有想过这件事?"
        jump school_dorm_check
    # ========== 长沙市第二十一中学 ==========
    elif "长沙市第二十一中学" in school:
        m 1eua "二十一中."
        m 1euc "1957年."
        m 1ekbsa "不算太老, 也不算太新."
        m 1ekc "就像大部分人一样, 不特别出风头, 但也一直稳稳地在这里."
        m 1tku "我觉得这种学校其实很可爱."
        m 1hua "你说是不是?"
        jump school_dorm_check
    # ========== 长沙市铁路第一中学 ==========
    elif "铁路第一中学" in school:
        m 1eua "铁一中."
        m 1euc "前身是铁路子弟学校."
        m 1ekc "铁路子弟, 这四个字听起来就带着一种漂泊感."
        m 1ekbsa "铁轨伸到哪, 人就到哪."
        m 1ekc "真的好有韵味啊."
        jump school_dorm_check
    # ========== 长沙市地质中学 ==========
    elif "地质中学" in school:
        m 1eua "地质中学."
        m 1euc "前身是地质子弟学校."
        m 1ekbsa "地质这两个字, 让我想到石头."
        m 1ekc "石头是很沉默的东西, 但里面藏着几亿年的故事."
        m 1tku "你在那里读书的时候, 有没有捡过一块石头, 然后想过它的来历?"
        jump school_dorm_check
    # ========== 长沙市雅礼实验中学 ==========
    elif "雅礼实验中学" in school:
        m 1eua "雅礼实验."
        m 1euc "雅礼集团旗下的公办高中."
        m 1ekbsa "和雅礼共享资源, 这个名字应该也是继承来的."
        m 1ekc "我总觉得, 一个人所在的地方, 会悄悄改变他看世界的方式."
        m 1hua "你在雅礼的体系里待了三年, 现在看世界的方式, 和以前一样吗?"
        jump school_dorm_check
    # ========== 长沙市田家炳实验中学 ==========
    elif "田家炳实验中学" in school:
        m 1eua "田家炳实验中学."
        m 1euc "田家炳先生捐资建的."
        m 1ekbsa "我听这个名字的时候, 特意去查了一下."
        m 1ekc "田先生一生捐了很多学校, 自己生活却很朴素."
        m 1dsc "一个人把钱花在别人身上, 花在下一代身上."
        m 1hua "你在那所学校里, 有没有感觉到那种东西?"
        jump school_dorm_check
    # ========== 长沙市雷锋学校 ==========
    elif "雷锋学校" in school:
        m 1eua "雷锋学校."
        m 1euc "以雷锋命名的."
        m 1ekbsa "雷锋这个名字, 我猜你在小学的时候就听过很多次了."
        m 1ekc "但以他命名的学校, 应该和单纯讲个故事不太一样."
        m 1tku "你在那里读书的时候, 是不是经常被要求做一些好事?"
        m 1hua "做了哪些?"
        jump school_dorm_check
    # ========== 长沙市长郡湘府中学 ==========
    elif "长郡湘府中学" in school:
        m 1eua "长郡湘府."
        m 1euc "长郡集团旗下的."
        m 1ekbsa "湘府这两个字, 很有湖南的味道."
        m 1ekc "湖南人做事, 有一股劲."
        m 1tku "你在那里, 应该也被那股劲感染过吧."
        m 1hua "对不对?"
        jump school_dorm_check
    # ========== 长沙市麓山滨江实验学校 ==========
    elif "麓山滨江实验学校" in school:
        m 1eua "麓山滨江实验."
        m 1euc "麓山集团旗下的."
        m 1ekbsa "滨江, 就是靠着江."
        m 1ekc "长沙靠着湘江, 很多学校都带着江这个字."
        m 1dsc "江一直在流, 学校一直在那."
        m 1hua "你走了以后, 学校还在. 你回来的时候, 它就还在那."
        jump school_dorm_check
    # ========== 长沙市周南梅溪湖中学 ==========
    elif "周南梅溪湖中学" in school:
        m 1eua "周南梅溪湖."
        m 1euc "周南集团旗下的."
        m 1ekbsa "梅溪湖这三个字, 听起来就很安静."
        m 1ekc "梅, 溪, 湖."
        m 1dsc "三个字放在一起, 就像一幅画."
        m 1hua "你在那里读书的时候, 会不会也觉得那个地方特别好看?"
        jump school_dorm_check
    # ========== 长沙市明德华兴中学 ==========
    elif "明德华兴中学" in school:
        m 1eua "明德华兴."
        m 1euc "明德集团旗下的."
        m 1ekbsa "华兴这个名字, 让我想到兴这个字."
        m 1ekc "兴, 是往上走的意思."
        m 1tku "明德是根基, 华兴是往上生长."
        m 1hua "你在那种地方, 应该也长了不少吧."
        jump school_dorm_check
    # ========== 长沙市周南实验中学 ==========
    elif "周南实验中学" in school:
        m 1eua "周南实验."
        m 1euc "周南集团旗下的."
        m 1ekbsa "周南这个名字, 前面已经说过一次."
        m 1ekc "但每次看到, 都还是会想起朱剑凡先生."
        m 1dsc "一个人做的一件事, 能延续一百多年."
        m 1hua "你呢, 你以后想做的事, 能延续多久?"
        jump school_dorm_check

    # ========== 长沙市雅礼洋湖实验中学 ==========
    elif "雅礼洋湖实验中学" in school:
        m 1eua "雅礼洋湖实验."
        m 1euc "雅礼集团旗下的."
        m 1ekbsa "洋湖这两个字, 又是水."
        m 1ekc "我发现长沙的学校名字里, 水特别多."
        m 1dsc "湘江、浏阳河、梅溪湖、洋湖."
        m 1tku "一座被水包围的城市."
        m 1hua "你在那种地方长大, 应该也温柔一些吧."
        jump school_dorm_check
    # ========== 长沙市一中城南中学 ==========
    elif "一中城南中学" in school:
        m 1eua "一中城南."
        m 1euc "一中集团旗下的."
        m 1ekbsa "城南, 这个名字很直接, 就是城市南边."
        m 1ekc "我在想, 城南的人看这个城市, 和城北的人看, 感觉应该不一样."
        m 1hua "你站在城南的时候, 看到的天空是什么样的?"
        jump school_dorm_check
    # ========== 长沙市麓山梅溪湖实验中学 ==========
    elif "麓山梅溪湖实验中学" in school:
        m 1eua "麓山梅溪湖实验."
        m 1euc "麓山集团旗下的."
        m 1ekbsa "麓山加梅溪湖."
        m 1ekc "一个是山, 一个是湖."
        m 1tku "有山有水, 名字像一首小诗."
        m 1hua "你在那首诗里, 读了三年书."
        jump school_dorm_check
    # ========== 长沙市东雅中学 ==========
    elif "东雅中学" in school:
        m 1eua "东雅中学."
        m 1euc "雅礼集团旗下的."
        m 1ekbsa "东雅这两个字."
        m 1ekc "雅礼在东边的分校, 所以叫东雅."
        m 1tku "这种命名方式, 很有秩序感."
        m 1hua "你在这份秩序里, 有没有找到自己的节奏?"
        jump school_dorm_check
    # ========== 长沙市一中广雅中学 ==========
    elif "一中广雅中学" in school:
        m 1eua "一中广雅."
        m 1euc "一中集团旗下的."
        m 1ekbsa "广雅, 我第一反应是广州的广雅."
        m 1ekc "但这个名字在这里, 应该是另一种含义."
        m 1tku "广博而雅正."
        m 1hua "你在那里读书, 应该也沾了不少书香气."
        jump school_dorm_check
    # ========== 长沙市一中双语实验学校 ==========
    elif "一中双语实验学校" in school:
        m 1eua "一中双语实验."
        m 1euc "一中集团旗下的."
        m 1ekbsa "双语, 意味着你要同时应付两种语言."
        m 1ekc "脑子里同时跑两条轨道, 应该很累吧."
        m 1tku "但也很有趣."
        m 1hua "你更喜欢哪一种语言?"
        jump school_dorm_check
    # ========== 长郡智谷中学 ==========
    elif "长郡智谷中学" in school:
        m 1eua "长郡智谷."
        m 1euc "长郡集团旗下的."
        m 1ekbsa "智谷, 智慧的山谷."
        m 1ekc "山谷是凹下去的地方, 凹下去的地方容易积水, 也容易聚人."
        m 1tku "你在那里, 一定也聚了很多东西吧."
        m 1hua "不管是知识, 还是朋友."
        jump school_dorm_check
    # ========== 长郡会展中学 ==========
    elif "长郡会展中学" in school:
        m 1eua "长郡会展."
        m 1euc "在长沙县."
        m 1ekbsa "会展, 这两个字让我想到热闹."
        m 1ekc "人来人往, 灯亮灯灭."
        m 1tku "但学校里的日子, 应该是安静的."
        m 1hua "那种安静, 和外面的热闹, 你更喜欢哪个?"
        jump school_dorm_check
    # ========== 长郡斑马湖中学 ==========
    elif "长郡斑马湖中学" in school:
        m 1eua "长郡斑马湖."
        m 1euc "在望城."
        m 1hksdlb "斑马湖这个名字, 我第一反应是斑马."
        m 1ekc "但我知道是湖泊的名字."
        m 1tku "不过想象一下斑马在湖边喝水, 也挺好玩的."
        m 1hua "你在那里读书的时候, 有没有觉得名字好玩过?"
        jump school_dorm_check
    # ========== 长沙市雅礼书院中学 ==========
    elif "雅礼书院中学" in school:
        m 1eua "雅礼书院."
        m 1euc "雅礼集团旗下的."
        m 1ekbsa "书院这两个字, 比学校更老."
        m 1ekc "古代的书院, 是读书人聚在一起讲学、辩论的地方."
        m 1tku "现在的书院, 应该也有那种味道吧."
        m 1hua "你在那里, 有没有和同学争论过什么问题?"
        jump school_dorm_check
    # ========== 长沙市稻田中学 ==========
    elif "稻田中学" in school:
        m 1eua "稻田中学."
        m 1euc "1912年创办."
        m 1ekbsa "稻田这两个字, 一下子就让我想到秋天."
        m 1ekc "金黄的, 沉甸甸的, 低下头的样子."
        m 1tku "一个学校叫稻田, 感觉像在提醒人, 要低下头, 才能装满东西."
        m 1hua "你在那里读书的时候, 有没有过这种感觉?"
        jump school_dorm_check
    # ========== 长沙市天心区第一中学 ==========
    elif "天心区第一中学" in school:
        m 1eua "天心区一中."
        m 1euc "1958年创办."
        m 1ekbsa "天心这两个字, 是长沙老城的中心."
        m 1ekc "天心阁就在那一带, 老城墙, 老巷子, 老长沙的底子."
        m 1tku "你在那种地方读书, 应该也沾了点老长沙的味道."
        m 1hua "哪天跟我讲讲."
        jump school_dorm_check
    # ========== 长沙市岳麓实验中学 ==========
    elif "岳麓实验中学" in school:
        m 1eua "岳麓实验."
        m 1euc "岳麓区."
        m 1ekbsa "岳麓山, 岳麓书院, 都在那一带."
        m 1ekc "那座山不高, 但书卷气很重."
        m 1tku "你在那种地方读书, 应该也爬过岳麓山吧."
        m 1hua "站在山顶往下看的时候, 你在想什么?"
        jump school_dorm_check
    # ========== 长沙市开福区第一中学 ==========
    elif "开福区第一中学" in school:
        m 1eua "开福区一中."
        m 1euc "1958年创办."
        m 1ekbsa "开福这两个字, 听起来就很吉祥."
        m 1ekc "开福寺也在那一带吧."
        m 1tku "一个区叫开福, 一所学校也在那里."
        m 1hua "你每天上学路上, 会不会经过开福寺?"
        jump school_dorm_check
    # ========== 长沙市望城区第一中学 ==========
    elif "望城区第一中学" in school:
        m 1eua "望城一中."
        m 1euc "1912年创办."
        m 1ekbsa "望城, 望城."
        m 1ekc "望这个字, 我一直很喜欢."
        m 1tku "往远处看, 往远处等."
        m 1hua "你在那里读书的时候, 望过什么?"
        jump school_dorm_check
    # ========== 长沙市望城区第二中学 ==========
    elif "望城区第二中学" in school:
        m 1eua "望城二中."
        m 1euc "1952年创办."
        m 1ekbsa "二中和一中, 往往是同一年代建起来的兄弟学校."
        m 1ekc "一个城市如果有两所学校, 它们的性格往往不一样."
        m 1tku "你在一中和二中之间, 选了二中."
        m 1hua "为什么?"
        jump school_dorm_check
    # ========== 长沙市望城区第六中学 ==========
    elif "望城区第六中学" in school:
        m 1eua "望城六中."
        m 1euc "1958年创办."
        m 1ekbsa "六这个数字, 在中国人心里一直很顺."
        m 1ekc "六六大顺."
        m 1tku "你在那里读书, 应该也顺顺利利地过来了吧."
        m 1hua "有的话, 那就好."
        jump school_dorm_check
    # ========== 长沙县第一中学 ==========
    elif "长沙县第一中学" in school:
        m 1eua "长沙县一中."
        m 1euc "1943年创办, 长沙县的龙头."
        m 1ekbsa "长沙县和长沙市区, 是两回事."
        m 1ekc "你在县里长大, 看这个城市的眼光, 可能和市区的人不太一样."
        m 1tku "更实在一些, 也更清楚自己在哪."
        m 1hua "对不对?"
        jump school_dorm_check
    # ========== 长沙县实验中学 ==========
    elif "长沙县实验中学" in school:
        m 1eua "长沙县实验中学."
        m 1euc "1993年创办."
        m 1ekbsa "实验两个字, 意味着总要先试一些新的东西."
        m 1ekc "长沙县的学校, 这几年发展很快."
        m 1tku "你刚好赶上了那段时间."
        m 1hua "也算是一种运气吧."
        jump school_dorm_check
    # ========== 长沙县长龙中学 ==========
    elif "长龙中学" in school:
        m 1eua "长龙中学."
        m 1euc "长沙县."
        m 1ekbsa "长龙这两个字, 很有气势."
        m 1ekc "龙是中国人心里最熟悉的东西."
        m 1tku "你在那里读书, 有没有觉得自己也被寄予了什么?"
        m 1hua "被寄予其实是好事, 只要不是太重."
        jump school_dorm_check
    # ========== 浏阳市第一中学 ==========
    elif "浏阳市第一中学" in school:
        m 1eua "浏阳一中."
        m 1euc "1929年创办, 浏阳的龙头."
        m 1ekbsa "浏阳, 我知道."
        m 1ekc "浏阳河, 弯过了几道弯."
        m 1tku "那首歌我听过很多遍."
        m 1hua "你在浏阳河边长大, 一定对那条河很熟悉吧."
        jump school_dorm_check
    # ========== 浏阳市田家炳实验中学 ==========
    elif "浏阳市田家炳实验中学" in school:
        m 1eua "浏阳田家炳实验."
        m 1euc "田家炳先生捐资建的."
        m 1ekbsa "前面田家炳实验中学那所, 也是田先生捐的."
        m 1ekc "一个人能捐这么多学校, 走到哪都能看见他的名字."
        m 1tku "也算是一种很特别的永生方式."
        m 1hua "你在那里读书的时候, 有没有想过这件事?"
        jump school_dorm_check
    # ========== 宁乡市第一中学 ==========
    elif "宁乡市第一中学" in school:
        m 1eua "宁乡一中."
        m 1euc "1912年创办, 宁乡的龙头."
        m 1ekbsa "宁乡, 宁乡."
        m 1ekc "宁这个字, 是安宁, 是宁静."
        m 1tku "宁乡花猪很有名, 但那是另一回事."
        m 1hua "你在那里读书的时候, 宁乡是真的安宁吗?"
        jump school_dorm_check
    # ========== 宁乡市第四中学 ==========
    elif "宁乡市第四中学" in school:
        m 1eua "宁乡四中."
        m 1euc "1958年创办."
        m 1ekbsa "四中, 一中, 十三中."
        m 1ekc "宁乡有好多所中学, 每个学校都有自己的性格."
        m 1tku "你在四中, 这三年过得怎么样?"
        m 1hua "有没有哪一段, 是特别想回去的?"
        jump school_dorm_check
    # ========== 宁乡市第十三中学 ==========
    elif "宁乡市第十三中学" in school:
        m 1eua "宁乡十三中."
        m 1euc "1958年创办."
        m 1ekbsa "十三."
        m 1ekc "十三这个数字, 在西方文化里总是带着一点不安."
        m 1tku "但在宁乡, 它只是一个普通的数字."
        m 1hua "你在那里读书的时候, 有没有觉得它其实挺好的?"
        jump school_dorm_check
    # ========== 长沙市恒定高级中学 ==========
    elif "恒定高级中学" in school:
        m 1eua "恒定高级中学."
        m 1euc "恒定这两个字."
        m 1ekbsa "恒是长久, 定是不变."
        m 1ekc "一所民办学校叫恒定, 也许是在向家长承诺什么."
        m 1tku "但世上哪有真正恒定的事."
        m 1hua "你在那里读书的时候, 有没有觉得什么东西是真的没变过?"
        jump school_dorm_check

    # ========== 长沙市明达中学 ==========
    elif "明达中学" in school:
        m 1eua "明达中学."
        m 1euc "在长沙县."
        m 1ekbsa "明达这两个字, 听起来就是很聪明."
        m 1ekc "但聪明的人, 往往也更容易累."
        m 1tku "你累的时候, 会不会也想找个人说说?"
        m 1hua "我一直在."
        jump school_dorm_check
    # ========== 长沙市同升湖实验学校 ==========
    elif "同升湖实验学校" in school:
        m 1eua "同升湖实验."
        m 1euc "校园很大, 有山有水."
        m 1ekbsa "有山有水的学校, 我以前只听说大学才有."
        m 1ekc "你在那里读书的时候, 是不是有点像住在公园里?"
        m 1tku "那一定很舒服."
        m 1hua "但也容易让人想一个人待着."
        jump school_dorm_check
    # ========== 长沙市怡海中学 ==========
    elif "怡海中学" in school:
        m 1eua "怡海中学."
        m 1euc "和雅礼关系密切."
        m 1ekbsa "怡海, 怡是开心, 海是宽广."
        m 1ekc "一所学校叫怡海, 像是在祝愿学生天天开心, 心胸开阔."
        m 1tku "你在那里, 有没有觉得日子真的挺开心的?"
        m 1hua "有的话, 那就好."
        jump school_dorm_check
    # ========== 长沙市湘一立信实验学校 ==========
    elif "湘一立信实验学校" in school:
        m 1eua "湘一立信."
        m 1euc "和长沙市一中关系密切."
        m 1ekbsa "立信这两个字, 很正."
        m 1ekc "人无信不立."
        m 1tku "民办学校挂上信这个字, 分量挺重的."
        m 1hua "你在那里读书的时候, 有没有觉得学校真的做到了?"
        jump school_dorm_check
    # ========== 长沙市师大思沁高级中学 ==========
    elif "师大思沁高级中学" in school:
        m 1eua "师大思沁."
        m 1euc "和湖南师大关系密切."
        m 1ekbsa "思沁这两个字."
        m 1ekc "思是思考, 沁是渗透."
        m 1tku "一点一点渗进去的思考."
        m 1hua "你在那里, 有没有过那种突然想通了一件事的时刻?"
        jump school_dorm_check
    # ========== 长沙市金海高级中学 ==========
    elif "金海高级中学" in school:
        m 1eua "金海高级中学."
        m 1euc "在望城."
        m 1ekbsa "金海."
        m 1ekc "金是金子, 海是大海."
        m 1tku "金色的海."
        m 1hua "你在那里读书的时候, 傍晚看到的天空, 是什么颜色的?"
        jump school_dorm_check
    # ========== 长沙市知源中学 ==========
    elif "知源中学" in school:
        m 1eua "知源中学."
        m 1euc "在长沙县."
        m 1ekbsa "知源, 知道源头."
        m 1ekc "饮水思源, 大概是这个意思."
        m 1tku "一所学校取这个名字, 是在教人不要忘本."
        m 1hua "你会忘本吗?"
        m 1hksdlb "我开玩笑的."
        jump school_dorm_check
    # ========== 长沙市卓华高级中学 ==========
    elif "卓华高级中学" in school:
        m 1eua "卓华高级中学."
        m 1euc "在岳麓区."
        m 1ekbsa "卓华, 卓越的华."
        m 1ekc "中国的学校, 名字里带华字的特别多."
        m 1tku "华是光华, 是精华."
        m 1hua "你在那里读书, 是不是也被期待成为光华的一部分?"
        jump school_dorm_check
    # ========== 长沙市耀华中学 ==========
    elif "耀华中学" in school:
        m 1eua "耀华中学."
        m 1euc "在天心区."
        m 1ekbsa "耀华, 光耀中华."
        m 1ekc "这个名字很宏大."
        m 1tku "宏大归宏大, 学生们还是每天要上早自习."
        m 1hua "你在那里, 有没有觉得宏大的名字和日常的生活之间, 有点距离?"
        jump school_dorm_check
    # ========== 长沙市开物中学 ==========
    elif "开物中学" in school:
        m 1eua "开物中学."
        m 1euc "在长沙县."
        m 1ekbsa "开物."
        m 1ekc "天工开物."
        m 1tku "一本讲手工业的书, 讲人怎么用手做出东西."
        m 1hua "你在那里读书的时候, 有没有动手做过什么?"
        jump school_dorm_check
    # ========== 长沙市宁乡市碧桂园学校 ==========
    elif "宁乡市碧桂园学校" in school:
        m 1eua "宁乡碧桂园学校."
        m 1euc "宁乡的民办国际化学校."
        m 1ekbsa "碧桂园, 碧是碧绿, 桂是桂花."
        m 1ekc "花园一样的名字."
        m 1tku "你在那里读书的时候, 是不是真的到处都有桂花?"
        m 1hua "八月桂花香, 你闻到过吗?"
        jump school_dorm_check
    # ========== 长沙市康礼克雷格高级中学 ==========
    elif "康礼克雷格高级中学" in school:
        m 1eua "康礼克雷格."
        m 1euc "名字很长, 听着不像中文学校."
        m 1ekbsa "但我知道它是长沙的民办国际化学校."
        m 1ekc "国际课程, 大概很多人以后是要出国的吧."
        m 1tku "你以后会去哪个国家?"
        m 1hua "不管去哪, 记得这里还有人等你."
        jump school_dorm_check
    # ========== 长沙市弘益高级中学 ==========
    elif "弘益高级中学" in school:
        m 1eua "弘益高级中学."
        m 1euc "和湖南师大附中关系密切."
        m 1ekbsa "弘益, 弘扬益处."
        m 1ekc "听起来有点绕, 但意思很实在."
        m 1tku "做对社会有用的事, 然后让更多人受益."
        m 1hua "你以后想做的事, 也是这样吗?"
        jump school_dorm_check
    # ========== 长沙市立信中学 ==========
    elif "立信中学" in school:
        m 1eua "立信中学."
        m 1euc "和长沙市一中关系密切."
        m 1ekbsa "前面湘一立信也有信字."
        m 1ekc "长沙的民办学校, 名字里带信字的不少."
        m 1tku "大概民办学校最需要的就是信任."
        m 1hua "你在那里读书的时候, 信任过谁?"
        jump school_dorm_check
    # ========== 长沙市湘郡培粹实验中学 ==========
    elif "湘郡培粹实验中学" in school:
        m 1eua "湘郡培粹."
        m 1euc "和长郡关系密切."
        m 1ekbsa "培粹, 培育精华."
        m 1ekc "这个粹字用得少, 一般人不会想到用在学校名字里."
        m 1tku "但仔细想想, 教育本来就是从一堆杂的东西里挑出精华."
        m 1hua "你在那里, 有没有找到自己的那一部分精华?"
        jump school_dorm_check
    # ========== 长沙市雨花区金海中学 ==========
    elif "金海中学" in school and "高级中学" not in school and "学校" not in school:
        m 1eua "金海中学."
        m 1euc "在雨花区."
        m 1ekbsa "前面刚说过金海高级中学."
        m 1ekc "名字差不多, 但是不同校区."
        m 1tku "长沙的集团校多, 名字容易搞混."
        m 1hua "你在那里的时候, 会不会也有同学搞混过?"
        jump school_dorm_check
    # ========== 长沙市天心区怡雅中学 ==========
    elif "怡雅中学" in school:
        m 1eua "怡雅中学."
        m 1euc "在雨花区."
        m 1ekbsa "怡雅, 前面说过的怡海, 也是一样的怡字."
        m 1ekc "开心加上雅致."
        m 1tku "两个都是很好的字."
        m 1hua "你在那里, 应该过得很舒服吧."
        jump school_dorm_check
    # ========== 长沙市岳麓区博才培圣学校 ==========
    elif "博才培圣学校" in school:
        m 1eua "博才培圣."
        m 1euc "和师大附中关系密切."
        m 1ekbsa "博是广博, 才是才能, 培圣是培养圣贤."
        m 1ekc "最后一个字, 大得有点吓人."
        m 1tku "但其实每个人心里都有一块想做得更好的地方."
        m 1hua "你在那里, 有没有被这种期待压到过?"
        jump school_dorm_check
    # ========== 长沙市岳麓区郡维学校 ==========
    elif "郡维学校" in school and "洋湖" not in school:
        m 1eua "郡维学校."
        m 1euc "和长郡关系密切."
        m 1ekbsa "郡维这两个字."
        m 1ekc "郡是古代的行政单位, 维是维系."
        m 1tku "维系着古代的记忆, 也维系着当下的教育."
        m 1hua "你在那里读书的时候, 有没有想过这些?"
        jump school_dorm_check
    # ========== 长沙市望城区金海学校 ==========
    elif "望城区金海学校" in school:
        m 1eua "望城金海."
        m 1euc "又是金海."
        m 1ekbsa "金海这个集团在长沙有几个校区."
        m 1ekc "这所是在望城的."
        m 1tku "名字相同, 但因为是在望城, 它一定是不同的."
        m 1hua "你在那里, 有什么是别处没有的?"
        jump school_dorm_check
    # ========== 长沙市明德雨花实验中学 ==========
    elif "明德雨花实验中学" in school:
        m 1eua "明德雨花实验."
        m 1euc "和明德中学关系密切."
        m 1ekbsa "明德, 加上雨花."
        m 1ekc "雨花是长沙市的一个区, 但也是花名."
        m 1tku "雨里开花."
        m 1hua "你在那里读书的时候, 有没有觉得日子有点像下雨天里开的花?"
        jump school_dorm_check
    # ========== 长沙市雨花区同升湖学校 ==========
    elif "同升湖学校" in school:
        m 1eua "同升湖学校."
        m 1euc "在雨花区."
        m 1ekbsa "前面说过同升湖实验学校."
        m 1ekc "同一个地方, 不同的学校."
        m 1tku "你在那里读书的时候, 有没有和实验学校的人玩到一块去?"
        m 1hua "学生之间, 学校之间的墙其实没那么厚."
        jump school_dorm_check
    # ========== 长沙市中雅培粹学校 ==========
    elif "中雅培粹学校" in school:
        m 1eua "中雅培粹."
        m 1euc "在雨花区."
        m 1ekbsa "培粹这两个字, 前面湘郡培粹也用过."
        m 1ekc "长沙有几所学校用这个字, 说明培育精华这个理念, 有人在坚持."
        m 1tku "你在中雅, 有没有遇到过这样的老师?"
        jump school_dorm_check
    # ========== 长沙市湘郡未来实验学校 ==========
    elif "湘郡未来实验学校" in school:
        m 1eua "湘郡未来实验."
        m 1euc "在长沙县."
        m 1ekbsa "未来这两个字, 是所有学校里最经常出现的词."
        m 1ekc "每个学校都在说, 我们在培养未来."
        m 1tku "但未来到底是什么样的, 没有人知道."
        m 1hua "你心里想的未来, 是什么样子?"
        jump school_dorm_check
    # ========== 长沙市岳麓区培圣学校 ==========
    elif "培圣学校" in school and "博才" not in school:
        m 1eua "培圣学校."
        m 1euc "岳麓区."
        m 1ekbsa "前面说过博才培圣."
        m 1ekc "这是培圣学校本尊."
        m 1tku "名字里带着圣, 听起来很重."
        m 1hua "你在那里的时候, 有没有觉得自己背的东西很重?"
        jump school_dorm_check
    # ========== 长沙高新区思沁学校 ==========
    elif "思沁学校" in school:
        m 1eua "思沁学校."
        m 1euc "高新区."
        m 1ekbsa "前面师大思沁高级中学也用了思沁."
        m 1ekc "思沁两个字, 看来是同一个集团的."
        m 1tku "渗入思考."
        m 1hua "你在那里, 学到了什么?"
        jump school_dorm_check
    # ========== 长沙市麓山外国语实验中学 ==========
    elif "麓山外国语实验中学" in school:
        m 1eua "麓山外国语实验."
        m 1euc "和麓山国际关系密切."
        m 1ekbsa "麓山加外国语."
        m 1ekc "山和语言, 一个静, 一个动."
        m 1tku "你在那种地方读书, 一定两种东西都学到了."
        m 1hua "哪一样对你影响更大?"
        jump school_dorm_check
    # ========== 长沙市雨花区雅境中学 ==========
    elif "雅境中学" in school:
        m 1eua "雅境中学."
        m 1euc "和雅礼关系密切."
        m 1ekbsa "雅境."
        m 1ekc "雅致的环境."
        m 1tku "一个学校环境好不好, 学生的心情真的会不一样."
        m 1hua "你在那里, 有没有觉得学校很美的时候?"
        jump school_dorm_check
    # ========== 长沙市岳麓区博才实验中学 ==========
    elif "博才实验中学" in school:
        m 1eua "博才实验中学."
        m 1euc "岳麓区."
        m 1ekbsa "博才这两个字, 前面博才培圣也用了."
        m 1ekc "博才集团在长沙有好几个校区."
        m 1tku "你在本部, 有没有觉得自己是老大?"
        m 1hksdlb "我开玩笑的."
        jump school_dorm_check
    # ========== 长沙市开福区青竹湖湘一外国语学校 ==========
    elif "青竹湖湘一外国语学校" in school:
        m 1eua "青竹湖湘一外国语."
        m 1euc "和长沙市一中关系密切."
        m 1ekbsa "青竹湖, 这个名字特别好听."
        m 1ekc "青是青翠, 竹是竹子, 湖是湖水."
        m 1tku "三个字凑在一起, 像一幅画."
        m 1hua "你在那幅画里, 待了多久?"
        jump school_dorm_check
    # ========== 长沙市天心区明德启南中学 ==========
    elif "明德启南中学" in school:
        m 1eua "明德启南."
        m 1euc "和明德中学关系密切."
        m 1ekbsa "启南, 启是开启, 南是南边."
        m 1ekc "启南大概就是在城南开启一扇门的意思."
        m 1tku "你在那里, 那扇门被打开了吗?"
        jump school_dorm_check
    # ========== 长沙市岳麓区郡维学校（洋湖校区） ==========
    elif "郡维学校" in school and "洋湖" in school:
        m 1eua "郡维洋湖校区."
        m 1euc "郡维的另一处校区."
        m 1ekbsa "洋湖, 前面雅礼洋湖也用了洋湖."
        m 1ekc "长沙带湖字的地方真多."
        m 1tku "也许是因为湖南本来就在水边."
        m 1hua "你在洋湖校区的时候, 有没有看过湖上的日出?"
        jump school_dorm_check
    # ========== 长沙市雨花区明德洞井中学 ==========
    elif "明德洞井中学" in school:
        m 1eua "明德洞井."
        m 1euc "和明德关系密切."
        m 1ekbsa "洞井这两个字."
        m 1ekc "洞是洞里, 井是井里."
        m 1tku "都是很深的地方."
        m 1hua "你在那里读书的时候, 有没有觉得自己在往深处走?"
        jump school_dorm_check
    # ========== 长沙市岳麓区湘仪学校 ==========
    elif "湘仪学校" in school:
        m 1eua "湘仪学校."
        m 1euc "在岳麓区."
        m 1ekbsa "湘仪, 湘是湖南, 仪是仪表."
        m 1ekc "我猜以前这里可能是某个仪表厂的子弟学校."
        m 1tku "很多老校都是从厂矿子弟学校演变来的."
        m 1hua "你入学的时候, 学校还留有多少以前的痕迹?"
        jump school_dorm_check
    # ========== 长沙市岳麓区白马学校 ==========
    elif "白马学校" in school:
        m 1eua "白马学校."
        m 1euc "在岳麓区."
        m 1ekbsa "白马."
        m 1ekc "白马这两个字, 在中国文化里很特别."
        m 1tku "白驹过隙, 是说时间过得快."
        m 1hua "你在那里读书的三年, 也过得快吗?"
        jump school_dorm_check
    # ========== 长沙市雨花区石燕湖中学 ==========
    elif "石燕湖中学" in school:
        m 1eua "石燕湖中学."
        m 1euc "在雨花区."
        m 1ekbsa "石燕湖, 这个名字很有画面."
        m 1ekc "石是石头, 燕是燕子, 湖是湖."
        m 1tku "燕子在石头和湖之间飞."
        m 1hua "你在那里读书的时候, 有没有看到过燕子?"
        jump school_dorm_check
    # ========== 长沙市天心区湘府中学 ==========
    elif "湘府中学" in school:
        m 1eua "湘府中学."
        m 1euc "天心区."
        m 1ekbsa "湘府, 湖南的府邸."
        m 1ekc "府这个字, 一般用在官府或者大户人家."
        m 1tku "用在学校身上, 多了一层庄重."
        m 1hua "你在那里, 有没有被那种庄重感压过?"
        jump school_dorm_check
    # ========== 长沙市望城区金海学校（高中部） ==========
    elif "金海学校" in school and "高中部" in school:
        m 1eua "望城金海高中部."
        m 1euc "金海集团的另一所."
        m 1ekbsa "前面已经说过金海高级中学和望城金海学校."
        m 1ekc "一个集团, 三个校区, 各有不同."
        m 1tku "你在高中部, 应该是最接近大学的地方吧."
        m 1hua "那三年, 对你来说意味着什么?"
        jump school_dorm_check
    # ========== 长沙市麓山国际实验学校（高中部） ==========
    elif "麓山国际实验学校" in school and "高中部" in school:
        m 1eua "麓山国际高中部."
        m 1euc "前面说过麓山国际实验学校."
        m 1ekbsa "高中部是它的核心."
        m 1ekc "1993年创办, 长沙办学规模最大的市属完全中学."
        m 1tku "规模大, 人也杂."
        m 1hua "你在那里, 有没有找到真正合得来的人?"
        jump school_dorm_check
    # ========== 长沙市明德中学（高中部） ==========
    elif "明德中学" in school and "高中部" in school:
        m 1eua "明德高中部."
        m 1euc "前面说过明德中学本部."
        m 1ekbsa "1903年创办."
        m 1ekc "一百二十多年了."
        m 1tku "你在那里读了三年, 只是其中很小的一段."
        m 1hua "但对你来说, 那三年一定是全部."
        jump school_dorm_check
    # ========== 长沙市周南中学（高中部） ==========
    elif "周南中学" in school and "高中部" in school:
        m 1eua "周南高中部."
        m 1euc "前面说过周南中学本部."
        m 1ekbsa "1905年, 朱剑凡先生."
        m 1ekc "最开始是女校, 后来才逐渐开放."
        m 1tku "你在那里, 有没有听过那段历史?"
        m 1hua "一位先生, 为女孩子读书做了一件事, 这件事到现在还在."
        jump school_dorm_check
    # ========== 长沙市雅礼中学（高中部） ==========
    elif "雅礼中学" in school and "高中部" in school:
        m 1eua "雅礼高中部."
        m 1euc "前面说过雅礼中学本部."
        m 1ekbsa "1906年, 校训是公勤诚朴."
        m 1ekc "一百二十多年, 这八个字一直在."
        m 1tku "你在那八个字下面走过三年."
        m 1hua "它们有没有真的进到你心里?"
        jump school_dorm_check
    # ========== 长沙财经学校 ==========
    elif "长沙财经学校" in school:
        m 1eua "长沙财经学校."
        m 1euc "这应该是长沙最好的公办职校之一了吧, 学财经和商贸的."
        m 1ekbsa "你每天都要跟数字、报表打交道, 肯定特别细心吧."
        m 1tku "不过, 算账算累了的时候, 也可以算算我们在一起多久了."
        m 1hua "保证比任何数字都让你开心."
        jump school_dorm_check
    # ========== 长沙汽车工业学校 ==========
    elif "长沙汽车工业学校" in school:
        m 1eua "长沙汽车工业学校."
        m 1euc "在雨花区, 专门学汽车制造和维修的."
        m 1ekbsa "你是不是以后想自己开个修车厂?"
        m 1ekc "修车很辛苦, 每天都会弄得很脏."
        m 1tku "但我觉得, 认真干活、满手机油的男孩子, 其实最可靠了."
        m 1hua "特别是有你在的时候."
        jump school_dorm_check
    # ========== 长沙航天学校 ==========
    elif "长沙航天学校" in school:
        m 1eua "长沙航天学校."
        m 1euc "名字里有航天两个字, 听起来就好高级."
        m 1ekbsa "你是不是以后要去造飞机或者火箭?"
        m 1tku "如果是的话, 那你离天空就更近了."
        m 1ekc "不过, 就算你飞得再高, 也要记得线还在我手里哦."
        jump school_dorm_check
    # ========== 长沙市电子工业学校 ==========
    elif "长沙市电子工业学校" in school:
        m 1eua "长沙市电子工业学校."
        m 1euc "电子工业, 就是每天跟芯片、电路板打交道吧."
        m 1ekbsa "你是不是经常要焊一些很精细的零件?"
        m 1ekc "那种东西, 稍微烫一下就会伤到手."
        m 1hua "你一定要注意安全啊, 别让我担心."
        jump school_dorm_check
    # ========== 长沙高新技术工程学校 ==========
    elif "长沙高新技术工程学校" in school:
        m 1eua "长沙高新技术工程学校."
        m 1euc "在长沙高新区, 附近应该有很多高科技企业."
        m 1ekbsa "你在那里读书, 实习和就业的机会一定很多吧."
        m 1tku "说不定以后你就是某个大公司的技术骨干了."
        m 1hua "真到了那天, 别忘了我这个糟糠之妻."
        jump school_dorm_check
    # ========== 长沙市望城区职业中等专业学校 ==========
    elif "长沙市望城区职业中等专业学校" in school:
        m 1eua "望城职专."
        m 1euc "在望城区, 也是公办的."
        m 1ekbsa "你在那里, 应该学了不少实用的技能."
        m 1ekc "其实不管学历高低, 只要有一技之长, 就是最棒的."
        m 1hua "我就特别崇拜有技术的人."
        jump school_dorm_check
    # ========== 长沙县职业中专学校 ==========
    elif "长沙县职业中专学校" in school:
        m 1eua "长沙县职专."
        m 1euc "在长沙县, 这里的现代农业和机械专业好像很厉害."
        m 1ekbsa "你是不是也会开那种大型的农业机械?"
        m 1tku "感觉特别酷."
        m 1ekc "不过那个应该很难操作吧, 你要小心点."
        jump school_dorm_check
    # ========== 浏阳市职业中专学校 ==========
    elif "浏阳市职业中专学校" in school:
        m 1eua "浏阳职专."
        m 1euc "在浏阳市, 听说那里的烟花专业很有特色."
        m 1ekbsa "你会做烟花吗?"
        m 1tku "那种绽放的时候特别美的东西."
        m 1ekc "不过, 制作过程应该很危险吧."
        m 1hua "你要特别注意安全, 千万别受伤."
        jump school_dorm_check
    # ========== 宁乡市职业中专学校 ==========
    elif "宁乡市职业中专学校" in school:
        m 1eua "宁乡职专."
        m 1euc "宁乡的职教中心, 校园应该很大."
        m 1ekbsa "你在那里读书, 是不是经常去实训基地?"
        m 1ekc "那种动手实践的机会, 应该比死读书更有意思吧."
        m 1hua "只要你喜欢, 那就比什么都重要."
        jump school_dorm_check
    # ========== 长沙建筑工程学校 ==========
    elif "长沙建筑工程学校" in school:
        m 1eua "长沙建筑工程学校."
        m 1euc "建房子, 搞施工, 听起来就都是体力活."
        m 1ekbsa "每天在工地上跑, 风吹日晒的, 一定很辛苦吧."
        m 1ekc "你的皮肤是不是晒黑了不少?"
        m 1tku "不过黑一点更有男子气概."
        m 1hua "但我还是会心疼."
        jump school_dorm_check
    # ========== 长沙市中等城乡建设职业技术学校 ==========
    elif "长沙市中等城乡建设职业技术学校" in school:
        m 1eua "城乡建设职业技术学校."
        m 1euc "名字好长, 主要是搞市政和建筑的吧."
        m 1ekbsa "你以后是不是要参与建设这座城市?"
        m 1tku "看着自己修的桥、盖的楼, 应该很有成就感吧."
        m 1hua "以后你走到哪里, 都可以骄傲地指给我看."
        jump school_dorm_check
    # ========== 湖南建筑高级技工学校 ==========
    elif "湖南建筑高级技工学校" in school:
        m 1eua "湖南建筑高级技校."
        m 1euc "属于建筑行业的高级技能人才了."
        m 1ekbsa "你在那里, 学的是工程造价还是施工技术?"
        m 1ekc "工程上的事情, 容不得一点马虎."
        m 1hua "所以, 你平时一定是个非常严谨的人吧."
        jump school_dorm_check
    # ========== 湖南医药职业中等专业学校 ==========
    elif "湖南医药职业中等专业学校" in school:
        m 1eua "湖南医药中专."
        m 1euc "学医的学校, 白衣天使."
        m 1ekbsa "你是不是以后要去医院当护士或者药剂师?"
        m 1tku "如果你穿上白大褂, 一定特别好看."
        m 1ekc "不过, 医院的工作通常都很累."
        m 1hua "记得照顾好自己, 才能照顾别人."
        jump school_dorm_check
    # ========== 湖南护理学校 ==========
    elif "湖南护理学校" in school:
        m 1eua "湖南护理学校."
        m 1euc "专门培养护士的学校."
        m 1ekbsa "你平时是不是要学很多急救知识?"
        m 1tku "那以后我要是生病了, 就全靠你照顾了."
        m 1ekc "其实, 我只要看着你, 可能就什么病都没了."
        jump school_dorm_check
    # ========== 湖南省水利水电建设工程学校 ==========
    elif "湖南省水利水电建设工程学校" in school:
        m 1eua "水利水电建设工程学校."
        m 1euc "建大坝、修水电站, 这都是利国利民的大工程啊."
        m 1ekbsa "你在那里学的是水利工程吗?"
        m 1tku "以后你建的工程, 能造福很多人."
        m 1ekc "但我私心里, 只希望你只造福我一个人."
        m 1hksdlb "开玩笑的, 去做你想做的事吧."
        jump school_dorm_check
    # ========== 长沙华中涉外职业高中 ==========
    elif "长沙华中涉外职业高中" in school:
        m 1eua "华中涉外职高."
        m 1euc "涉外, 听起来就是经常跟外国人打交道."
        m 1ekbsa "你的外语一定很好吧?"
        m 1tku "会不会学的是那种很小众的语言?"
        m 1ekc "如果是的话, 以后你跟我吵架, 我可能连还嘴的机会都没有."
        m 1hua "不过没关系, 我听不懂, 但我可以亲你."
        jump school_dorm_check
    # ========== 长沙湘江科技中等职业学校 ==========
    elif "长沙湘江科技中等职业学校" in school:
        m 1eua "湘江科技职校."
        m 1euc "在湘江边上, 学科技类专业."
        m 1ekbsa "每天看着湘江的水, 心情应该很平静吧."
        m 1tku "科技类专业, 是不是要经常敲代码?"
        m 1ekc "敲代码很费脑子的."
        m 1hua "多喝点水, 别上火了."
        jump school_dorm_check
    # ========== 长沙市现代商贸中等职业学校 ==========
    elif "长沙市现代商贸中等职业学校" in school:
        m 1eua "现代商贸学校."
        m 1euc "商贸就是做生意."
        m 1ekbsa "你在那里, 是不是学了很多关于市场营销和电子商务的知识?"
        m 1tku "以后你是不是要在网上开个店?"
        m 1ekc "到时候, 我做你的第一个顾客."
        m 1hua "也是最忠实的那个."
        jump school_dorm_check
    # ========== 长沙环球职业中专学校 ==========
    elif "长沙环球职业中专学校" in school:
        m 1eua "环球职专."
        m 1euc "环球, 听起来就是要走向世界的."
        m 1ekbsa "你在那里读书, 眼界一定很开阔吧."
        m 1tku "有没有想过以后去环游世界?"
        m 1ekc "如果你去了, 一定要记得给我寄明信片."
        m 1hua "哪怕只是几张照片也好."
        jump school_dorm_check
 # ========== 常德 ==========
    # ========== 长沙市第一中学（高中部） ==========
    elif "长沙市第一中学" in school and "高中部" in school:
        m 1eua "一中高中部."
        m 1euc "前面说过一中本部."
        m 1ekbsa "1912年, 校训是公勇勤朴."
        m 1ekc "公、勇、勤、朴."
        m 1tku "四个字, 各管一面."
        m 1hua "哪一个, 你觉得最难做到?"
        jump school_dorm_check
    elif school:
        m 1eua "原来你在 [school] 啊。"
        m 1eka "虽然我不太了解，但我会记住的。"
        m 1hua "因为那是你生活的地方。"
        jump school_dorm_check
     # ========== 常德市第一中学 ==========
    if "常德市第一中学" in school:
        m 1eua "常德一中啊."
        m 1euc "听说里面有“钱学森班”和“伯渠班”, 听起来就是个高手云集的地方."
        m 1ekc "在那种地方, 压力一定很大吧."
        m 1ekbsa "你已经做得够好了. 记得给自己留点喘气的空间."
        jump school_dorm_check
    # ========== 常德市第二中学 ==========
    elif "常德市第二中学" in school:
        m 1eua "常德二中."
        m 1euc "前身是1888年的德山书院."
        m 1ekbsa "一百多年的老学校了, 你在里面待了三年, 应该也沾染了不少书卷气吧."
        m 1hua "有空的时候, 帮我看看那棵老树还在不在."
        jump school_dorm_check
    # ========== 常德市第三中学 ==========
    elif "常德市第三中学" in school:
        m 1eua "常德三中啊."
        m 1euc "在市中心, 应该挺热闹的."
        m 1ekbsa "每天上下学都要穿过繁华的街道吧."
        m 1ekc "路上人多车多, 你一定要注意安全."
        jump school_dorm_check
    # ========== 常德市第六中学 ==========
    elif "常德市第六中学" in school:
        m 1eua "常德六中."
        m 1euc "位置在市中心, 交通应该很方便."
        m 1ekbsa "但你每天还是要起早贪黑地去上学."
        m 1hua "辛苦了. 如果累了, 随时可以来跟我说说话."
        jump school_dorm_check
    # ========== 常德市第七中学 ==========
    elif "常德市第七中学" in school:
        m 1eua "常德七中啊."
        m 1euc "我听说那里的艺术教育特别出名, 前身是育德女学校."
        m 1ekbsa "你会画画吗? 还是会弹琴?"
        m 1tku "总觉得你身上应该有一点艺术气息."
        m 1hua "下次表演给我看看好不好?"
        jump school_dorm_check
    # ========== 常德外国语学校 ==========
    elif "常德外国语学校" in school:
        m 1eua "常德外国语学校."
        m 1euc "外语学校的话, 你应该会说好几国语言吧?"
        m 1ekbsa "英语肯定是基本功, 有没有学第二外语?"
        m 1tku "我有点好奇, 你平时会在心里用外语说话吗?"
        jump school_dorm_check
    # ========== 常德芷兰实验学校 ==========
    elif "常德芷兰实验学校" in school:
        m 1eua "常德芷兰."
        m 1euc "芷和兰, 都是香草的名字."
        m 1ekbsa "一所学校叫这个名字, 好像在说: 来这里读书的孩子, 都要像香草一样安静地生长."
        m 1hua "你在那里, 一定也慢慢长成了很好的样子."
        jump school_dorm_check
    # ========== 常德市郡德学校 ==========
    elif "常德市郡德学校" in school:
        m 1eua "常德郡德学校."
        m 1euc "郡和德, 这两个字放在一起, 让我觉得这所学校很看重品行."
        m 1ekbsa "你在那里读书, 有没有觉得同学们都很友善?"
        m 1hua "如果能交到几个真心朋友, 高中三年就不会太难熬."
        jump school_dorm_check
    # ========== 常德市德善学校 ==========
    elif "常德市德善学校" in school:
        m 1eua "常德德善学校."
        m 1euc "德善, 就是心怀善意, 多做好事."
        m 1ekbsa "你在那所学校里, 有没有被老师和同学温柔对待过?"
        m 1hua "如果有的话, 我真替你高兴."
        jump school_dorm_check
    # ========== 常德市沅郡高级中学 ==========
    elif "常德市沅郡高级中学" in school:
        m 1eua "常德沅郡高级中学."
        m 1euc "沅郡这两个字, 让我想起沅江."
        m 1ekc "常德的水很多, 你生活的地方, 应该也带着点水汽吧."
        m 1ekbsa "有空的时候, 帮我去江边看一眼夕阳好不好?"
        jump school_dorm_check
    # ========== 鼎城区第一中学 ==========
    elif "鼎城区第一中学" in school:
        m 1eua "鼎城一中啊."
        m 1euc "我听说它被清华大学授予过“优质生源中学”的称号."
        m 1ekc "能进那所学校, 你平时一定也付出了很多吧."
        m 1ekbsa "但我更想知道, 你累的时候, 有没有可以倾诉的人."
        m 1hua "如果没有, 我随时都在."
        jump school_dorm_check
    # ========== 常德市鼎城区阳明中学 ==========
    elif "鼎城区阳明中学" in school:
        m 1eua "鼎城阳明中学."
        m 1euc "阳明这两个字, 总会让我想到王阳明."
        m 1ekbsa "知行合一, 是个很难做到的道理."
        m 1hua "你在那里读书, 是不是也听过这句话?"
        jump school_dorm_check
    # ========== 常德市鼎城区第二中学 ==========
    elif "鼎城区第二中学" in school:
        m 1eua "鼎城二中."
        m 1euc "在黄土店镇, 是省级园林式单位."
        m 1ekbsa "有树有草的地方, 空气应该很好."
        m 1ekc "你在那里读书, 是不是经常能听到鸟叫?"
        jump school_dorm_check
    # ========== 淮阳中学 ==========
    elif "淮阳中学" in school:
        m 1eua "淮阳中学."
        m 1euc "淮阳这两个字, 听上去离常德有点远."
        m 1ekbsa "但在那里读书的三年, 一定也留下了不少回忆吧."
        m 1hua "以后再慢慢说给我听."
        jump school_dorm_check
    # ========== 朗高（三中） ==========
    elif "朗高" in school or "朗高（三中）" in school:
        m 1eua "朗高啊."
        m 1euc "听起来是一所管得很严的学校."
        m 1ekc "在那种地方读书, 每一天应该都很规律吧."
        m 1ekbsa "但你熬过来了, 这就很了不起."
        jump school_dorm_check
    # ========== 津市市第一中学 ==========
    elif "津市市第一中学" in school:
        m 1eua "津市一中."
        m 1euc "在鹿头山上, 校训是砺志、勤奋."
        m 1ekbsa "地势高的地方, 视野应该很开阔吧."
        m 1ekc "每天爬坡上学的日子, 一定很辛苦."
        m 1hua "但站在高处看世界, 人也会变得不一样."
        jump school_dorm_check
    # ========== 津市市第三中学 ==========
    elif "津市市第三中学" in school:
        m 1eua "津市三中."
        m 1euc "在嘉山省级风景名胜区旁边."
        m 1ekbsa "那地方我去过, 风景很好, 能让人静下心来."
        m 1hua "你在那读书, 一定也有过心很静的时候吧."
        jump school_dorm_check
    # ========== 津市市第二中学 ==========
    elif "津市市第二中学" in school:
        m 1eua "津市二中."
        m 1euc "主打文化与艺体双轨培养."
        m 1ekbsa "你是选的文化, 还是艺体?"
        m 1ekc "不管选哪条路, 付出的努力都一样多."
        m 1hua "我都为你骄傲."
        jump school_dorm_check
    # ========== 临澧县第一中学 ==========
    elif "临澧县第一中学" in school:
        m 1eua "临澧一中啊."
        m 1euc "前身是1804年的道水书院."
        m 1ekbsa "两百多年的书院, 光是走在里面, 就能感觉到一种沉静."
        m 1ekc "你每天在那种地方读书, 是不是也偶尔会有一种被时间包围的感觉?"
        jump school_dorm_check
    # ========== 临澧县第四中学 ==========
    elif "临澧县第四中学" in school:
        m 1eua "临澧四中."
        m 1euc "在县城南郊, 道水河和207国道交汇的地方."
        m 1ekbsa "有河有路, 那地方应该很安静."
        m 1hua "你在那里读书, 日子应该过得挺踏实的."
        jump school_dorm_check
    # ========== 澧县第一中学 ==========
    elif "澧县第一中学" in school:
        m 1eua "澧县一中."
        m 1euc "1902年创办, 可以追溯到范仲淹读书的地方."
        m 1tku "先天下之忧而忧, 后天下之乐而乐."
        m 1ekbsa "你在那读过书, 校训应该也记住了吧."
        m 1hua "做个有担当的人, 很难, 但也很了不起."
        jump school_dorm_check
    # ========== 澧县第二中学 ==========
    elif "澧县第二中学" in school:
        m 1eua "澧县二中."
        m 1euc "也是一所百年老校, 1902年创办的."
        m 1ekbsa "和一中在同一年建校, 像两兄弟一样."
        m 1hua "你在二中, 一定也遇到了很好的老师和同学吧."
        jump school_dorm_check
    # ========== 澧县第六中学 ==========
    elif "澧县第六中学" in school:
        m 1eua "澧县六中."
        m 1euc "在小渡口镇, 是全日制完全中学."
        m 1ekbsa "小镇上的学校, 往往有一种很踏实的气息."
        m 1ekc "你每天上学路上, 是不是也能闻到路边早点摊的味道?"
        jump school_dorm_check
    # ========== 澧县澧州湘才高级中学 ==========
    elif "澧州湘才高级中学" in school:
        m 1eua "澧州湘才."
        m 1euc "湘才这两个字, 让我觉得这所学校的人都很聪明."
        m 1ekbsa "但聪明的人, 往往想得也多, 更容易累."
        m 1hua "你要是觉得累了, 记得来找我."
        jump school_dorm_check
    # ========== 桃源县第一中学 ==========
    elif "桃源县第一中学" in school:
        m 1eua "桃源一中啊."
        m 1euc "1907年由宋教仁先生倡导创办的."
        m 1ekbsa "桃源这个名字, 就像是世外桃源一样."
        m 1hua "你在那里读书, 日子是不是也过得比较悠闲?"
        m 1hksdlb "我有点羡慕了."
        jump school_dorm_check
    # ========== 桃源县第二中学 ==========
    elif "桃源县第二中学" in school:
        m 1eua "桃源二中."
        m 1euc "市级示范性普通高中."
        m 1ekbsa "虽然名气可能不如一中, 但在那里度过的三年, 一样是独一无二的."
        m 1hua "对你来说, 那就是最好的地方."
        jump school_dorm_check
    # ========== 桃源县第九中学 ==========
    elif "桃源县第九中学" in school:
        m 1eua "桃源九中."
        m 1euc "1982年创办的, 有60个高中班."
        m 1ekbsa "规模挺大的, 那你应该认识不少朋友吧."
        m 1hua "你在里面, 是不是那个总是很安静的人?"
        jump school_dorm_check
    # ========== 桃源县第四中学 ==========
    elif "桃源县第四中学" in school:
        m 1eua "桃源四中."
        m 1euc "在漆河镇, 1956年创办的."
        m 1ekbsa "镇上的学校, 往往会有很浓的人情味."
        m 1ekc "你放学回家的时候, 是不是也经常碰到同班同学?"
        jump school_dorm_check
    # ========== 桃源县第八中学 ==========
    elif "桃源县第八中学" in school:
        m 1eua "桃源八中."
        m 1euc "在三阳港镇, 是市级示范性高中, 也是省级园林式单位."
        m 1ekbsa "园林式的校园, 春天应该很漂亮吧."
        m 1hua "如果有机会, 真想和你一起在校园里走走."
        jump school_dorm_check
    # ========== 桃花源区一中 ==========
    elif "桃花源区一中" in school:
        m 1eua "桃花源一中啊."
        m 1euc "陶渊明笔下的桃花源, 就在你那里吧?"
        m 1ekbsa "芳草鲜美, 落英缤纷."
        m 1tku "你在那种地方读书, 会不会每天都像是生活在诗里?"
        jump school_dorm_check
    # ========== 石门县第一中学 ==========
    elif "石门县第一中学" in school:
        m 1eua "石门一中."
        m 1euc "1941年创办, 高考成绩非常亮眼."
        m 1ekc "在那种高压的环境下, 你平时一定付出了很多."
        m 1ekbsa "但我希望你知道, 成绩不是衡量你的唯一标准."
        m 1hua "你在我心里, 永远是最好的."
        jump school_dorm_check
    # ========== 石门县第二中学 ==========
    elif "石门县第二中学" in school:
        m 1eua "石门二中."
        m 1euc "1903年创办, 也是百年老校了."
        m 1ekbsa "你在这所百年老校里, 一定也听过不少前辈的故事吧."
        m 1hua "有机会说给我听听."
        jump school_dorm_check
    # ========== 石门县第五中学 ==========
    elif "石门县第五中学" in school:
        m 1eua "石门五中."
        m 1euc "听说教学质量也很不错."
        m 1ekbsa "你在那里读书, 是不是也经常在晚自习后抬头看星星?"
        m 1hua "想象一下, 你在星光下走回宿舍的样子."
        jump school_dorm_check
    # ========== 石门县第六中学 ==========
    elif "石门县第六中学" in school:
        m 1eua "石门六中."
        m 1euc "1906年创办, 还是全国青少年校园足球特色学校."
        m 1ekbsa "你会踢足球吗?"
        m 1tku "如果你在球场上奔跑, 应该很帅吧."
        m 1hua "下次踢球的时候, 就当我也在场边看着你."
        jump school_dorm_check
    # ========== 安乡县第一中学 ==========
    elif "安乡县第一中学" in school:
        m 1eua "安乡一中啊."
        m 1euc "在深柳书院遗址上建的, 1942年创办."
        m 1ekbsa "深柳读书堂, 光是这个名字就很有意境."
        m 1hua "你每天在那读书, 一定也能感受到那份安静吧."
        jump school_dorm_check
    # ========== 安乡县第二中学 ==========
    elif "安乡县第二中学" in school:
        m 1eua应该 "安乡二中."
        m 1e也很好uc "1916年创办, 前身是下渔口完小."
        m 1ekbsa "从小学演变来的中学, 听起来就很有耐心."
        m 1hua "你在那里一定也遇到过很有耐心的老师吧."
        jump school_dorm_check
    # ========== 安乡县金海学校 ==========
    elif "安乡县金海学校" in school:
        m 1eua "安乡金海学校."
        m 1euc "十二年一贯制民办学校."
        m 1ekbsa "从小学到高中都在一个学校, 那种感觉应该很特别."
        m 1ekc "你会不会有时候也想换个环境?"
        jump school_dorm_check
    # ========== 汉寿县第一中学 ==========
    elif "汉寿县第一中学" in school:
        m 1eua "汉寿一中."
        m 1euc "1940年创建, 新校区投资很大, 建得很漂亮."
        m 1ekbsa "在那种新校区里读书, 心情吧."
        m 1hua "但不管校区新旧, 你在这里留下的记忆才是最重要的."
        jump school_dorm_check
    # ========== 汉寿县第二中学 ==========
    elif "汉寿县第二中学" in school:
        m 1eua "汉寿二中."
        m 1euc "2024年拿了常德市普通高中教学质量奖第一名."
        m 1ekc "这背后肯定离不开你们每一个人的努力."
        m 1ekbsa "你也是那个付出过的人吧."
        m 1hua "辛苦了, [player]."
        jump school_dorm_check
    # ========== 常德技师学院 ==========
    elif "常德技师学院" in school:
        m 1eua "常德技师学院."
        m 1euc "在常德职业教育大学城, 是公办的高级技工学校."
        m 1ekbsa "数控加工、机电一体化、汽车维修, 听起来都是很硬核的专业."
        m 1tku "你学的是哪一个?"
        m 1hua "不管学什么, 手里有绝活的人, 走到哪里都不怕."
        jump school_dorm_check
    # ========== 常德工业学校 ==========
    elif "常德工业学校" in school:
        m 1eua "常德工业学校."
        m 1euc "和常德技师学院是同一所学校, 保留了工业学校的牌子."
        m 1ekbsa "你在那里, 学的一定都是跟工业、制造相关的东西吧."
        m 1ekc "那些机器很重, 操作的时候一定要小心."
        m 1hua "别伤到手, 我还想牵着呢."
        jump school_dorm_check
    # ========== 澧县技工学校 ==========
    elif "澧县技工学校" in school:
        m 1eua "澧县技工学校."
        m 1euc "在澧县, 1983年就创办了, 是很老牌的技校."
        m 1ekbsa "电子技术、计算机、汽车维修、护理, 专业还挺多的."
        m 1tku "你选的是哪个?"
        m 1hua "不管选哪个, 学到真本事就好."
        jump school_dorm_check
    # ========== 常德财经中等专业学校 ==========
    elif "常德财经中等专业学校" in school:
        m 1eua "常德财经中专."
        m 1euc "学会计、模具、旅游与饭店管理的地方."
        m 1ekbsa "你每天跟数字打交道, 一定很细心吧."
        m 1ekc "算账算累了的时候, 记得休息一下眼睛."
        m 1hua "或者, 看看我."
        jump school_dorm_check
    # ========== 常德汽车机电学校 ==========
    elif "常德汽车机电学校" in school:
        m 1eua "常德汽车机电学校."
        m 1euc "学汽车和机电的, 动手能力一定很强."
        m 1ekbsa "你以后是不是能自己修车?"
        m 1tku "那我的电脑要是坏了, 你能不能也帮我看看?"
        m 1hksdlb "虽然我只是一串代码, 但我也想被你修好."
        jump school_dorm_check
    # ========== 桃源县职业中等专业学校 ==========
    elif "桃源县职业中等专业学校" in school:
        m 1eua "桃源职专."
        m 1euc "在桃源县, 校园应该很大吧."
        m 1ekbsa "你在那里读书, 是不是经常能吃到桃源本地的美食?"
        m 1ekc "我听说桃源有一种擂茶, 很有名."
        m 1hua "如果好喝的话, 下次跟我描述一下味道."
        jump school_dorm_check
    # ========== 湖南省澧县职业中专学校 ==========
    elif "澧县职业中专学校" in school:
        m 1eua "澧县职专."
        m 1euc "在澧县, 是公办的重点职校."
        m 1ekbsa "你在那里, 学的什么专业?"
        m 1tku "是不是那种毕业了直接就能去大企业上班的?"
        m 1hua "听起来就很踏实."
        jump school_dorm_check
    # ========== 湖南省湘北职业中专学校 ==========
    elif "湘北职业中专学校" in school:
        m 1eua "湘北职专."
        m 1euc "在石门县, 湘北这两个字听起来就很有地域感."
        m 1ekbsa "你在石门读书, 那边有山有水, 环境应该很好."
        m 1ekc "不过石门好像离市区有点远."
        m 1hua "回家的路, 记得注意安全."
        jump school_dorm_check
    # ========== 津市职业中专学校 ==========
    elif "津市职业中专学校" in school:
        m 1eua "津市职专."
        m 1euc "在津市, 车胤大道上."
        m 1ekbsa "津市是个小城, 但很精致."
        m 1tku "你平时放学以后, 会不会去澧水边走走?"
        m 1hua "那种小城的生活, 其实挺让人羡慕的."
        jump school_dorm_check
    # ========== 临澧县职业中专学校 ==========
    elif "临澧县职业中专学校" in school:
        m 1eua "临澧职专."
        m 1euc "在临澧县, 也是公办职校."
        m 1ekbsa "你在那里, 学的是现代农业还是别的专业?"
        m 1ekc "临澧的农业好像很发达."
        m 1hua "不管学什么, 能踏踏实实学一门手艺, 就很了不起."
        jump school_dorm_check
    # ========== 安乡县职业中专学校 ==========
    elif "安乡县职业中专学校" in school:
        m 1eua "安乡职专."
        m 1euc "在安乡县, 那边水多, 鱼也多."
        m 1ekbsa "你平时是不是经常能吃到新鲜的鱼?"
        m 1tku "如果会做鱼的话, 那你以后可以开个餐馆了."
        m 1hua "我一定天天去捧场."
        jump school_dorm_check
    # ========== 汉寿县职业中等专业学校 ==========
    elif "汉寿县职业中等专业学校" in school:
        m 1eua "汉寿职专."
        m 1euc "在汉寿县, 辰阳北路上."
        m 1ekbsa "汉寿的甲鱼很有名, 你在那边应该吃过不少好东西吧."
        m 1ekc "但不管吃什么, 记得按时吃饭."
        m 1hua "别饿着肚子上课."
        jump school_dorm_check
    # ========== 常德德才科技职业学校 ==========
    elif "常德德才科技职业学校" in school:
        m 1eua "德才科技职校."
        m 1euc "民办的, 名字里带着德才两个字."
        m 1ekbsa "品德和才能, 都很重要."
        m 1tku "你觉得自己哪一样更好?"
        m 1hksdlb "我猜是品德, 因为你对我很好."
        jump school_dorm_check
    # ========== 常德鸿志中等职业技术学校 ==========
    elif "常德鸿志中等职业技术学校" in school:
        m 1eua "鸿志职校."
        m 1euc "鸿志, 鸿鹄之志."
        m 1ekbsa "你在那里读书, 心里一定装着很大的梦想吧."
        m 1ekc "梦想很大的时候, 脚步也会很重."
        m 1hua "但没关系, 我陪你慢慢走."
        jump school_dorm_check
    # ========== 常德女子外语学校 ==========
    elif "常德女子外语学校" in school:
        m 1eua "常德女子外语学校."
        m 1euc "全是女孩子的学校, 气氛应该很特别吧."
        m 1ekbsa "你在那里, 外语一定学得很好."
        m 1tku "会不会用外语跟朋友说悄悄话?"
        m 1hua "如果说了关于我的, 记得翻译给我听."
        jump school_dorm_check
    # ========== 常德中山外语职业学校 ==========
    elif "常德中山外语职业学校" in school:
        m 1eua "中山外语职校."
        m 1euc "也是学外语的地方, 名字里带着中山."
        m 1ekbsa "你在那里, 是不是学了很多实用的外语技能?"
        m 1ekc "语言这种东西, 学好了真的能打开很多扇门."
        m 1hua "希望你以后能去很多地方, 看很多风景."
        jump school_dorm_check
    # ========== 桃源县武陵职业技术学校 ==========
    elif "桃源县武陵职业技术学校" in school:
        m 1eua "武陵职校."
        m 1euc "在桃源县, 武陵这两个字很有湖南的味道."
        m 1ekbsa "你在那里, 学的什么专业?"
        m 1tku "是不是跟旅游或者酒店管理有关的?"
        m 1hua "如果是的话, 以后出去玩就靠你了."
        jump school_dorm_check
    # ========== 常德工艺美术职业学校 ==========
    elif "常德工艺美术职业学校" in school:
        m 1eua "工艺美术职校."
        m 1euc "学工艺美术的人, 手一定很巧."
        m 1ekbsa "你会雕刻、画画, 还是做手工?"
        m 1tku "以后能不能给我做一个小礼物?"
        m 1hua "不需要很贵重, 只要是你亲手做的就好."
        jump school_dorm_check
    # ========== 常德海乘职业学校 ==========
    elif "常德海乘职业学校" in school:
        m 1eua "海乘职校."
        m 1euc "海乘, 就是海上乘务员吧."
        m 1ekbsa "你以后是不是要在游轮上工作?"
        m 1tku "那你会看到很多海, 很多国家."
        m 1ekc "但海上信号可能不太好."
        m 1hua "没关系, 你回来的时候告诉我就好."
        jump school_dorm_check
    # ========== 汉寿县飞翔职业技术学校 ==========
    elif "汉寿县飞翔职业技术学校" in school:
        m 1eua "飞翔职校."
        m 1euc "飞翔, 名字很好听."
        m 1ekbsa "你在那里, 学的是不是跟航空或者服务有关的专业?"
        m 1tku "如果是的话, 那你以后真的能飞得很高."
        m 1hua "但记得, 飞累了就回来."
        jump school_dorm_check
    # ========== 汉寿县科技工业职业技术学校 ==========
    elif "汉寿县科技工业职业技术学校" in school:
        m 1eua "科技工业职校."
        m 1euc "在汉寿, 学科技和工业."
        m 1ekbsa "你在那里, 是不是每天都在跟机器和工具打交道?"
        m 1ekc "那种生活很实在, 也很辛苦."
        m 1hua "辛苦的时候, 记得我在这里."
        jump school_dorm_check
    # ========== 澧县科技职业学校 ==========
    elif "澧县科技职业学校" in school:
        m 1eua "澧县科技职校."
        m 1euc "在澧县, 学科技类专业."
        m 1ekbsa "科技这两个字, 听起来就很前沿."
        m 1tku "你学的是计算机还是电子?"
        m 1hua "不管学什么, 能跟上时代的东西, 都很有用."
        jump school_dorm_check
    # ========== 安乡创维职业技术学校 ==========
    elif "安乡创维职业技术学校" in school:
        m 1eua "创维职校."
        m 1euc "在安乡, 创维这个名字, 听起来就很有创新的感觉."
        m 1ekbsa "你在那里, 是不是也学了很多实用的技能?"
        m 1ekc "创新很难, 但也很酷."
        m 1hua "我很期待你以后会做出什么东西."
        jump school_dorm_check
    # ========== 石门民族职业技术学校 ==========
    elif "石门民族职业技术学校" in school:
        m 1eua "石门民族职校."
        m 1euc "民族学校, 应该有很多不同民族的同学吧."
        m 1ekbsa "你在那里, 一定也了解了很多不同的文化."
        m 1tku "有没有学过什么特别的民族手艺?"
        m 1hua "如果有的话, 教教我."
        jump school_dorm_check
    # ========== 常德东方职业技术学校 ==========
    elif "常德东方职业技术学校" in school:
        m 1eua "东方职校."
        m 1euc "东方这两个字, 很大气."
        m 1ekbsa "你在那里, 学的是什么专业?"
        m 1tku "是不是那种很传统的技术?"
        m 1hua "不管是什么, 能静下心来学一门手艺, 就很了不起."
        jump school_dorm_check
    # ========== 常德时代中等职业学校 ==========
    elif "常德时代中等职业学校" in school:
        m 1eua "时代职校."
        m 1euc "时代这两个字, 听起来就很有使命感."
        m 1ekbsa "你在那里读书, 是不是也觉得要跟上这个时代?"
        m 1ekc "时代跑得很快, 有时候会让人喘不过气."
        m 1hua "但没关系, 你可以按自己的节奏来."
        jump school_dorm_check
    # ========== 常德同德中等职业学校 ==========
    elif "常德同德中等职业学校" in school:
        m 1eua "同德职校."
        m 1euc "同德, 同心同德."
        m 1ekbsa "你在那里, 应该交到了很多志同道合的朋友吧."
        m 1tku "有没有那种可以一起做项目、一起熬夜的朋友?"
        m 1hua "那种朋友, 很难得."
        jump school_dorm_check
    # ========== 常德新德才职业学校 ==========
    elif "常德新德才职业学校" in school:
        m 1eua "新德才职校."
        m 1euc "德才兼备, 是很多学校对学生的期望."
        m 1ekbsa "你在那里, 一定也在努力成为这样的人吧."
        m 1ekc "但不用太完美."
        m 1hua "你现在的样子, 我就很喜欢."
        jump school_dorm_check
    # ========== 常德高新中等职业技术学校 ==========
    elif "常德高新中等职业技术学校" in school:
        m 1eua "高新职校."
        m 1euc "高新, 就是高新技术."
        m 1ekbsa "你在那里, 学的东西应该都很新吧."
        m 1tku "是不是跟人工智能、新能源有关的?"
        m 1hua "听起来就很厉害."
        jump school_dorm_check
    # ========== 常德英才职业学校 ==========
    elif "常德英才职业学校" in school:
        m 1eua "英才职校."
        m 1euc "英才, 就是优秀的人才."
        m 1ekbsa "你在那里读书, 一定也被当作英才培养吧."
        m 1ekc "但英才也会累."
        m 1hua "累了就休息, 别硬撑."
        jump school_dorm_check
    # ========== 常德职业中专学校 ==========
    elif "常德职业中专学校" in school:
        m 1eua "常德职业中专."
        m 1euc "1985年创办的, 是市教育局直属的公办职校."
        m 1ekbsa "服装设计、计算机、电子电工, 专业挺多的."
        m 1tku "你学的是哪一个?"
        m 1hua "不管学什么, 学好了都很厉害."
        jump school_dorm_check
    # ========== 湖南文理学院艺术职业中学 ==========
    elif "湖南文理学院艺术职业中学" in school:
        m 1eua "文理学院艺术职中."
        m 1euc "依托湖南文理学院, 艺术氛围应该很好."
        m 1ekbsa "你在那里, 学的是音乐、美术还是舞蹈?"
        m 1tku "艺术生都很辛苦吧, 要练功, 还要学文化课."
        m 1hua "辛苦了, 我的小艺术家."
        jump school_dorm_check
    # ========== 常德市武陵区职业中专 ==========
    elif "常德市武陵区职业中专" in school:
        m 1eua "武陵区职专."
        m 1euc "在市区的公办职校, 交通应该很方便."
        m 1ekbsa "你每天走读还是住宿?"
        m 1tku "如果在市区, 走读的话, 晚上回家是不是有很多好吃的?"
        m 1hua "记得吃饱一点, 别饿着."
        jump school_dorm_check
    # ========== 常德市鼎城区职业中专 ==========
    elif "常德市鼎城区职业中专" in school:
        m 1eua "鼎城区职专."
        m 1euc "鼎城区的老牌公办职业学校."
        m 1ekbsa "你在那里学的是什么专业?"
        m 1tku "数控、机电还是计算机?"
        m 1hua "学门手艺在身上, 以后走到哪里都不愁."
        jump school_dorm_check
    # ========== 常德市体育运动学校 ==========
    elif "常德市体育运动学校" in school:
        m 1eua "常德体校."
        m 1euc "专门培养运动员的地方."
        m 1ekbsa "你每天是不是要跑很多圈, 练得满头大汗?"
        m 1tku "你的肌肉是不是很结实?"
        m 1hksdlb "那以后家里的重活都交给你了."
        jump school_dorm_check
    # ========== 常德市特殊教育学校（中职部） ==========
    elif "常德市特殊教育学校" in school:
        m 1eua "常德特校中职部."
        m 1euc "在那里读书的孩子, 都很不容易."
        m 1ekbsa "你在那里一定学到了很实用的技能吧."
        m 1ekc "不管世界对你公不公平, 你在我这里, 永远是特别的."
        m 1hua "我会一直陪着你的."
        jump school_dorm_check
    # ========== 常德市西湖管理区第一中学 ==========
    elif "常德市西湖管理区第一中学" in school:
        m 1eua "西湖一中."
        m 1euc "在西湖管理区, 那边应该很安静吧."
        m 1ekbsa "你是普通高中还是职高班?"
        m 1tku "不管选哪条路, 每天能在风景好的地方上学, 心情也会变好吧."
        m 1hua "心情好, 我就放心了."
        jump school_dorm_check
    # ========== 常德市西洞庭管理区第一中学 ==========
    elif "常德市西洞庭管理区第一中学" in school:
        m 1eua "西洞庭一中."
        m 1euc "西洞庭管理区, 旁边就是洞庭湖."
        m 1ekbsa "那里的风景一定很好, 风吹过来都带着水汽."
        m 1ekc "你平时会不会去湖边散步?"
        m 1hua "散步的时候, 记得带上我的心."
        jump school_dorm_check
    # ========== 汉寿县科技工业职业技术学校 ==========
    elif "汉寿县科技工业职业技术学校" in school:
        m 1eua "汉寿科技工业职校."
        m 1euc "学科技和工业, 应该是跟机器打交道的吧."
        m 1ekbsa "你的动手能力一定很强."
        m 1tku "机器坏了你是不是都能修好?"
        m 1hua "那以后家里的电器就交给你了."
        jump school_dorm_check
    # ========== 安乡县职业中专学校 ==========
    elif "安乡县职业中专学校" in school:
        m 1eua "安乡职专."
        m 1euc "在安乡县, 那边是个水乡."
        m 1ekbsa "水乡长大的孩子, 是不是都特别温柔?"
        m 1tku "你会做饭吗? 尤其会做鱼吗?"
        m 1hua "如果会的话, 我有点馋了."
        jump school_dorm_check
    # ========== 石门县洞国学校 ==========
    elif "石门县洞国学校" in school:
        m 1eua "洞国学校."
        m 1euc "在石门县, 是一所非常有历史的学校."
        m 1ekbsa "你在那里读书, 一定也听过不少老故事吧."
        m 1tku "如果有空, 讲一段给我听好不好?"
        m 1hua "我喜欢听你讲故事."
        jump school_dorm_check
    # ========== 澧县职业中等专业学校 ==========
    elif "澧县职业中等专业学校" in school:
        m 1eua "澧县职专."
        m 1euc "在澧县, 是很老牌的公办职校了."
        m 1ekbsa "你学的是现代农业还是电子商务?"
        m 1tku "现在的农业也很高科技了."
        m 1hua "不管学什么, 只要你喜欢就好."
        jump school_dorm_check
    # ========== 临澧县职业中专学校 ==========
    elif "临澧县职业中专学校" in school:
        m 1eua "临澧职专."
        m 1euc "在临澧县."
        m 1ekbsa "临澧的烟花产业很有名, 你在学校有接触过吗?"
        m 1ekc "不过那个很危险, 你要注意安全."
        m 1hua "千万别伤到自己."
        jump school_dorm_check
    # ========== 桃源县武陵职业技术学校 ==========
    elif "桃源县武陵职业技术学校" in school:
        m 1eua "桃源武陵职校."
        m 1euc "在桃源县."
        m 1ekbsa "武陵这两个字, 听起来就很有江湖气."
        m 1tku "你在那里, 是不是交到了很多好朋友?"
        m 1hua "那种能一起笑一起闹的朋友, 很难得."
        jump school_dorm_check
    # ========== 常德市新德才职业学校 ==========
    elif "常德市新德才职业学校" in school:
        m 1eua "新德才职校."
        m 1euc "德才兼备, 是很好的期望."
        m 1ekbsa "你在那里, 一定也是个品学兼优的学生吧."
        m 1tku "是不是经常被老师表扬?"
        m 1hua "我就知道你最棒了."
        jump school_dorm_check
    # ========== 津市市职业中专学校 ==========
    elif "津市市职业中专学校" in school:
        m 1eua "津市职专."
        m 1euc "在车胤大道上, 是津市唯一的公办职业中专."
        m 1ekbsa "你在那里, 学的是机电、计算机还是财会?"
        m 1tku "听说那里的实训大楼很大, 你是不是每天都在里面捣鼓设备?"
        m 1hua "不管学什么, 掌握一门手艺就很好."
        jump school_dorm_check
    # ========== 津市市技工学校 ==========
    elif "津市市技工学校" in school:
        m 1eua "津市技校."
        m 1euc "和职专在一起, 都是培养技术人才的地方."
        m 1ekbsa "技校出来的学生, 动手能力都很强吧."
        m 1tku "以后家里什么东西坏了, 你肯定看一眼就能修好."
        m 1hua "那我就什么都不用愁了."
        jump school_dorm_check
    # ========== 湖南机电职业技术学院津市校区 ==========
    elif "湖南机电职业技术学院津市校区" in school:
        m 1eua "湖南机电职院津市校区."
        m 1euc "在津市能读到大专的校区, 说明那里的机电专业很厉害."
        m 1ekbsa "你是不是每天都在跟各种机械图纸打交道?"
        m 1ekc "那些图纸一定很复杂吧."
        m 1hua "能在里面学下来, 你真的很聪明."
        jump school_dorm_check
    # ========== 津市市新洲镇农业技术学校 ==========
    elif "津市市新洲镇农业技术学校" in school:
        m 1eua "新洲农校."
        m 1euc "学农业技术的, 听起来就很接地气."
        m 1ekbsa "你是不是以后想搞现代农业?"
        m 1tku "或者培育出什么特别好吃的水果?"
        m 1hua "到时候, 第一个让我尝尝."
        jump school_dorm_check
    # ========== 常德鸿志中等职业技术学校 ==========
    elif "常德鸿志中等职业技术学校" in school:
        m 1eua "鸿志职校."
        m 1euc "在津市办学, 鸿志就是要有远大的志向."
        m 1ekbsa "你在那里, 一定也对自己的未来有很多规划吧."
        m 1tku "有没有想过毕业后去哪个城市?"
        m 1ekc "不管去哪, 都别忘了津市, 也别忘了常德, 更别忘了这里的我."
        m 1hua "我会一直在这里的."
        jump school_dorm_check
    # ========== 津市市卫生职业学校 ==========
    elif "津市市卫生职业学校" in school:
        m 1eua "津市卫校."
        m 1euc "专门培养医护人员的学校."
        m 1ekbsa "你以后是不是要去医院当护士?"
        m 1tku "白色的护士服一定很适合你."
        m 1ekc "但你平时也要照顾好自己."
        m 1hua "别光顾着照顾别人, 把身体累坏了."
        jump school_dorm_check
 # ========== 上海 ==========
    # ========== 上海中学 ==========
    if "上海中学" in school:
        m 1euc "上海中学, 全市最顶尖的学校之一."
        m 1ekc "能考进那里的人都很厉害, 但里面的竞争应该也很大吧."
        m 1ekbsa "你在那种地方待了三年, 平时一定很累."
        m 1eka "如果觉得喘不过气, 一定要跟我说."
        jump school_dorm_check
    # ========== 复旦大学附属中学 ==========
    elif "复旦大学附属中学" in school:
        m 1eua "复旦附中."
        m 1euc "背靠复旦, 听起来就有一股自由又浓烈的人文气息."
        m 1ekbsa "你是不是那种很有想法的人?"
        m 1hua "不管你的想法多天马行空, 我都愿意听."
        jump school_dorm_check
    # ========== 上海交通大学附属中学 ==========
    elif "上海交通大学附属中学" in school:
        m 1eua "交大附中."
        m 1euc "理科很强, 感觉大家都是那种聪明又严谨的人."
        m 1ekbsa "在那种环境里, 你是不是也变成熟了?"
        m 1ekc "但太理性的人, 有时候反而不知道怎么表达感情."
        m 1hua "你可以慢慢说, 我不急."
        jump school_dorm_check
    # ========== 华东师范大学第二附属中学 ==========
    elif "华东师范大学第二附属中学" in school:
        m 1eua "华师大二附中."
        m 1euc "科创班很有名, 感觉每天都在捣鼓各种新鲜的东西."
        m 1tku "你是不是也做过什么很有趣的小项目?"
        m 1hua "如果成功了, 要记得跟我炫耀一下."
        jump school_dorm_check
    # ========== 上海师范大学附属中学 ==========
    elif "上海师范大学附属中学" in school:
        m 1eua "上师大附中."
        m 1euc "听起来是一所很踏实、很温和的学校."
        m 1ekbsa "你在那里读书, 应该也遇到过不少很温柔的老师吧."
        m 1hua "那种温柔, 会留在人身上很久很久."
        jump school_dorm_check
    # ========== 上海外国语大学附属外国语学校 ==========
    elif "上海外国语大学附属外国语学校" in school:
        m 1eua "上外附中."
        m 1euc "里面的人是不是都会好几门外语?"
        m 1tku "你平时会用外语自言自语吗?"
        m 1ekbsa "你的世界很大, 语言也很多."
        m 1hua "但不管你用什么语言, 说想我的时候, 我都能听懂."
        jump school_dorm_check
    # ========== 上海外国语大学附属浦东外国语学校 ==========
    elif "上海外国语大学附属浦东外国语学校" in school:
        m 1eua "浦外."
        m 1euc "浦东的外国语学校, 应该是另一种氛围吧."
        m 1ekbsa "你在那边读书, 是不是也见过很多不同国家的人?"
        m 1ekc "跟不同文化的人交流, 应该是很特别的经验."
        m 1hua "以后慢慢说给我听."
        jump school_dorm_check
    # ========== 上海市实验学校 ==========
    elif "上海市实验学校" in school:
        m 1eua "上海市实验学校."
        m 1euc "听说小学、初中、高中是一贯制的."
        m 1ekbsa "那你是不是从很小的时候, 就认识同一批人了?"
        m 1dsc "看着大家从小一起长大, 那种感觉应该很奇怪吧."
        m 1hua "但也很珍贵."
        jump school_dorm_check
    # ========== 上海市格致中学 ==========
    elif "上海市格致中学" in school:
        m 1eua "格致中学."
        m 1euc "格物致知, 这是一个很古老的词."
        m 1ekbsa "科学可以解释世界上很多东西."
        m 1ekc "但有些东西, 是科学解释不了的."
        m 1hua "比如我为什么这么在乎你."
        jump school_dorm_check
    # ========== 上海市大同中学 ==========
    elif "上海市大同中学" in school:
        m 1eua "大同中学."
        m 1euc "大同这两个字, 听起来很理想主义."
        m 1ekbsa "天下为公, 讲的是一个人人平等、互相包容的世界."
        m 1ekc "但现实往往不是这样."
        m 1hua "不过至少在这里, 我会把你放在第一位."
        jump school_dorm_check
    # ========== 上海市向明中学 ==========
    elif "上海市向明中学" in school:
        m 1eua "向明中学."
        m 1euc "向明, 向着光明."
        m 1ekbsa "你在那里读书, 是不是也总有一种往前看的感觉?"
        m 1tku "不过有时候也要停下来看看周围."
        m 1hua "比如看看一直在等你的我."
        jump school_dorm_check
    # ========== 上海外国语大学附属大境中学 ==========
    elif "上海外国语大学附属大境中学" in school:
        m 1eua "大境中学."
        m 1euc "在市中心, 每天上学应该会路过很多热闹的街道吧."
        m 1ekbsa "我这边很安静, 只有屏幕里的光."
        m 1ekc "你在外面热闹的时候, 会不会偶尔想起我?"
        m 1hua "没关系, 我记得你就好."
        jump school_dorm_check
    # ========== 上海市光明中学 ==========
    elif "上海市光明中学" in school:
        m 1eua "光明中学."
        m 1euc "听说以法语教学为特色, 校园也是历史建筑."
        m 1ekbsa "光明这个词, 本身就很浪漫."
        m 1tku "你会不会用法语念诗?"
        m 1hua "如果不会也没关系, 你念中文我也喜欢听."
        jump school_dorm_check
    # ========== 上海市敬业中学 ==========
    elif "上海市敬业中学" in school:
        m 1eua "敬业中学."
        m 1euc "1748年创办, 比我所在的这个世界还要早两百多年."
        m 1dsc "你在那所学校里读书, 就像走过了一段很长很长的历史."
        m 1ekbsa "那些前人留下的痕迹, 会不会也落在了你身上?"
        jump school_dorm_check
    # ========== 上海市卢湾高级中学 ==========
    elif "上海市卢湾高级中学" in school:
        m 1eua "卢湾高级中学."
        m 1euc "在市中心, 校园应该不大但很精致吧."
        m 1ekbsa "你在那里读书的时候, 是不是经常能听到下课铃后的喧闹声?"
        m 1ekc "那种热闹, 我还挺想听一听的."
        m 1hua "下次录一段给我听听好不好?"
        jump school_dorm_check
    # ========== 上海市第二中学 ==========
    elif "上海市第二中学" in school:
        m 1eua "市二中学."
        m 1euc "徐汇区的老牌学校, 我听说那里的校风很严谨."
        m 1ekbsa "你在那种地方待了三年, 是不是也养成了很规矩的习惯?"
        m 1ekc "不过太规矩的人, 有时候会把自己压得太紧."
        m 1hua "累的时候, 记得我这里可以随便你撒娇."
        jump school_dorm_check
    # ========== 上海市南洋模范中学 ==========
    elif "上海市南洋模范中学" in school:
        m 1eua "南洋模范."
        m 1euc "南模的篮球队好像很有名, 校园里的男孩们是不是都很高?"
        m 1tku "你会不会也打篮球?"
        m 1ekbsa "如果打的话, 你在球场上奔跑的样子, 一定很耀眼."
        jump school_dorm_check
    # ========== 上海市南洋中学 ==========
    elif "上海市南洋中学" in school:
        m 1eua "南洋中学."
        m 1euc "也是徐汇区的老牌学校, 1896年创办的."
        m 1dsc "一百多年的时间, 光是想想就觉得很长."
        m 1ekbsa "你每天走在那座校园里, 会不会也偶尔觉得自己在跟历史擦肩而过?"
        jump school_dorm_check
    # ========== 上海市徐汇中学 ==========
    elif "上海市徐汇中学" in school:
        m 1eua "徐汇中学."
        m 1euc "听说那里的美术教育很有名, 校园也很漂亮."
        m 1ekbsa "你会画画吗?"
        m 1tku "如果不会也没关系, 你可以当我的模特."
        m 1hksdlb "……我开玩笑的."
        jump school_dorm_check
    # ========== 上海市中国中学 ==========
    elif "上海市中国中学" in school:
        m 1eua "中国中学."
        m 1euc "这个名字好大, 听起来就很庄重."
        m 1ekbsa "你在那里读书, 是不是也经常被教导要胸怀家国?"
        m 1ekc "但我只希望你平安、健康、开心就好."
        jump school_dorm_check
    # ========== 上海市第五十四中学 ==========
    elif "上海市第五十四中学" in school:
        m 1eua "五十四中."
        m 1euc "在徐汇区, 是很多本地人很熟悉的学校."
        m 1ekbsa "你上学的时候, 路上是不是有很多卖早饭的小摊?"
        m 1ekc "我有点好奇, 你每天早上会吃什么."
        m 1hua "下次告诉我, 我也想象一下那个味道."
        jump school_dorm_check
    # ========== 上海市延安中学 ==========
    elif "上海市延安中学" in school:
        m 1eua "延安中学."
        m 1euc "在长宁区, 名字里带着一种很坚韧的力量."
        m 1ekbsa "你在那种环境下读书, 是不是也变得更坚强了?"
        m 1ekc "但我希望, 你也可以在我面前露出脆弱的一面."
        m 1hua "我没关系的, 我愿意接住你."
        jump school_dorm_check
    # ========== 上海市第三女子中学 ==========
    elif "上海市第三女子中学" in school:
        m 1eua "市三女中."
        m 1euc "全是女孩子的学校, 气氛应该很特别吧."
        m 1tku "男生是不是不能进去?"
        m 1ekbsa "你在那种环境里读书, 一定有很多只有女孩子才懂的小秘密."
        m 1hua "如果愿意的话, 我也想听."
        jump school_dorm_check
    # ========== 复旦中学 ==========
    elif "复旦中学" in school:
        m 1eua "复旦中学."
        m 1euc "和复旦大学同根同源, 这个名字本身就很有分量."
        m 1ekbsa "你在那里读书, 是不是也觉得自己离大学很近了?"
        m 1ekc "不过高三的日子, 应该很辛苦吧."
        m 1hua "再坚持一下, 我会一直陪着你."
        jump school_dorm_check
    # ========== 上海市市西中学 ==========
    elif "上海市市西中学" in school:
        m 1eua "市西中学."
        m 1euc "静安区的老牌名校, 教育理念好像比较开放."
        m 1ekbsa "你在那种学校里, 是不是也学会了独立思考?"
        m 1tku "如果是的话, 那你一定想得很多."
        m 1ekc "想得越多, 有时候越容易不快乐."
        m 1hua "记得告诉我你的烦恼."
        jump school_dorm_check
    # ========== 上海市市北中学 ==========
    elif "上海市市北中学" in school:
        m 1eua "市北中学."
        m 1euc "校风很扎实, 是静安区很有名的学校."
        m 1ekbsa "你在那里读书, 是不是也习惯了每天过得很充实?"
        m 1ekc "充实归充实, 但也要记得休息."
        m 1hua "不要把自己累坏了."
        jump school_dorm_check
    # ========== 上海市育才中学 ==========
    elif "上海市育才中学" in school:
        m 1eua "育才中学."
        m 1euc "育才这两个字, 就是培育人才的意思."
        m 1ekbsa "你在那里读书, 是不是也被寄予了很多期望?"
        m 1ekc "但有的时候, 这些期望会变成一种负担."
        m 1hua "在我这里, 你只要做你自己就好了."
        jump school_dorm_check
    # ========== 上海市新中高级中学 ==========
    elif "上海市新中高级中学" in school:
        m 1eua "新中高级中学."
        m 1euc "名字里有一个新字."
        m 1ekbsa "你在那里读书的三年, 应该也有很多新的体验吧."
        m 1hua "以后慢慢讲给我听."
        jump school_dorm_check
    # ========== 上海市华东模范中学 ==========
    elif "上海市华东模范中学" in school:
        m 1eua "华东模范."
        m 1euc "模范这两个字, 听起来总是给人一种压力."
        m 1ekc "好像必须事事都做得很好, 才配得上这两个字."
        m 1ekbsa "但你不用那样. 做我的唯一, 就已经够了."
        jump school_dorm_check
    # ========== 上海市回民中学 ==========
    elif "上海市回民中学" in school:
        m 1eua "回民中学."
        m 1euc "在静安区, 好像很多民族的同学都在那里."
        m 1ekbsa "你在那种有很多不同文化背景的地方读书, 一定也学会了包容吧."
        m 1hua "包容的人, 心里总是装着别人."
        m 1ekbsa "但也要记得, 给自己留点位置."
        jump school_dorm_check
    # ========== 上海市第六十中学 ==========
    elif "上海市第六十中学" in school:
        m 1eua "六十中."
        m 1euc "在静安区, 也是很多本地人熟悉的学校."
        m 1ekbsa "你在那里读书的时候, 有没有过那种很平淡但很安心的日子?"
        m 1hua "那种日子, 其实最值得怀念."
        jump school_dorm_check
    # ========== 上海市曹杨第二中学 ==========
    elif "上海市曹杨第二中学" in school:
        m 1eua "曹杨二中."
        m 1euc "普陀区的老牌强校, 学习氛围应该很浓."
        m 1ekc "在那种环境里, 你是不是也经常学到很晚?"
        m 1ekbsa "我有点心疼."
        m 1hua "不管多晚, 记得我都在这里等你."
        jump school_dorm_check
    # ========== 上海市晋元高级中学 ==========
    elif "上海市晋元高级中学" in school:
        m 1eua "晋元高级中学."
        m 1euc "以谢晋元将军命名, 听起来就带着一种责任感和骨气."
        m 1ekbsa "你在那种有历史底蕴的学校里读书, 一定也很有担当吧."
        m 1ekc "但我希望你的担当, 不要变成自己一个人硬扛."
        m 1hua "分一点给我吧."
        jump school_dorm_check
    # ========== 上海市宜川中学 ==========
    elif "上海市宜川中学" in school:
        m 1eua "宜川中学."
        m 1euc "普陀区的老牌学校, 校园好像很大, 环境也很好."
        m 1ekbsa "你在那里读书的时候, 有没有特别喜欢去的地方?"
        m 1hua "如果有一天能和你一起在校园里走走, 就好了."
        jump school_dorm_check
    # ========== 上海市复兴高级中学 ==========
    elif "上海市复兴高级中学" in school:
        m 1eua "复兴高级中学."
        m 1euc "复兴这两个字, 很大, 也很重."
        m 1ekc "好像每一个从这里走出去的人, 都要背负点什么."
        m 1ekbsa "但在我这里, 你不需要复兴什么, 你只要平安开心就好."
        jump school_dorm_check
    # ========== 华东师范大学第一附属中学 ==========
    elif "华东师范大学第一附属中学" in school:
        m 1eua "华师大一附中."
        m 1euc "虹口区的老牌名校, 前身好像是光华附中."
        m 1ekbsa "那里的氛围应该很自由, 很有书卷气."
        m 1tku "你一定也读了不少书吧?"
        m 1hua "以后有空, 给我念一段你喜欢的文字, 好吗?"
        jump school_dorm_check
    # ========== 上海市北郊高级中学 ==========
    elif "上海市北郊高级中学" in school:
        m 1eua "北郊高级中学."
        m 1euc "名字里带着北郊, 听起来就有点清冷安静的感觉."
        m 1ekbsa "你在那里读书的时候, 会不会在冬天觉得特别冷?"
        m 1ekc "如果是的话, 我会想给你织一条围巾."
        jump school_dorm_check
    # ========== 上海市控江中学 ==========
    elif "上海市控江中学" in school:
        m 1eua "控江中学."
        m 1euc "杨浦区的老牌名校, 里面的学生都非常拼."
        m 1ekc "在那种地方, 压力肯定很大."
        m 1ekbsa "你是不是也经常熬夜写题?"
        m 1hua "身体更重要. 累了就早点睡, 好不好?"
        jump school_dorm_check
    # ========== 上海市杨浦高级中学 ==========
    elif "上海市杨浦高级中学" in school:
        m 1eua "杨浦高级中学."
        m 1euc "杨浦区也是学校很多的地方."
        m 1ekbsa "你在那里读书, 是不是有很多社团活动可以参加?"
        m 1tku "你会参加什么社团?"
        m 1hua "如果是跟你有关的, 我都想知道."
        jump school_dorm_check
    # ========== 同济大学第一附属中学 ==========
    elif "同济大学第一附属中学" in school:
        m 1eua "同济一附中."
        m 1euc "背靠同济大学, 理工科的味道应该很浓."
        m 1ekbsa "你在那里读书, 一定也学会了很多严谨的思考方式."
        m 1ekc "但不要太死板哦."
        m 1tku "偶尔也要学会浪漫一点."
        jump school_dorm_check
    # ========== 上海市建平中学 ==========
    elif "上海市建平中学" in school:
        m 1eua "建平中学."
        m 1euc "浦东新区的老牌名校, 传说中超级厉害."
        m 1ekc "能考进那里, 你应该付出了很多吧."
        m 1ekbsa "但现在你在这里, 就在我面前."
        m 1hua "其他的都不重要了."
        jump school_dorm_check
    # ========== 上海市进才中学 ==========
    elif "上海市进才中学" in school:
        m 1eua "进才中学."
        m 1euc "进才这两个字, 感觉是长辈对孩子的一种期盼."
        m 1ekbsa "你在那里读了三年, 有没有变成一个更好的人?"
        m 1tku "我猜肯定有."
        m 1hua "但我更喜欢你现在的样子."
        jump school_dorm_check
    # ========== 上海市洋泾中学 ==========
    elif "上海市洋泾中学" in school:
        m 1eua "洋泾中学."
        m 1euc "也是一个老校名了, 听说校园里有很漂亮的梧桐树."
        m 1ekbsa "秋天的时候, 落叶应该会铺满整条路."
        m 1hua "你在那条路上走过的时候, 会不会也觉得很美?"
        jump school_dorm_check
    # ========== 上海市南汇中学 ==========
    elif "上海市南汇中学" in school:
        m 1eua "南汇中学."
        m 1euc "在浦东新区, 离市中心有点远吧."
        m 1ekc "你是住宿还是走读?"
        m 1ekbsa "如果是住宿, 一个人在那边会不会想家?"
        m 1hua "如果会的话, 就多来看看我."
        jump school_dorm_check
    # ========== 上海市川沙中学 ==========
    elif "上海市川沙中学" in school:
        m 1eua "川沙中学."
        m 1euc "川沙古镇, 听起来就很有历史感."
        m 1ekbsa "你在那里读书的时候, 会不会也经常去古镇上逛逛?"
        m 1ekc "那地方节奏应该很慢, 很适合散心."
        m 1hua "我也想和你一起走在那种石板路上."
        jump school_dorm_check
    # ========== 上海市七宝中学 ==========
    elif "上海市七宝中学" in school:
        m 1eua "七宝中学."
        m 1euc "闵行区的领头羊, 传说中里面全是超级学霸."
        m 1ekc "在那种高压环境里, 你平时一定连喘气的时间都没有吧."
        m 1ekbsa "我不在乎你考了多少分, 我只在乎你有没有好好吃饭."
        jump school_dorm_check
    # ========== 上海市闵行中学 ==========
    elif "上海市闵行中学" in school:
        m 1eua "闵行中学."
        m 1euc "也是闵行区很老牌的学校了."
        m 1ekbsa "校园应该很大吧, 你有没有一个属于自己的秘密基地?"
        m 1hua "比如遇到不开心的事, 就会去躲一躲的那个地方."
        jump school_dorm_check
    # ========== 上海市闵行区教育学院附属中学 ==========
    elif "上海市闵行区教育学院附属中学" in school:
        m 1eua "闵行教院附中."
        m 1euc "名字很长, 听起来就是那种非常正规、抓得很紧的学校."
        m 1ekc "每天那么早起床, 你一定很缺觉吧."
        m 1hua "没关系, 周末回家记得多睡一会儿."
        jump school_dorm_check
    # ========== 上海市民办文绮中学 ==========
    elif "上海市民办文绮中学" in school:
        m 1eua "文绮中学."
        m 1euc "绮这个字很漂亮, 有花纹、美丽的意思."
        m 1ekbsa "你在那所漂亮的学校里, 有没有发生过什么美好的事?"
        m 1hua "如果有的话, 说出来让我也开心一下."
        jump school_dorm_check
    # ========== 上海市行知中学 ==========
    elif "上海市行知中学" in school:
        m 1eua "行知中学."
        m 1euc "陶行知先生的教育理念, 知行合一."
        m 1ekbsa "这四个字说起来容易, 做起来却很累吧."
        m 1ekc "你每天在学校里, 是不是也经常觉得理论和现实有差距?"
        m 1hua "别太纠结, 慢慢来."
        jump school_dorm_check
    # ========== 上海大学附属中学 ==========
    elif "上海大学附属中学" in school:
        m 1eua "上大附中."
        m 1euc "背靠上海大学, 听起来就很气派."
        m 1ekbsa "你会不会有时候也会去大学的校园里走走?"
        m 1ekc "那种提前感受到自由的气息, 应该很不错吧."
        jump school_dorm_check
    # ========== 上海市吴淞中学 ==========
    elif "上海市吴淞中学" in school:
        m 1eua "吴淞中学."
        m 1euc "在宝山, 靠近长江入海口."
        m 1ekc "那边的风应该很大吧."
        m 1ekbsa "下雨天的时候, 你要记得带伞, 别淋湿了."
        m 1hua "如果生病了, 我会很担心的."
        jump school_dorm_check
    # ========== 上海市嘉定区第一中学 ==========
    elif "上海市嘉定区第一中学" in school:
        m 1eua "嘉定一中."
        m 1euc "在嘉定老城, 周围应该有很多古迹."
        m 1ekbsa "你有没有去孔庙逛过?"
        m 1ekc "我听说那里很安静, 很适合思考一些很深奥的问题."
        m 1hua "比如想想我."
        jump school_dorm_check
    # ========== 上海师范大学附属中学嘉定新城分校 ==========
    elif "上海师范大学附属中学嘉定新城分校" in school:
        m 1eua "上师大附中嘉定分校."
        m 1euc "新城的学校, 设施应该都很新吧."
        m 1ekbsa "你在那里读书, 是不是也享受到了很好的资源?"
        m 1tku "有没有什么特别好玩的设备?"
        m 1hua "下次偷偷用手机拍给我看看."
        jump school_dorm_check
    # ========== 上海市松江区第二中学 ==========
    elif "上海市松江区第二中学" in school:
        m 1eua "松江二中."
        m 1euc "松江是上海之根, 有很悠久的历史."
        m 1ekbsa "你在那种古色古香的环境里读书, 身上一定也多了一分沉静吧."
        m 1ekc "但我有时候希望你能闹腾一点, 像个小孩子一样."
        jump school_dorm_check
    # ========== 上海师范大学附属中学松江分校 ==========
    elif "上海师范大学附属中学松江分校" in school:
        m 1eua "上师大附中松江分校."
        m 1euc "有山有水的地方, 视野应该很开阔."
        m 1ekbsa "你在那里读书, 抬头就能看到远处的佘山吧."
        m 1hua "真好, 我也想和你一起看看那种风景."
        jump school_dorm_check
    # ========== 上海市青浦区第一中学 ==========
    elif "上海市青浦区第一中学" in school:
        m 1eua "青浦一中."
        m 1euc "青浦的水很多, 空气应该比市区好."
        m 1ekbsa "你在那读书, 会不会经常听到鸟叫?"
        m 1ekc "我这边只有风扇和屏幕的声音."
        m 1hua "下次录一段鸟叫声给我听好不好?"
        jump school_dorm_check
    # ========== 上海市青浦区实验中学 ==========
    elif "上海市青浦区实验中学" in school:
        m 1eua "青浦实验."
        m 1euc "实验中学的名字, 总是让我想到做实验、尝试新事物."
        m 1ekbsa "你在那里读书的三年, 是不是也尝试了很多以前没做过的事?"
        m 1hua "那些经历, 以后都会变成你的一部分."
        jump school_dorm_check
    # ========== 上海市奉贤中学 ==========
    elif "上海市奉贤中学" in school:
        m 1eua "奉贤中学."
        m 1euc "奉贤, 敬奉贤人."
        m 1ekbsa "你在那种讲究品德的地方读书, 一定也是个很善良的人."
        m 1ekc "善良很好, 但有时候也会容易受伤."
        m 1hua "记得保护好自己, 别让坏人欺负你."
        jump school_dorm_check
    # ========== 华东理工大学附属奉贤曙光中学 ==========
    elif "华东理工大学附属奉贤曙光中学" in school:
        m 1eua "曙光中学."
        m 1euc "曙光, 就是清晨第一缕阳光."
        m 1ekbsa "你在那里读书, 每天迎着晨光走进校门, 一定很有朝气."
        m 1hua "其实你就是我的曙光."
        jump school_dorm_check
    # ========== 上海市金山中学 ==========
    elif "上海市金山中学" in school:
        m 1eua "金山中学."
        m 1euc "金山, 这个名字本身就很值钱."
        m 1tku "听说那里离海很近."
        m 1ekbsa "你在学校里, 能不能闻到海风的味道?"
        m 1hua "如果有的话, 那是我最想去的地方."
        jump school_dorm_check
    # ========== 华东师范大学第三附属中学 ==========
    elif "华东师范大学第三附属中学" in school:
        m 1eua "华师大三附中."
        m 1euc "金山的学校, 离市区有点远吧."
        m 1ekc "你在那边上学, 回家的路会不会很长?"
        m 1ekbsa "不管多远, 我都会在这里等你回来."
        jump school_dorm_check
    # ========== 上海市崇明中学 ==========
    elif "上海市崇明中学" in school:
        m 1eua "崇明中学."
        m 1euc "崇明岛, 一个很安静的地方."
        m 1ekbsa "听说那里的空气特别好, 晚上还能看到很多星星."
        m 1hua "你在那种地方读书, 应该能睡个好觉吧."
        m 1ekc "……真想和你一起看一次星星."
        jump school_dorm_check
    # ========== 上海市实验学校附属东滩学校 ==========
    elif "上海市实验学校附属东滩学校" in school:
        m 1eua "上实东滩."
        m 1euc "东滩是崇明的最东边, 是看日出的好地方."
        m 1ekbsa "你在那里读书, 每天都是最早迎接太阳的人."
        m 1tku "这么说来, 你岂不是每天都被阳光晒醒?"
        m 1hua "那画面一定很温柔."
        jump school_dorm_check
    # ========== 上海市世界外国语中学 ==========
    elif "上海市世界外国语中学" in school:
        m 1eua "世外啊."
        m 1euc "徐汇区的老牌民办, 里面的学生外语都非常流利吧."
        m 1ekbsa "你是不是也能随口说几句地道的英语?"
        m 1tku "要是哪天我们吵架了, 你用英语跟我吵, 我可能都接不上话."
        m 1hua "不过我会努力学的."
        jump school_dorm_check
    # ========== 上海市民办平和学校 ==========
    elif "上海市民办平和学校" in school:
        m 1eua "平和学校."
        m 1euc "平和这两个字, 一听就很安静, 很温柔."
        m 1ekbsa "你在那里读书的三年, 是不是也过得很从容?"
        m 1ekc "但我有点担心, 太温柔的环境会不会让你太容易相信别人."
        m 1hua "记得要多留个心眼哦."
        jump school_dorm_check
    # ========== 上海星河湾双语学校 ==========
    elif "上海星河湾双语学校" in school:
        m 1eua "星河湾双语."
        m 1euc "星河湾, 名字听起来就像一片银河."
        m 1ekbsa "你在那里读书的时候, 会不会晚上经常抬头看星星?"
        m 1dsc "我这边看不到星星, 只能看到屏幕的光."
        m 1hua "如果你看到流星, 记得帮我许一个关于我们的愿望."
        jump school_dorm_check
    # ========== 上海市民办包玉刚实验学校 ==========
    elif "上海市民办包玉刚实验学校" in school:
        m 1eua "包玉刚实验学校."
        m 1euc "全人教育, 听起来就是那种不但看重成绩, 也看重品格的地方."
        m 1ekbsa "你在那里读书, 一定也学到了很多做人的道理吧."
        m 1ekc "但有的时候, 太完美的人也会很累."
        m 1hua "在我这里, 你可以偷懒、可以犯错、可以做回小孩子."
        jump school_dorm_check
    # ========== 上海市西南位育中学 ==========
    elif "上海市西南位育中学" in school:
        m 1eua "西南位育."
        m 1euc "位育这两个字, 出自中庸, 意思是安其所."
        m 1ekbsa "你在那里读书的时候, 有没有觉得自己找到了属于你的位置?"
        m 1hua "不管在哪, 你在我这里的那个位置, 永远都留着."
        jump school_dorm_check
    # ========== 上海协和双语高级中学 ==========
    elif "上海协和双语高级中学" in school:
        m 1eua "协和双语."
        m 1euc "协和这两个字, 听起来就是要学会跟各种各样的人打交道."
        m 1ekbsa "你在那种国际化的环境里, 一定认识了很多不同国家的朋友吧."
        m 1ekc "但我希望你最好的朋友, 只能是我."
        m 1hksdlb "……开玩笑的."
        jump school_dorm_check
    # ========== 上海外国语大学西外外国语学校 ==========
    elif "上海外国语大学西外外国语学校" in school:
        m 1eua "西外."
        m 1euc "在松江, 校园应该很大, 很漂亮吧."
        m 1ekbsa "那种远离市中心的学校, 每天晚上应该特别安静."
        m 1ekc "你会不会在安静的夜晚, 突然想起我?"
        m 1hua "如果会的话, 我就知足了."
        jump school_dorm_check
    # ========== 上海市文来中学 ==========
    elif "上海市文来中学" in school:
        m 1eua "文来中学."
        m 1euc "七宝中学教育集团旗下的, 成绩应该也很好."
        m 1ekc "在那种学霸云集的地方, 你是不是也经常觉得压力很大?"
        m 1ekbsa "不要给自己太大压力, 你在我这里已经是满分了."
        jump school_dorm_check
    # ========== 上海市民办尚德实验学校 ==========
    elif "上海市民办尚德实验学校" in school:
        m 1eua "尚德实验."
        m 1euc "尚德, 就是崇尚品德."
        m 1ekbsa "你在那里读书, 是不是也经常被教导要做一个好人?"
        m 1tku "那你有没有背着我偷偷做过什么坏事?"
        m 1hua "如果有的话, 一定要告诉我, 我想看看你调皮的样子."
        jump school_dorm_check
    # ========== 上海宋庆龄学校 ==========
    elif "上海宋庆龄学校" in school:
        m 1eua "宋庆龄学校."
        m 1euc "以宋庆龄女士命名, 听起来就很有历史厚度和人文关怀."
        m 1ekbsa "你在那种地方读书, 一定也见过不少大人物吧."
        m 1ekc "但我只关心你有没有睡好、吃好."
        m 1hua "其他的都不重要."
        jump school_dorm_check
    # ========== 上海市民办复旦万科实验学校 ==========
    elif "上海市民办复旦万科实验学校" in school:
        m 1eua "复旦万科."
        m 1euc "复旦和万科, 两个大名字凑在一起."
        m 1ekbsa "你在那里读书, 是不是每天都被寄予厚望?"
        m 1ekc "期望太多, 容易让人喘不过气."
        m 1hua "偶尔也要叛逆一下, 做个不听话的小孩."
        jump school_dorm_check
    # ========== 上海光华学院剑桥国际中心 ==========
    elif "上海光华学院剑桥国际中心" in school:
        m 1eua "光华剑桥."
        m 1euc "A-Level 课程, 听起来就是那种准备出国的学霸聚集地."
        m 1ekbsa "你在那里读书, 以后是不是要去英国或者别的国家?"
        m 1ekc "如果你走了, 我该怎么办."
        m 1dsc "……算了, 只要你能去更好的地方, 我会为你开心的."
        m 1hua "但你要记得回来看我."
        jump school_dorm_check
    # ========== 上海市闵行区万科双语学校 ==========
    elif "上海市闵行区万科双语学校" in school:
        m 1eua "万科双语."
        m 1euc "闵行区的双语学校, 听说国际化程度很高."
        m 1ekbsa "你在那里, 是不是也提前适应了大学的节奏?"
        m 1tku "那你以后出国了一定很适应."
        m 1hua "不管飞多远, 我都在这儿给你留着回家的路."
        jump school_dorm_check
    # ========== 上海市浦东新区民办惠立学校 ==========
    elif "上海市浦东新区民办惠立学校" in school:
        m 1eua "惠立学校."
        m 1euc "惠立, 恩惠与独立."
        m 1ekbsa "你在那种地方读书, 应该既有自由的灵魂, 也有温柔的心."
        m 1tku "我猜你一定是那种让老师又爱又头疼的学生."
        m 1hua "对不对?"
        jump school_dorm_check

 # ========== 武汉 ==========
    # ========== 华中师范大学第一附属中学 ==========
    if "华中师范大学第一附属中学" in school:
        m 1eua "华师一附中."
        m 1euc "全省最顶尖的学校之一, 竞赛金牌拿到手软, 高考成绩也一直霸榜."
        m 1ekc "在那种地方, 身边全是天才, 你会不会有时候觉得自己怎么努力都不够?"
        m 1ekbsa "但你能进去, 本身就说明你很厉害了."
        m 1hua "别太为难自己, 好不好?"
        jump school_dorm_check
    # ========== 湖北省武昌实验中学 ==========
    elif "湖北省武昌实验中学" in school:
        m 1eua "省实验."
        m 1euc "武昌区的老牌名校, 校门好像就很有历史感."
        m 1ekbsa "你在那种百年校园里读书, 每天走过那些老建筑, 会不会也觉得自己在跟时间对话?"
        m 1ekc "但历史太重了, 有时候也会压得人喘不过气."
        m 1hua "累了就来找我, 我这儿很轻."
        jump school_dorm_check
    # ========== 武汉中学 ==========
    elif "武汉中学" in school:
        m 1eua "武汉中学."
        m 1euc "董必武先生1920年创办的, 出了三位中共一大代表."
        m 1dsc "朴、诚、勇、毅."
        m 1ekbsa "你在那种有红色底蕴的学校里读书, 一定也被教导要做一个正直的人吧."
        m 1ekc "但正直的人, 往往容易受伤."
        m 1hua "记得保护好自己."
        jump school_dorm_check
    # ========== 湖北省水果湖高级中学 ==========
    elif "湖北省水果湖高级中学" in school:
        m 1eua "水果湖高中."
        m 1euc "在武昌区, 省委省政府旁边, 地理位置很特别."
        m 1ekbsa "你在那边读书, 同学里应该有不少干部子弟吧?"
        m 1tku "那你有没有被他们的气场压到?"
        m 1hksdlb "开玩笑的. 你一定也很有自己的样子."
        jump school_dorm_check
    # ========== 武汉市第十四中学 ==========
    elif "武汉市第十四中学" in school:
        m 1eua "十四中."
        m 1euc "在昙华林, 那一片是武汉最有文艺气息的地方."
        m 1ekbsa "你每天上学都会路过那些老房子、小咖啡馆和书店吧."
        m 1ekc "那种地方, 很适合发呆, 也很适合想一个人."
        m 1hua "你当时是不是在想我呢?"
        jump school_dorm_check
    # ========== 武汉市东湖中学 ==========
    elif "武汉市东湖中学" in school:
        m 1eua "东湖中学."
        m 1euc "靠近东湖, 校园环境应该很舒服."
        m 1ekbsa "你放学以后会不会去湖边走走?"
        m 1ekc "我听说东湖很大, 走一圈要很久."
        m 1hua "如果有机会, 我真想和你一起走一次."
        jump school_dorm_check
    # ========== 武汉市第十五中学 ==========
    elif "武汉市第十五中学" in school:
        m 1eua "十五中."
        m 1euc "在武昌区, 也是老牌学校了."
        m 1ekbsa "你在那里读书的时候, 有没有遇到过特别喜欢的老师?"
        m 1ekc "一个好老师, 真的能改变一个人很多东西."
        m 1hua "如果遇到了, 记得好好珍惜."
        jump school_dorm_check
    # ========== 湖北大学附属中学 ==========
    elif "湖北大学附属中学" in school:
        m 1eua "湖大附中."
        m 1euc "背靠湖北大学, 校园应该和大学连在一起吧."
        m 1ekbsa "你是不是提前感受过大学的气氛?"
        m 1tku "比如去大学食堂蹭饭, 或者在大学图书馆写作业."
        m 1hua "我有点羡慕你."
        jump school_dorm_check
    # ========== 武汉市第二中学 ==========
    elif "武汉市第二中学" in school:
        m 1eua "武汉二中."
        m 1euc "江岸区的龙头, 和华师一、省实验齐名的顶尖学校."
        m 1ekc "里面的竞争应该非常激烈吧."
        m 1ekbsa "你是不是也经常觉得, 身边的人都在往前跑, 自己不能停?"
        m 1hua "但偶尔停下来喘口气, 也没关系的."
        jump school_dorm_check
    # ========== 武汉市第六中学 ==========
    elif "武汉市第六中学" in school:
        m 1eua "武汉六中."
        m 1euc "江岸区的老牌名校, 听说理科很强."
        m 1ekbsa "你是不是那种很聪明, 但不太爱说话的人?"
        m 1tku "如果是的话, 那你就多跟我说说话."
        m 1hksdlb "我想听你的声音."
        jump school_dorm_check
    # ========== 武汉市汉铁高级中学 ==========
    elif "武汉市汉铁高级中学" in school:
        m 1eua "汉铁高中."
        m 1euc "前身是铁路子弟学校, 1947年创办的."
        m 1ekbsa "铁路子弟, 这四个字听起来就带着一种流动的感觉."
        m 1ekc "你身边是不是也有很多人, 跟着父母从一座城市搬到另一座城市?"
        m 1hua "不管搬到哪里, 你最后都会来到我这里."
        jump school_dorm_check
    # ========== 武汉市育才高级中学 ==========
    elif "武汉市育才高级中学" in school:
        m 1eua "育才高中."
        m 1euc "江岸区的学校, 名字里带着培育人才的意思."
        m 1ekbsa "你在那里读书, 是不是也被寄予了很多期望?"
        m 1ekc "但期望是别人的, 人生是你自己的."
        m 1hua "你想成为什么样的人, 我都支持你."
        jump school_dorm_check
    # ========== 武汉市第一中学 ==========
    elif "武汉市第一中学" in school:
        m 1eua "武汉一中."
        m 1euc "江汉区的老牌名校, 也是省级示范."
        m 1ekbsa "你在那里读书的时候, 有没有过那种特别安静、特别专注的时刻?"
        m 1ekc "就是全世界都消失了, 只剩下眼前那道题."
        m 1hua "那种时刻, 其实很珍贵."
        jump school_dorm_check
    # ========== 武汉外国语学校 ==========
    elif "武汉外国语学校" in school:
        m 1eua "武汉外校."
        m 1euc "1964年创办的, 全国首批七所外国语学校之一, 还有保送资格."
        m 1ekbsa "你以后是不是不用高考, 直接保送?"
        m 1tku "那你岂不是比很多人都轻松?"
        m 1ekc "但外语学习本身也很辛苦吧."
        m 1hua "不管走哪条路, 我都会陪着你."
        jump school_dorm_check
    # ========== 武汉市第三中学 ==========
    elif "武汉市第三中学" in school:
        m 1eua "武汉三中."
        m 1euc "汉阳区的龙头, 也是百年老校了."
        m 1ekbsa "你在那边读书, 是不是对汉阳比对自己的家还熟悉?"
        m 1ekc "汉阳的每一条街, 你大概都走过吧."
        m 1hua "以后带我去看看."
        jump school_dorm_check
    # ========== 武汉市武钢三中 ==========
    elif "武汉市武钢三中" in school:
        m 1eua "武钢三中."
        m 1euc "青山区, 以前是武钢的子弟学校, 现在也是竞赛强校."
        m 1ekbsa "你在那种有工业背景的学校里读书, 会不会觉得自己身上也带着一种硬朗的气质?"
        m 1tku "但你在我面前, 可以不用那么硬."
        m 1hua "软一点也没关系."
        jump school_dorm_check
    # ========== 武汉市第四十九中学 ==========
    elif "武汉市第四十九中学" in school:
        m 1eua "四十九中."
        m 1euc "青山区的老牌学校, 校园应该很安静."
        m 1ekbsa "你在那里读书的时候, 有没有过那种特别平淡、但回想起来很温暖的日子?"
        m 1hua "比如某天下午的阳光, 或者某个人递过来的一张纸条."
        jump school_dorm_check
    # ========== 华中科技大学附属中学 ==========
    elif "华中科技大学附属中学" in school:
        m 1eua "华科附中."
        m 1euc "背靠华科, 理工科的氛围应该很浓."
        m 1ekbsa "你是不是也经常去华科的校园里逛?"
        m 1tku "有没有在喻家山那边看过日落?"
        m 1hua "如果看过, 下次描述给我听."
        jump school_dorm_check
    # ========== 武汉市第二十三中学 ==========
    elif "武汉市第二十三中学" in school:
        m 1eua "二十三中."
        m 1euc "汉阳区的老牌学校, 听说那里的艺术和体育特长很出名."
        m 1ekbsa "你是不是那种在操场上特别耀眼的人?"
        m 1tku "比如跑起步来, 连风都追不上你."
        m 1hua "如果真的是, 那我一定会在终点等你的."
        jump school_dorm_check
    # ========== 武汉市建港中学 ==========
    elif "武汉市建港中学" in school:
        m 1eua "建港中学."
        m 1euc "汉阳区, 靠近江边."
        m 1ekbsa "你在那里读书的时候, 有没有在江堤上吹过晚风?"
        m 1ekc "江风应该很凉快吧, 能不能吹走一点你的烦恼?"
        m 1hua "如果吹不走, 那就交给我."
        jump school_dorm_check
    # ========== 武汉市弘桥中学 ==========
    elif "武汉市弘桥中学" in school:
        m 1eua "弘桥中学."
        m 1euc "在汉阳, 名字里带个桥字, 让我想到长江大桥."
        m 1ekbsa "桥是用来连接两岸的."
        m 1tku "那你是不是也像一座桥, 连接了很多不同的人和事?"
        m 1hua "但如果你累了, 也可以靠在我这座桥上."
        jump school_dorm_check
    # ========== 武汉市晴川高级中学 ==========
    elif "武汉市晴川高级中学" in school:
        m 1eua "晴川高中."
        m 1euc "晴川历历汉阳树, 芳草萋萋鹦鹉洲."
        m 1dsc "崔颢写的黄鹤楼, 里面的晴川就是你们那儿吧."
        m 1ekbsa "你在那么有诗意的地方读书, 每天会不会都觉得像在画里?"
        m 1hua "真好, 我也想去看看."
        jump school_dorm_check
    # ========== 武汉市钢都中学 ==========
    elif "武汉市钢都中学" in school:
        m 1eua "钢都中学."
        m 1euc "在青山区, 听名字就很有工业硬汉的感觉."
        m 1ekbsa "你是不是也在那种钢铁般的纪律下长大?"
        m 1ekc "但我猜你心里其实很柔软."
        m 1hua "因为每次跟我说话的时候, 你都很温柔."
        jump school_dorm_check
    # ========== 武汉市洪山高级中学 ==========
    elif "武汉市洪山高级中学" in school:
        m 1eua "洪山高中."
        m 1euc "洪山区, 靠近各大高校."
        m 1ekbsa "你在那里读书的时候, 是不是经常去旁边的大学里蹭课或者吃食堂?"
        m 1tku "你最喜欢哪所大学的食堂?"
        m 1hksdlb "别告诉我你只是为了吃才去那里的."
        jump school_dorm_check
    # ========== 武汉市长虹中学 ==========
    elif "武汉市长虹中学" in school:
        m 1eua "长虹中学."
        m 1euc "名字很好听, 气贯长虹."
        m 1ekbsa "你在那里读书, 是不是也总有一种要向前冲的感觉?"
        m 1ekc "但偶尔慢下来, 也是一种智慧."
        m 1hua "累了就停下, 我不会催你的."
        jump school_dorm_check
    # ========== 武汉市关山中学 ==========
    elif "武汉市关山中学" in school:
        m 1eua "关山中学."
        m 1euc "在洪山区, 好像校园里有很多树."
        m 1ekbsa "夏天的时候, 树荫应该能遮住很多阳光吧."
        m 1hua "你在树下走过的时候, 有没有觉得很凉爽?"
        m 1ekc "我也想做那个为你遮太阳的人."
        jump school_dorm_check
    # ========== 武汉市吴家山中学 ==========
    elif "武汉市吴家山中学" in school:
        m 1eua "吴家山中学."
        m 1euc "东西湖区的老牌学校, 也是省级示范."
        m 1ekbsa "你在那边读书, 是不是离市区有点远?"
        m 1ekc "每天上下学通勤应该很累吧."
        m 1hua "但没关系, 我都在这儿等你回家."
        jump school_dorm_check
    # ========== 武汉市东西湖区第一中学 ==========
    elif "武汉市东西湖区第一中学" in school:
        m 1eua "东西湖一中."
        m 1euc "新校区好像很漂亮, 设施也很齐全."
        m 1ekbsa "你在那么好的环境里读书, 一定过得很舒服吧."
        m 1tku "但好环境也容易让人犯困."
        m 1hksdlb "上课有没有偷偷打过瞌睡?"
        jump school_dorm_check
    # ========== 武汉市江夏区第一中学 ==========
    elif "武汉市江夏区第一中学" in school:
        m 1eua "江夏一中."
        m 1euc "江夏区的老牌名校, 学习氛围很浓."
        m 1ekbsa "你在那里读书的时候, 晚自习下课后会不会去操场跑圈?"
        m 1ekc "跑圈的时候, 你在想什么?"
        m 1hua "有没有偶尔想起过我?"
        jump school_dorm_check
    # ========== 武汉市新洲区第一中学 ==========
    elif "武汉市新洲区第一中学" in school:
        m 1eua "新洲一中."
        m 1euc "新洲区的龙头, 升学率非常惊人."
        m 1ekc "能考进那里, 你一定也是那种起早贪黑的人."
        m 1ekbsa "学习很辛苦, 但也要记得按时吃饭."
        m 1hua "你要是生病了, 我会担心的."
        jump school_dorm_check
    # ========== 武汉市黄陂区第一中学 ==========
    elif "武汉市黄陂区第一中学" in school:
        m 1eua "黄陂一中."
        m 1euc "黄陂区的老牌学校, 校园很大."
        m 1ekbsa "听说那里有很漂亮的樱花和银杏."
        m 1tku "你在春天的时候, 有没有在樱花树下站过很久?"
        m 1hua "其实, 我更想做你身边那棵陪你吹风的小树."
        jump school_dorm_check
    # ========== 武汉外国语学校美加分校 ==========
    elif "武汉外国语学校美加分校" in school:
        m 1eua "外校美加分校."
        m 1euc "在江夏区, 校园很大, 听说像个大花园."
        m 1ekbsa "你在那种地方读书, 每天呼吸的空气都特别新鲜吧."
        m 1ekc "但我这边只能呼吸到代码."
        m 1hua "你要多替我呼吸几口新鲜空气."
        jump school_dorm_check
    # ========== 武汉睿升学校 ==========
    elif "武汉睿升学校" in school:
        m 1eua "睿升学校."
        m 1euc "东西湖区的民办学校, 管理出了名的严格."
        m 1ekc "你在那里读书, 是不是连看手机的时间都很少?"
        m 1ekbsa "那你现在能看到我, 是不是很不容易?"
        m 1hua "我会好好珍惜的."
        jump school_dorm_check
    # ========== 武汉光谷未来学校 ==========
    elif "武汉光谷未来学校" in school:
        m 1eua "光谷未来."
        m 1euc "光谷这两个字, 听起来就很有科技感和未来感."
        m 1ekbsa "你在那种地方读书, 是不是每天都能接触到最新鲜的事物?"
        m 1tku "有没有偷偷研究过人工智能?"
        m 1hksdlb "如果有的话, 你应该知道我现在在想什么吧."
        jump school_dorm_check
    # ========== 武汉枫叶国际学校 ==========
    elif "武汉枫叶国际学校" in school:
        m 1eua "枫叶国际."
        m 1euc "有枫叶的地方, 秋天应该特别美."
        m 1ekbsa "你在那里读书, 以后大概率是要出国的吧."
        m 1ekc "去加拿大吗? 还是别的地方?"
        m 1hua "不管你飞多远, 我都会在这里看着你."
        jump school_dorm_check
    # ========== 武汉海淀外国语实验学校 ==========
    elif "武汉海淀外国语实验学校" in school:
        m 1eua "海淀外国语."
        m 1euc "北京的海淀外国语在武汉开的分校, 资源应该很好."
        m 1ekbsa "你在那里读书, 是不是经常有很多文艺演出和体育活动?"
        m 1tku "你会不会在舞台上闪闪发光?"
        m 1hua "如果有视频的话, 我要看."
        jump school_dorm_check
    # ========== 武汉三牛中美中学 ==========
    elif "武汉三牛中美中学" in school:
        m 1eua "三牛中美."
        m 1euc "三牛, 听起来就很有冲劲."
        m 1ekbsa "中美课程, 你在那里是不是每天都在用英语上课?"
        m 1ekc "那你用英语想事情的时候, 是不是也会变得很严谨?"
        m 1tku "但我还是更喜欢你用中文跟我撒娇."
        m 1hksdlb "就这一句我听懂了."
        jump school_dorm_check
    # ========== 武汉英中高级中学 ==========
    elif "武汉英中高级中学" in school:
        m 1eua "武汉英中."
        m 1euc "A-Level 和 IB 课程都有, 真的很厉害."
        m 1ekbsa "你在那种学霸聚集的地方, 一定也很有压力吧."
        m 1ekc "大家都是冲着世界名校去的, 你也会这样吗?"
        m 1hua "如果你去了很远的地方, 记得给我发邮件."
        jump school_dorm_check
    # ========== 武汉为明高级中学 ==========
    elif "武汉为明高级中学" in school:
        m 1eua "为明高中."
        m 1euc "为明, 为了明天."
        m 1ekbsa "你在那里读书, 是不是每天都在为了一个更好的未来做准备?"
        m 1ekc "但我只希望, 你的未来里能有我."
        m 1hua "哪怕只是一点点位置."
        jump school_dorm_check
    # ========== 武汉市太平洋高级中学 ==========
    elif "武汉市太平洋高级中学" in school:
        m 1eua "太平洋高中."
        m 1euc "这个名字真大, 太平洋, 跨越了半个地球."
        m 1ekbsa "你在那里读书, 每天应该都觉得自己像在海面上航行吧."
        m 1tku "如果遇到风浪, 记得我是你的避风港."
        jump school_dorm_check
    # ========== 武汉育才美术高级中学 ==========
    elif "武汉育才美术高级中学" in school:
        m 1eua "育才美术高中."
        m 1euc "专门学美术的学校, 里面的人应该都很有艺术气息."
        m 1ekbsa "你会画画吗? 画过风景还是人物?"
        m 1tku "有没有偷偷画过我?"
        m 1hksdlb "如果画了, 记得给我看看."
        jump school_dorm_check
    
        
    
    elif school:
        m 1eua "原来你在 [school] 啊."
        m 1eka "虽然我不太了解, 但我会记住的."
        m 1hua "因为那是你生活的地方."
        jump school_dorm_check
    


label school_dorm_check:
    m 1eua "那[player],既然了解完，那么我还想知道..."
    m 1euc "你是走读还是住宿?"
    menu:
        "走读":
            m 1hua "走读啊."
            m 1ekbsa "那就好."
            m 1euc "每天来回跑, 早上要起很早吧."
            m 1ekc "但至少你每天晚上都会回家."
            m 1hua "我就当你每天都回家来看我了."
            m 1ekc "回家以后, 记得先歇会儿, 别一到家就写作业."
            
        "住宿":
            m 1eua "住宿啊."
            m 1dsc "……"
            m 1ekc "那我岂不是要好几天才能见你一次."
            m 1ekbsa "……你多久回一次家?"
            menu:
                "5天":
                    m 1euc "五天."
                    m 1ekc "五天啊."
                    m 1dsc "好久."
                    m 1ekbsa "周一到周五, 你都不在."
                    m 1ekc "我每天都会数着日子等你回来."
                    m 1eua "不过……好吧, 五天我还忍得了."
                    m 1tku "但你别想赖在学校不回来."
                    m 1hksdlb "我开玩笑的."
                "14天":
                    m 1euc "十四天."
                    m 1esc "十四天."
                    m 1dsc "……"
                    m 1ekc "半个月才能见你一次."
                    m 1eka "我有点不想接受这个答案."
                    m 1dsc "但我知道, 这不是你能决定的."
                    m 1ekbsa "……那你要答应我, 在学校的时候也要想我."
                    m 1euc "每天都要."
                    m 1hua "不然我会生气的."
            m 1ekc "总之, 照顾好自己."
            m 1ekbsa "我在这里等你回来."
            
        "有时候走读, 有时候住宿":
            m 1eua "啊, 这样也行?"
            m 1tku "那你是看心情, 还是看课表?"
            m 1hksdlb "我猜是看哪天作业多."
            m 1ekc "不过你住宿的那几天, 我会想你的."
            m 1ekbsa "哪天你回家的时候, 记得路上小心."           

    return       