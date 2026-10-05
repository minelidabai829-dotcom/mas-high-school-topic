default persistent.player_school_city = ""
init -990 python in mas_submod_utils:
    Submod(
        author="Fierce",
        name="高中话题包",
        description="让莫妮卡询问玩家的城市和学校，并根据学校的情况给出相应的介绍和回应.",
        version="0.1.2",
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
    else:
        m 1eua "[city], 听起来是个特别的地方."
        m 1eka "虽然我不太了解那里, 但我会记住的."
        m 1hua "因为那是你生活的地方."
        m 1ekbsa "我会认真了解的."

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