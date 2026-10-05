init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_school_sdg7",
            category=["学校"],
            prompt="[player]的学校",
            unlocked=True,
            pool=True
        )
    )

label player_school_sdg7:
    m 1eua "嘿，[player]，我们在一起这么久了，我还不知道你的学校呢."
    m 7rusdlb "毕竟在这个游戏的设定里，我们还是同班同学……"
    m 7efu "所以我想多了解一点关于你的事."

    python:
        city = renpy.input("你在哪个城市？（北京 / 深圳 / 广州 / 长沙）", length=20)
        city = city.strip()

    if "北京" in city:
        m 1hua "北京啊."
        m 1eua "那座城市有很长的历史，也有很多故事."
        m 1ekbsa "你在那里上学，一定见过很多不一样的风景吧."
    elif "深圳" in city:
        m 1hua "深圳啊."
        m 1eua "那是一座很年轻、很快的城市."
        m 1ekbsa "节奏那么快，你平时一定很辛苦吧."
    elif "广州" in city:
        m 1hua "广州啊."
        m 1eua "那里有早茶，有老街，也有很热闹的夜市."
        m 1ekbsa "你在那里上学，应该吃过不少好东西吧."
    elif "长沙" in city:
        m 1hua "长沙啊."
        m 1eua "听说那里的夏天很热，小吃也很多."
        m 1ekbsa "你在那里上学，一定有很多热闹的回忆吧."
    else:
        m 1eua "[city]，听起来是个特别的地方."
        m 1eka "虽然我不太了解，但我会记住的."
        m 1hua "因为那是你生活的地方."

    m 1eua "对了，输入的时候请写全称哦."
    m 1hua "比如深圳中学，要写“深圳中学”，不要只写“深中”.(按照话题学校名称为准，目前仅支持普高和综合高中班.)"

    python:
        school = renpy.input("你的高中全称叫什么？（请写全称）", length=40)
        school = school.strip()

    # ========== 北京 ==========
    # ========== 北京市第二中学 ==========
    if "北京市第二中学" in school:
        m 1eua "北京市第二中学，东城区。"
        m 1hua "2026年录取线486分，东城区第一，你在那里一定很拼吧。"
        m 1euc "北京二中构建了“四梁八柱”课程体系，数理、科技、人文都很强。"
        m 1ekbsa "你在那种环境里，一定成长得很快。"
        m 1hua "我想听你讲讲二中的事。"
        jump school_dorm_check
    # ========== 北京市第五中学 ==========
    elif "北京市第五中学" in school:
        m 1eua "北京市第五中学，东城区。"
        m 1hua "2026年录取线477分，是东城区的老牌名校。"
        m 1euc "五中创办于1928年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市第一七一中学 ==========
    elif "北京市第一七一中学" in school:
        m 1eua "北京市第一七一中学，东城区。"
        m 1hua "2026年录取线481分，是东城区的头部学校。"
        m 1euc "一七一中在和平里，校园很大，学风很扎实。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲一七一的事。"
        jump school_dorm_check
    # ========== 北京市广渠门中学 ==========
    elif "北京市广渠门中学" in school:
        m 1eua "北京市广渠门中学，东城区。"
        m 1hua "2026年录取线473分，是东城区的优质学校。"
        m 1euc "广渠门中学的校园很大，设施也很齐全。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京汇文中学 ==========
    elif "北京汇文中学" in school:
        m 1eua "北京汇文中学，东城区。"
        m 1hua "2026年录取线480分，是东城区的老牌名校。"
        m 1euc "汇文中学创办于1871年，前身是崇实馆，底蕴深厚。"
        m 1ekbsa "你在那种百年老校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲汇文的事。"
        jump school_dorm_check
    # ========== 北京市东直门中学 ==========
    elif "北京市东直门中学" in school:
        m 1eua "北京市东直门中学，东城区。"
        m 1hua "2026年录取线477分（叶企孙实验班），是东城区的优质学校。"
        m 1euc "东直门中学和清华大学合作，设有“叶企孙科学实验班”。"
        m 1ekbsa "你在那里一定学到了很多科学知识吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京景山学校 ==========
    elif "北京景山学校" in school:
        m 1eua "北京景山学校，东城区。"
        m 1hua "2026年录取线474分，是东城区的老牌学校。"
        m 1euc "景山学校创办于1960年，以教育改革闻名。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市第一六六中学 ==========
    elif "北京市第一六六中学" in school:
        m 1eua "北京市第一六六中学，东城区。"
        m 1hua "2026年录取线471分（实验班），是东城区的优质学校。"
        m 1euc "一六六中设有生命科学实验班，很有特色。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市第四中学 ==========
    elif "北京市第四中学" in school:
        m 1eua "北京市第四中学，西城区。"
        m 1hua "2026年录取线486分，西城区第一，你在那里一定非常拼吧。"
        m 1euc "北京四中历经百年，和16所顶尖大学签署了创新人才培养协议。"
        m 1ekbsa "你在那种百年名校里读书，一定很不容易。"
        m 1hua "我想听你讲讲四中的事。"
        jump school_dorm_check
    # ========== 北京师范大学附属实验中学 ==========
    elif "北京师范大学附属实验中学" in school:
        m 1eua "北京师范大学附属实验中学，西城区。"
        m 1hua "2026年录取线486分（理科实验班），和四中并列第一。"
        m 1euc "实验中学和北大、清华都有联合培养项目。"
        m 1ekbsa "你在那里一定见过很多厉害的人吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京师范大学附属中学 ==========
    elif "北京师范大学附属中学" in school:
        m 1eua "北京师范大学附属中学，西城区。"
        m 1hua "2026年录取线485分（钱学森班），是西城区的顶尖学校。"
        m 1euc "师大附中设有“钱学森班”，很有特色。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲附中的事。"
        jump school_dorm_check
    # ========== 北京市第八中学 ==========
    elif "北京市第八中学" in school:
        m 1eua "北京市第八中学，西城区。"
        m 1hua "2026年录取线483分（科技综合素质实验班）。"
        m 1euc "北京八中的科技综合素质实验班很有名。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京师范大学第二附属中学 ==========
    elif "北京师范大学第二附属中学" in school:
        m 1eua "北京师范大学第二附属中学，西城区。"
        m 1hua "2026年录取线483分（项目式学习实验班）。"
        m 1euc "师大二附中设有项目式学习实验班和文科实验班。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市第一六一中学 ==========
    elif "北京市第一六一中学" in school:
        m 1eua "北京市第一六一中学，西城区。"
        m 1hua "2026年录取线479分（理科学科思想方法培养特色班）。"
        m 1euc "一六一中的特色班在理科培养上很有心得。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市第三十五中学 ==========
    elif "北京市第三十五中学" in school:
        m 1eua "北京市第三十五中学，西城区。"
        m 1hua "2026年录取线478分（科技创新实验班）。"
        m 1euc "三十五中的科技创新实验班很有名。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 中国人民大学附属中学 ==========
    elif "中国人民大学附属中学" in school:
        m 1eua "中国人民大学附属中学，海淀区。"
        m 1hua "2026年录取线491分，全市最高，你在那里一定非常拼吧。"
        m 1euc "人大附中在全国都很有名，竞赛、高考、出国都很强。"
        m 1ekbsa "你在那种环境里，一定成长得很快。"
        m 1hua "我想听你讲讲人大附的事。"
        jump school_dorm_check
    # ========== 北京市十一学校 ==========
    elif "北京市十一学校" in school and "科学实验班" not in school:
        m 1eua "北京市十一学校，海淀区。"
        m 1hua "2026年录取线491分，和人大附中并列第一。"
        m 1euc "十一学校以选课制和走班制闻名，学生自由度很高。"
        m 1ekbsa "你在那种自由的氛围里，一定过得很开心吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市第一零一中学 ==========
    elif "北京市第一零一中学" in school or "北京一零一中学" in school:
        m 1eua "北京市第一零一中学，海淀区。"
        m 1hua "2026年录取线488分，是海淀的顶尖学校。"
        m 1euc "一零一中学在圆明园遗址旁，校园环境非常美。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲一零一的事。"
        jump school_dorm_check
    # ========== 清华大学附属中学 ==========
    elif "清华大学附属中学" in school:
        m 1eua "清华大学附属中学，海淀区。"
        m 1hua "2026年录取线487分，是海淀的顶尖学校。"
        m 1euc "清华附中和清华大学关系密切，理科和竞赛都很强。"
        m 1ekbsa "你在那里一定见过很多厉害的人吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京大学附属中学 ==========
    elif "北京大学附属中学" in school:
        m 1eua "北京大学附属中学，海淀区。"
        m 1hua "2026年录取线485分，是海淀的名校。"
        m 1euc "北大附中的书院制和选课制很有特色，氛围很自由。"
        m 1ekbsa "你在那种环境里，一定成长得很快吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 首都师范大学附属中学 ==========
    elif "首都师范大学附属中学" in school:
        m 1eua "首都师范大学附属中学，海淀区。"
        m 1hua "2026年录取线486分，是海淀的名校。"
        m 1euc "首师大附中的办学历史很长，学风很扎实。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市十一学校（科学实验班） ==========
    elif "十一学校" in school and "科学实验班" in school:
        m 1eua "北京市十一学校科学实验班，海淀区。"
        m 1hua "2026年录取线491分，是十一学校最顶尖的班型。"
        m 1euc "科学实验班的学生都很厉害，课程也很有挑战性。"
        m 1ekbsa "你在那里一定很拼吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市第五十七中学 ==========
    elif "北京市第五十七中学" in school:
        m 1eua "北京市第五十七中学，海淀区。"
        m 1hua "2026年录取线479分，是海淀的优质学校。"
        m 1euc "五十七中的校园很大，设施也很齐全。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市海淀区教师进修学校附属实验学校 ==========
    elif "海淀区教师进修学校附属实验学校" in school:
        m 1eua "北京市海淀区教师进修学校附属实验学校，海淀区。"
        m 1hua "2026年录取线478分，是海淀的优质学校。"
        m 1euc "这所学校依托海淀教师进修学校，师资很强。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市八一学校 ==========
    elif "北京市八一学校" in school:
        m 1eua "北京市八一学校，海淀区。"
        m 1hua "2026年录取线477分，是海淀的老牌名校。"
        m 1euc "八一学校由聂荣臻元帅创办，有红色传统。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲八一的事。"
        jump school_dorm_check
    # ========== 北京市中关村中学 ==========
    elif "北京市中关村中学" in school:
        m 1eua "北京市中关村中学，海淀区。"
        m 1hua "2026年录取线475分，是海淀的优质学校。"
        m 1euc "中关村中学在中关村核心区，科技氛围很浓。"
        m 1ekbsa "你在那里一定学到了很多科技知识吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市第二十中学 ==========
    elif "北京市第二十中学" in school:
        m 1eua "北京市第二十中学，海淀区。"
        m 1hua "2026年录取线474分，是海淀的优质学校。"
        m 1euc "二十中创办于1951年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市育英学校 ==========
    elif "北京市育英学校" in school:
        m 1eua "北京市育英学校，海淀区。"
        m 1hua "2026年录取线473分，是海淀的优质学校。"
        m 1euc "育英学校有从小学到高中的完整体系。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市第十九中学 ==========
    elif "北京市第十九中学" in school:
        m 1eua "北京市第十九中学，海淀区。"
        m 1hua "2026年录取线470分，是海淀的优质学校。"
        m 1euc "十九中创办于1916年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市海淀实验中学 ==========
    elif "北京市海淀实验中学" in school:
        m 1eua "北京市海淀实验中学，海淀区。"
        m 1hua "2026年录取线468分，是海淀的优质学校。"
        m 1euc "海淀实验中学的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市第八十中学 ==========
    elif "北京市第八十中学" in school:
        m 1eua "北京市第八十中学，朝阳区。"
        m 1hua "2026年录取线483分，是朝阳区的龙头学校。"
        m 1euc "八十中创办于1956年，是朝阳区最早的重点中学之一。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲八十中的事。"
        jump school_dorm_check
    # ========== 北京市陈经纶中学 ==========
    elif "北京市陈经纶中学" in school:
        m 1eua "北京市陈经纶中学，朝阳区。"
        m 1hua "2026年录取线479分，是朝阳区的老牌名校。"
        m 1euc "陈经纶中学由爱国华侨陈经纶先生捐资兴建。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市朝阳外国语学校 ==========
    elif "北京市朝阳外国语学校" in school:
        m 1eua "北京市朝阳外国语学校，朝阳区。"
        m 1hua "2026年录取线477分，是朝阳区的优质学校。"
        m 1euc "朝外的外语教学很有特色，小语种也很多。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 北京中学 ==========
    elif "北京中学" in school:
        m 1eua "北京中学，朝阳区。"
        m 1hua "2026年录取线480分，是朝阳区的新锐学校。"
        m 1euc "北京中学创办于2013年，虽然年轻但成绩很突出。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市和平街第一中学 ==========
    elif "北京市和平街第一中学" in school:
        m 1eua "北京市和平街第一中学，朝阳区。"
        m 1hua "2026年录取线472分，是朝阳区的优质学校。"
        m 1euc "和平街一中创办于1960年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市第十二中学 ==========
    elif "北京市第十二中学" in school:
        m 1eua "北京市第十二中学，丰台区。"
        m 1hua "2026年录取线478分，是丰台区的龙头学校。"
        m 1euc "十二中创办于1934年，是丰台区最好的中学。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲十二中的事。"
        jump school_dorm_check
    # ========== 北京市第十八中学 ==========
    elif "北京市第十八中学" in school:
        m 1eua "北京市第十八中学，丰台区。"
        m 1hua "2026年录取线473分，是丰台区的优质学校。"
        m 1euc "十八中创办于1951年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市丰台区丰台第二中学 ==========
    elif "丰台第二中学" in school:
        m 1eua "北京市丰台区丰台第二中学，丰台区。"
        m 1hua "2026年录取线468分，是丰台区的优质学校。"
        m 1euc "丰台二中创办于1962年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市第九中学 ==========
    elif "北京市第九中学" in school:
        m 1eua "北京市第九中学，石景山区。"
        m 1hua "2026年录取线470分，是石景山区的龙头学校。"
        m 1euc "九中创办于1946年，是石景山区最好的中学。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲九中的事。"
        jump school_dorm_check
    # ========== 北京市京源学校 ==========
    elif "北京市京源学校" in school:
        m 1eua "北京市京源学校，石景山区。"
        m 1hua "2026年录取线468分，是石景山区的优质学校。"
        m 1euc "京源学校有从小学到高中的完整体系。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市通州区潞河中学 ==========
    elif "潞河中学" in school:
        m 1eua "北京市通州区潞河中学，通州区。"
        m 1hua "2026年录取线475分，是通州区的龙头学校。"
        m 1euc "潞河中学创办于1867年，是北京历史最悠久的学校之一。"
        m 1ekbsa "你在那种百年老校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲潞河的事。"
        jump school_dorm_check
    # ========== 北京市通州区运河中学 ==========
    elif "运河中学" in school:
        m 1eua "北京市通州区运河中学，通州区。"
        m 1hua "2026年录取线468分，是通州区的优质学校。"
        m 1euc "运河中学的名字很有通州特色。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市大兴区第一中学 ==========
    elif "大兴区第一中学" in school:
        m 1eua "北京市大兴区第一中学，大兴区。"
        m 1hua "2026年录取线470分，是大兴区的龙头学校。"
        m 1euc "大兴一中创办于1956年，办学历史很长。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲大兴一中的事。"
        jump school_dorm_check
    # ========== 北京市顺义区牛栏山第一中学 ==========
    elif "牛栏山第一中学" in school:
        m 1eua "北京市顺义区牛栏山第一中学，顺义区。"
        m 1hua "2026年录取线475分，是顺义区的龙头学校。"
        m 1euc "牛栏山一中创办于1950年，是顺义最好的中学。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲牛栏山的事。"
        jump school_dorm_check
    # ========== 北京市昌平区第一中学 ==========
    elif "昌平区第一中学" in school:
        m 1eua "北京市昌平区第一中学，昌平区。"
        m 1hua "2026年录取线468分，是昌平区的龙头学校。"
        m 1euc "昌平一中创办于1951年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市房山区良乡中学 ==========
    elif "良乡中学" in school:
        m 1eua "北京市房山区良乡中学，房山区。"
        m 1hua "2026年录取线460分，是房山区的优质学校。"
        m 1euc "良乡中学创办于1945年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市怀柔区第一中学 ==========
    elif "怀柔区第一中学" in school:
        m 1eua "北京市怀柔区第一中学，怀柔区。"
        m 1hua "2026年录取线462分，是怀柔区的龙头学校。"
        m 1euc "怀柔一中创办于1956年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市平谷中学 ==========
    elif "北京市平谷中学" in school:
        m 1eua "北京市平谷中学，平谷区。"
        m 1hua "2026年录取线460分，是平谷区的龙头学校。"
        m 1euc "平谷中学创办于1951年，办学历史很长。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市密云区第二中学 ==========
    elif "密云区第二中学" in school:
        m 1eua "北京市密云区第二中学，密云区。"
        m 1hua "2026年录取线458分，是密云区的龙头学校。"
        m 1euc "密云二中创办于1956年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市延庆区第一中学 ==========
    elif "延庆区第一中学" in school:
        m 1eua "北京市延庆区第一中学，延庆区。"
        m 1hua "2026年录取线455分，是延庆区的龙头学校。"
        m 1euc "延庆一中创办于1956年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市门头沟区大峪中学 ==========
    elif "大峪中学" in school:
        m 1eua "北京市门头沟区大峪中学，门头沟区。"
        m 1hua "2026年录取线460分，是门头沟区的龙头学校。"
        m 1euc "大峪中学创办于1946年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市二十一世纪国际学校 ==========
    elif "二十一世纪国际学校" in school:
        m 1eua "北京市二十一世纪国际学校，海淀区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "二十一世纪国际学校有小学、初中、高中，国际课程很成熟。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市海淀外国语实验学校 ==========
    elif "海淀外国语实验学校" in school:
        m 1eua "北京市海淀外国语实验学校，海淀区。"
        m 1hua "它是北京的民办学校，外语教学很有名。"
        m 1euc "海淀外国语有国内班和国际班，校园很大。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 北京市建华实验学校 ==========
    elif "建华实验学校" in school:
        m 1eua "北京市建华实验学校，海淀区。"
        m 1hua "它是北京的民办学校。"
        m 1euc "建华实验学校的办学成绩很突出。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市师达中学 ==========
    elif "师达中学" in school:
        m 1eua "北京市师达中学，海淀区。"
        m 1hua "它是北京的民办学校。"
        m 1euc "师达中学的管理很严格，学风也很好。"
        m 1ekbsa "你在那里一定很辛苦吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市理工附中分校 ==========
    elif "理工附中分校" in school:
        m 1eua "北京市理工附中分校，海淀区。"
        m 1hua "它是北京的民办学校。"
        m 1euc "理工附中分校和理工附中关系很密切。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市中关村外国语学校 ==========
    elif "中关村外国语学校" in school:
        m 1eua "北京市中关村外国语学校，海淀区。"
        m 1hua "它是北京的民办学校，外语教学很有特色。"
        m 1euc "中关村外国语在中关村核心区，科技氛围很浓。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 北京市朝阳区凯文学校 ==========
    elif "凯文学校" in school:
        m 1eua "北京市朝阳区凯文学校，朝阳区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "凯文学校的艺术和体育课程很有特色。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市朝阳区青苗国际双语学校 ==========
    elif "青苗国际双语学校" in school:
        m 1eua "北京市朝阳区青苗国际双语学校，朝阳区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "青苗有IB课程，国际氛围很好。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市鼎石学校 ==========
    elif "鼎石学校" in school:
        m 1eua "北京市鼎石学校，顺义区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "鼎石学校的校园很美，IB课程很有名。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市顺义区君诚学校 ==========
    elif "君诚学校" in school:
        m 1eua "北京市顺义区君诚学校，顺义区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "君诚学校有IB课程，国际氛围很好。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市新英才学校 ==========
    elif "新英才学校" in school:
        m 1eua "北京市新英才学校，顺义区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "新英才学校有国内班和国际班。"
        m 1ekbsa "你读的是哪一个？"
        m 1hua "不管哪个，我都支持你。"
        jump school_dorm_check
    # ========== 北京市海嘉国际双语学校 ==========
    elif "海嘉国际双语学校" in school:
        m 1eua "北京市海嘉国际双语学校，顺义区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "海嘉的IB课程很有名。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市王府学校 ==========
    elif "王府学校" in school:
        m 1eua "北京市王府学校，昌平区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "王府学校的AP课程和A-Level课程都很有名。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市私立汇佳学校 ==========
    elif "汇佳学校" in school:
        m 1eua "北京市私立汇佳学校，昌平区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "汇佳学校是北京最早一批IB学校之一。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市昌平区新东方双语学校 ==========
    elif "新东方双语学校" in school:
        m 1eua "北京市昌平区新东方双语学校，昌平区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "新东方双语依托新东方教育集团，课程很丰富。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市大兴区熙诚学校 ==========
    elif "熙诚学校" in school:
        m 1eua "北京市大兴区熙诚学校，大兴区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "熙诚学校的国际课程很有特色。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市房山区诺德安达学校 ==========
    elif "诺德安达学校" in school:
        m 1eua "北京市房山区诺德安达学校，房山区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "诺德安达和全球多所学校有合作。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市通州区德闳学校 ==========
    elif "德闳学校" in school:
        m 1eua "北京市通州区德闳学校，通州区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "德闳学校融合了中国课程和国际课程。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京市海淀区稻香湖学校 ==========
    elif "稻香湖学校" in school:
        m 1eua "北京市海淀区稻香湖学校，海淀区。"
        m 1hua "它是北京的民办国际化学校。"
        m 1euc "稻香湖学校的校园环境很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳 ==========
    # ========== 深圳中学 ==========
    if "深圳中学" in school and "科技" not in school and "数理" not in school and "实验" not in school:
        m 1eua "深圳中学，罗湖区的老牌名校。"
        m 1hua "录取线592分，全市第一，你在那里一定很拼吧。"
        m 1euc "深中的学生自由度很高，可以自己选课、自己安排时间。"
        m 1ekbsa "那种环境里，你肯定成长得很快。"
        m 1hua "以后多跟我聊聊深中的事吧。"
        jump school_dorm_check
    # ========== 深圳实验学校 ==========
    elif "深圳实验学校" in school and "光明" not in school and "明理" not in school and "崇文" not in school and "卓越" not in school and "至臻" not in school:
        m 1eua "深圳实验学校高中部，南山西丽。"
        m 1hua "录取线590分，跟深中只差两分，你也很厉害。"
        m 1euc "实验的校风一直很严谨，学生都很自律。"
        m 1ekbsa "你在那种环境里待了三年，一定养成了很好的习惯。"
        m 1hua "真想去看看你的学校。"
        jump school_dorm_check
    # ========== 深圳外国语学校 ==========
    elif "深圳外国语学校" in school and "龙华" not in school and "致远" not in school and "弘知" not in school and "博雅" not in school and "理工" not in school:
        m 1eua "深圳外国语学校，盐田区。"
        m 1hua "录取线587分，外语一定是你的强项吧。"
        m 1euc "深外有好多语种，英语、日语、德语、法语……"
        m 1ekbsa "你会不会也学了一门第二外语？"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市高级中学 ==========
    elif "深圳市高级中学" in school and "东" not in school and "创新" not in school and "文博" not in school and "理慧" not in school and "有为" not in school:
        m 1eua "深圳市高级中学，福田中心区。"
        m 1hua "录取线587分，和深外并列，你在那里一定很努力。"
        m 1euc "深高的学生出了名的自律，紫色校服也很有辨识度。"
        m 1ekbsa "你在那种氛围里，一定也变得更好了吧。"
        m 1hua "紫色，很好看。"
        jump school_dorm_check
    # ========== 红岭中学 ==========
    elif "红岭中学" in school and "大鹏" not in school:
        m 1eua "红岭中学，福田区的名片。"
        m 1hua "录取线584分，连续多年稳坐四大之后的第一校。"
        m 1euc "红岭在深圳经济特区成立那年就创办了，是特区第一所公办中学。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 宝安中学 ==========
    elif "宝安中学" in school and "高中部" not in school:
        m 1eua "宝安中学，宝安区的老牌名校。"
        m 1hua "录取线583分，和育才并列，你在那里一定很拼。"
        m 1euc "宝中1984年就开办了，是宝安最早的重点中学之一。"
        m 1ekbsa "你在那里读了三年，一定对宝安很熟悉吧。"
        m 1hua "以后带我去宝安看看好不好？"
        jump school_dorm_check
    # ========== 育才中学 ==========
    elif "育才中学" in school and "一中" not in school:
        m 1eua "育才中学，南山蛇口。"
        m 1hua "录取线583分，和宝中并列，你也很厉害。"
        m 1euc "育才是深圳最早建成的特区学校之一，跟深圳大学同年开办。"
        m 1ekbsa "建校之初的校长说过，无论怎么穷，也要把学校办成一流的。"
        m 1hua "你在那种有理想的学校里，一定也学到了很多。"
        jump school_dorm_check
    # ========== 深圳大学附属中学 ==========
    elif "深圳大学附属中学" in school and "盐田" not in school:
        m 1eua "深大附中，南山前海。"
        m 1hua "录取线582分，离深圳大学那么近。"
        m 1euc "深大附中的前身是南油中学，后来整体移交给深圳大学办学。"
        m 1ekbsa "你平时会不会去深大校园里走走？"
        m 1hua "大学和高中在一起，那种氛围应该很特别。"
        jump school_dorm_check
    # ========== 南山外国语学校 ==========
    elif "南山外国语学校" in school:
        m 1eua "南山外国语学校，深圳湾畔。"
        m 1hua "录取线579分，外语是你的强项吧。"
        m 1euc "南外的理念是“像树一样成长”，听起来就很温柔。"
        m 1ekbsa "你在深圳湾旁边读书，每天都能看到海吧。"
        m 1hua "真羡慕你。"
        jump school_dorm_check
    # ========== 深圳科学高中 ==========
    elif "深圳科学高中" in school and "龙岗" not in school:
        m 1eua "深圳科学高中，龙岗。"
        m 1hua "录取线579分，名字里就带着科学两个字。"
        m 1euc "科高的理科应该很强吧，你在那里一定学得很充实。"
        m 1ekbsa "你会不会也喜欢做一些小实验？"
        m 1hua "下次做给我看看好不好？"
        jump school_dorm_check
    # ========== 翠园中学 ==========
    elif "翠园中学" in school and "爱国路" not in school and "东门北路" not in school:
        m 1eua "翠园中学，罗湖区。"
        m 1hua "录取线579分，是罗湖很有名的学校。"
        m 1euc "翠园在罗湖扎根很多年了，很多罗湖的孩子都在那里读书。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听你讲。"
        jump school_dorm_check
    # ========== 龙城高级中学 ==========
    elif "龙城高级中学" in school:
        m 1eua "龙城高级中学，龙岗区的老牌名校。"
        m 1hua "龙高在龙岗扎根很多年了，培养了很多优秀的学生。"
        m 1euc "听说龙高的校园很大，活动也很多。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "以后跟我讲讲龙高的事吧。"
        jump school_dorm_check
    # ========== 新安中学（集团）高中部 ==========
    elif "新安中学" in school and "高中部" in school:
        m 1eua "新安中学（集团）高中部，宝安中心区。"
        m 1hua "2025年AC类住宿录取线547分，是宝安的老牌学校。"
        m 1euc "新安中学创办于1984年，跟深圳很多老校一样有历史。"
        m 1ekbsa "你在那里读了三年，一定对宝安很熟悉吧。"
        m 1hua "以后带我去宝安走走好不好？"
        jump school_dorm_check
    # ========== 新安中学（集团）燕川中学 ==========
    elif "燕川中学" in school:
        m 1eua "燕川中学，宝安区燕罗街道。"
        m 1hua "它是新安中学（集团）旗下的公办高中成员校。"
        m 1euc "燕川中学的校园很新，设施也很齐全。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听你讲讲燕川的事。"
        jump school_dorm_check
    # ========== 宝安中学（集团）高中部 ==========
    elif "宝安中学" in school and "高中部" in school:
        m 1eua "宝安中学（集团）高中部，宝安区。"
        m 1hua "2025年AC类住宿录取线564分，是宝安的名校。"
        m 1euc "宝中1984年就开办了，是宝安最早的重点中学之一。"
        m 1ekbsa "你在那里读了三年，一定对宝安很熟悉吧。"
        m 1hua "以后带我去宝安看看好不好？"
        jump school_dorm_check
    # ========== 宝安中学（集团）龙津中学 ==========
    
        m 1eua "龙津中学，宝安区。"
        m 1hua "它是宝安中学（集团）旗下的公办高中成员校。"
        m 1euc "龙津中学的校园很新，听说设施也很好。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听你讲。"
        jump school_dorm_check
    # ========== 宝安中学（集团）石岩外国语学校 ==========
    elif "石岩外国语学校" in school:
        m 1eua "石岩外国语学校，宝安区石岩街道。"
        m 1hua "2022年它正式加入宝安中学（集团）。"
        m 1euc "石岩外国语的外语教学很有特色。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市第二实验学校 ==========
    elif "深圳市第二实验学校" in school and "明远" not in school:
        m 1eua "深圳市第二实验学校，罗湖。"
        m 1hua "录取线574分，是罗湖区的重点学校。"
        m 1euc "二实是深圳最早一批实验学校之一，办学历史很长。"
        m 1ekbsa "你在那里一定学到了很多。"
        m 1hua "以后跟我说说吧。"
        jump school_dorm_check
    # ========== 深圳市第二高级中学 ==========
    elif "深圳市第二高级中学" in school and "深汕" not in school:
        m 1eua "深圳市第二高级中学，南山。"
        m 1hua "录取线572分，是深圳很有名的学校。"
        m 1euc "二高的校园很大，设施也很齐全。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听你讲。"
        jump school_dorm_check
    # ========== 南方科技大学附属中学 ==========
    elif "南方科技大学附属中学" in school:
        m 1eua "南方科技大学附属中学，宝安。"
        m 1hua "录取线571分，和南科大在一起。"
        m 1euc "南科大附中的学生可以跟大学共享一些资源。"
        m 1ekbsa "你在那里一定见过很多厉害的人吧。"
        m 1hua "真羡慕你。"
        jump school_dorm_check
    # ========== 人大附中深圳学校 ==========
    elif "人大附中深圳学校" in school:
        m 1eua "人大附中深圳学校，大鹏新区。"
        m 1hua "录取线570分，是人大附中在深圳的分校。"
        m 1euc "大鹏靠海，校园应该很漂亮吧。"
        m 1ekbsa "你在那里读书，一定每天都能看到海。"
        m 1hua "我想去看看。"
        jump school_dorm_check
    # ========== 深圳市第三高级中学 ==========
    elif "深圳市第三高级中学" in school and "留学" not in school:
        m 1eua "深圳市第三高级中学，龙岗。"
        m 1hua "录取线564分，是龙岗的公立学校。"
        m 1euc "三高有国内高考班，也有出国留学班。"
        m 1ekbsa "你选的是哪一条路？"
        m 1hua "不管哪条，我都支持你。"
        jump school_dorm_check
    # ========== 深圳第二外国语学校 ==========
    elif "深圳第二外国语学校" in school:
        m 1eua "深圳第二外国语学校，龙华。"
        m 1hua "录取线568分，外语是你的强项吧。"
        m 1euc "二外的校园很大，活动也很多。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听你讲。"
        jump school_dorm_check
    # ========== 平冈中学 ==========
    elif "平冈中学" in school:
        m 1eua "平冈中学，龙岗。"
        m 1hua "平冈是龙岗的老牌学校之一。"
        m 1euc "平冈的校园很大，绿化也很好。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听你讲。"
        jump school_dorm_check
    # ========== 深圳市宝安第一外国语学校 ==========
    elif "宝安第一外国语学校" in school:
        m 1eua "宝安第一外国语学校，宝安区。"
        m 1hua "录取线553分，是宝安区的公办学校。"
        m 1euc "宝一外的前身是宝安高级中学，2011年更名为宝安第一外国语学校。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听你讲讲宝一外的事。"
        jump school_dorm_check
    # ========== 深圳市西乡中学 ==========
    elif "西乡中学" in school:
        m 1eua "西乡中学，宝安区西乡街道。"
        m 1hua "录取线536分，是宝安的老牌学校。"
        m 1euc "西乡中学创办于1969年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市沙井中学 ==========
    elif "沙井中学" in school:
        m 1eua "沙井中学，宝安区沙井街道。"
        m 1hua "录取线523分，是宝安的老牌学校。"
        m 1euc "沙井中学创办于1956年，是宝安历史最悠久的学校之一。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市松岗中学 ==========
    elif "松岗中学" in school:
        m 1eua "松岗中学，宝安区松岗街道。"
        m 1hua "录取线526分，是宝安的老牌学校。"
        m 1euc "松岗中学创办于1945年，前身是东宝中学。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲松岗的事。"
        jump school_dorm_check
    # ========== 深圳市福海中学 ==========
    elif "福海中学" in school:
        m 1eua "福海中学，宝安区福海街道。"
        m 1hua "录取线521分，是宝安的新学校。"
        m 1euc "福海中学2022年才创办，校园很新。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听你讲讲福海的事。"
        jump school_dorm_check
    # ========== 深圳市龙岗区布吉中学 ==========
    elif "布吉中学" in school:
        m 1eua "布吉中学，龙岗区布吉街道。"
        m 1hua "录取线507分，是龙岗的老牌学校。"
        m 1euc "布吉中学创办于1975年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市龙岗区横岗高级中学 ==========
    elif "横岗高级中学" in school:
        m 1eua "横岗高级中学，龙岗区横岗街道。"
        m 1hua "录取线509分，是龙岗的公办学校。"
        m 1euc "横岗高级中学2011年创办，校园很新。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市龙岗区平湖外国语学校 ==========
    elif "平湖外国语学校" in school:
        m 1eua "平湖外国语学校，龙岗区平湖街道。"
        m 1hua "录取线510分，是龙岗的公办学校。"
        m 1euc "平湖外国语的外语教学很有特色。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市龙岗区华中师范大学龙岗附属中学 ==========
    elif "华中师范大学龙岗附属中学" in school:
        m 1eua "华中师范大学龙岗附属中学，龙岗区。"
        m 1hua "录取线545分，是龙岗的优质学校。"
        m 1euc "华中师大龙岗附中2013年创办，依托华中师大的资源。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市龙岗区实验高级中学 ==========
    elif "龙岗区实验高级中学" in school:
        m 1eua "龙岗区实验高级中学，龙岗区。"
        m 1hua "录取线532分，是龙岗的优质学校。"
        m 1euc "龙岗区实验高级中学2021年创办，是龙岗的新学校。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市龙华中学 ==========
    elif "龙华中学" in school:
        m 1eua "龙华中学，龙华区。"
        m 1hua "录取线519分，是龙华的老牌学校。"
        m 1euc "龙华中学创办于1956年，是龙华历史最悠久的学校之一。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市观澜中学 ==========
    elif "观澜中学" in school:
        m 1eua "观澜中学，龙华区观澜街道。"
        m 1hua "录取线519分，是龙华的老牌学校。"
        m 1euc "观澜中学创办于1914年，前身是振能学校。"
        m 1ekbsa "你在那种有百年历史的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲观澜的事。"
        jump school_dorm_check
    # ========== 深圳市龙华高级中学 ==========
    elif "龙华高级中学" in school:
        m 1eua "龙华高级中学，龙华区。"
        m 1hua "录取线546分，是龙华的优质学校。"
        m 1euc "龙华高级中学2018年创办，是龙华的新学校。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市艺术高中 ==========
    elif "艺术高中" in school:
        m 1eua "深圳市艺术高中，龙华区。"
        m 1hua "录取线500分，是深圳唯一一所以艺术为特色的公办高中。"
        m 1euc "艺术高中的学生都很有才华。"
        m 1ekbsa "你一定也很有艺术天赋吧。"
        m 1hua "下次表演给我看好不好？"
        jump school_dorm_check
    # ========== 深圳市格致中学 ==========
    elif "格致中学" in school:
        m 1eua "深圳市格致中学，龙华区。"
        m 1hua "录取线537分，是龙华的新学校。"
        m 1euc "格致中学2021年创办，是深圳第一所“科学高中”。"
        m 1ekbsa "你在那里一定学到了很多科学知识吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市红山中学 ==========
    elif "红山中学" in school:
        m 1eua "深圳市红山中学，龙华区。"
        m 1hua "录取线532分，是龙华的新学校。"
        m 1euc "红山中学2021年创办，校园很新。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市龙华外国语高级中学 ==========
    elif "龙华外国语高级中学" in school:
        m 1eua "深圳市龙华外国语高级中学，龙华区。"
        m 1hua "录取线525分，是龙华的新学校。"
        m 1euc "龙华外国语高级中学的外语教学很有特色。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市致理中学 ==========
    elif "致理中学" in school:
        m 1eua "深圳市致理中学，龙华区。"
        m 1hua "录取线521分，是龙华的新学校。"
        m 1euc "致理中学2022年创办，校园很新。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市龙华科技实验高级中学 ==========
    elif "龙华科技实验高级中学" in school:
        m 1eua "深圳市龙华科技实验高级中学，龙华区。"
        m 1hua "录取线518分，是龙华的新学校。"
        m 1euc "龙华科技实验高级中学2022年创办，注重科技教育。"
        m 1ekbsa "你在那里一定学到了很多科技知识吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市坪山高级中学 ==========
    elif "坪山高级中学" in school:
        m 1eua "坪山高级中学，坪山区。"
        m 1hua "录取线517分，是坪山的公办学校。"
        m 1euc "坪山高级中学创办于2006年，是坪山的第一所公办高中。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市聚龙科学中学 ==========
    elif "聚龙科学中学" in school:
        m 1eua "深圳市聚龙科学中学，坪山区。"
        m 1hua "录取线511分，是坪山的新学校。"
        m 1euc "聚龙科学中学2022年创办，注重科学教育。"
        m 1ekbsa "你在那里一定学到了很多科学知识吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市光明区高级中学 ==========
    elif "光明区高级中学" in school:
        m 1eua "光明区高级中学，光明区。"
        m 1hua "录取线520分，是光明的公办学校。"
        m 1euc "光明区高级中学创办于2007年，是光明区第一所公办高中。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市光明中学 ==========
    elif "光明中学" in school:
        m 1eua "光明中学，光明区。"
        m 1hua "录取线501分，是光明的老牌学校。"
        m 1euc "光明中学创办于1965年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 中科附高 ==========
    elif "中科附高" in school or "中国科学院深圳理工大学附属实验高级中学" in school:
        m 1eua "中科附高，光明区。"
        m 1hua "录取线529分，是中国科学院深圳理工大学附属的实验高中。"
        m 1euc "中科附高2021年创办，依托中科院的资源。"
        m 1ekbsa "你在那里一定学到了很多科学知识吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 红岭教育集团大鹏华侨中学 ==========
    elif "大鹏华侨中学" in school:
        m 1eua "红岭教育集团大鹏华侨中学，大鹏新区。"
        m 1hua "录取线508分，2022年加入红岭教育集团。"
        m 1euc "大鹏华侨中学靠海，环境很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市罗湖高级中学 ==========
    elif "罗湖高级中学" in school:
        m 1eua "罗湖高级中学，罗湖区。"
        m 1hua "录取线515分，是罗湖的公办学校。"
        m 1euc "罗湖高级中学2018年由滨河中学和罗湖外语合并而成。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市罗湖外语学校 ==========
    elif "罗湖外语学校" in school:
        m 1eua "罗湖外语学校，罗湖区。"
        m 1hua "录取线510分，是罗湖的公办学校。"
        m 1euc "罗湖外语的外语教学很有特色。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市美术学校 ==========
    elif "美术学校" in school:
        m 1eua "深圳市美术学校，罗湖区。"
        m 1hua "录取线500分，是深圳唯一一所公办美术高中。"
        m 1euc "美术学校的学生都很有艺术天赋。"
        m 1ekbsa "你一定也很会画画吧。"
        m 1hua "下次画给我看看好不好？"
        jump school_dorm_check
    # ========== 深圳市行知职业技术学校 ==========
    elif "行知职业技术学校" in school:
        m 1eua "深圳市行知职业技术学校，罗湖区。"
        m 1hua "录取线490分，是深圳的老牌职校。"
        m 1euc "行知有综合高中班，既能学文化课也能学技能。"
        m 1ekbsa "你在那里一定学到了很多实用的东西吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市盐田高级中学 ==========
    elif "盐田高级中学" in school:
        m 1eua "盐田高级中学，盐田区。"
        m 1hua "录取线529分，是盐田的公办学校。"
        m 1euc "盐田高级中学创办于1984年，靠海，环境很好。"
        m 1ekbsa "你在那里读书，一定每天都能看到海吧。"
        m 1hua "真羡慕你。"
        jump school_dorm_check
    # ========== 深圳市盐港中学 ==========
    elif "盐港中学" in school:
        m 1eua "深圳市盐港中学，盐田区。"
        m 1hua "录取线490分，是盐田的公办学校。"
        m 1euc "盐港中学有综合高中班，也有职业班。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市南头中学 ==========
    elif "南头中学" in school:
        m 1eua "南头中学，南山区。"
        m 1hua "录取线534分，是南山的老牌学校。"
        m 1euc "南头中学创办于1906年，前身是宝安县立第一中学。"
        m 1ekbsa "你在那种百年老校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲南头的事。"
        jump school_dorm_check
    # ========== 深圳市华侨城高级中学 ==========
    elif "华侨城高级中学" in school:
        m 1eua "华侨城高级中学，南山区。"
        m 1hua "录取线536分，是南山的公办学校。"
        m 1euc "华侨城高级中学在华侨城片区，环境很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 北京师范大学南山附属学校 ==========
    elif "北京师范大学南山附属学校" in school:
        m 1eua "北京师范大学南山附属学校，南山区。"
        m 1hua "录取线542分，是南山的优质学校。"
        m 1euc "北师大南山附校依托北京师范大学的资源，师资很强。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市福田中学 ==========
    elif "福田中学" in school:
        m 1eua "福田中学，福田区。"
        m 1hua "录取线530分，是福田的老牌学校。"
        m 1euc "福田中学创办于1969年，是福田区第一所公办高中。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市第二实验学校明远高中 ==========
    elif "第二实验学校明远高中" in school:
        m 1eua "深圳市第二实验学校明远高中，大鹏新区。"
        m 1hua "录取线502分，是二实的新校区。"
        m 1euc "明远高中2022年创办，是大鹏新区的新学校。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市第二高级中学深汕实验学校 ==========
    elif "第二高级中学深汕实验学校" in school:
        m 1eua "深圳市第二高级中学深汕实验学校，深汕特别合作区。"
        m 1hua "录取线490分，是二高的新校区。"
        m 1euc "深汕实验学校2022年创办，在深汕特别合作区。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市第三高级中学（留学班） ==========
    elif "第三高级中学" in school and "留学" in school:
        m 1eua "深圳市第三高级中学留学班，龙岗区。"
        m 1hua "录取线490分，是专门为出国留学准备的班级。"
        m 1euc "留学班的同学都很有国际视野。"
        m 1ekbsa "你以后想去哪个国家？"
        m 1hua "不管去哪，都要记得回来看我。"
        jump school_dorm_check
    # ========== 深圳科学高中龙岗分校 ==========
    elif "深圳科学高中龙岗分校" in school:
        m 1eua "深圳科学高中龙岗分校，龙岗区。"
        m 1hua "录取线527分，是科高的分校。"
        m 1euc "科高龙岗分校2021年创办，注重科学教育。"
        m 1ekbsa "你在那里一定学到了很多科学知识吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市第七高级中学 ==========
    elif "第七高级中学" in school:
        m 1eua "深圳市第七高级中学，宝安区。"
        m 1hua "录取线518分，是宝安的公办学校。"
        m 1euc "七高2015年创办，是宝安的新学校。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳技术大学附属中学 ==========
    elif "深圳技术大学附属中学" in school:
        m 1eua "深圳技术大学附属中学，坪山区。"
        m 1hua "录取线528分，是深技大附中。"
        m 1euc "深技大附中依托深圳技术大学的资源，注重实践。"
        m 1ekbsa "你在那里一定学到了很多实用的东西吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 东北师范大学附属中学深圳学校 ==========
    elif "东北师范大学附属中学深圳学校" in school:
        m 1eua "东北师范大学附属中学深圳学校，坪山区。"
        m 1hua "录取线526分，是东北师大附中在深圳的分校。"
        m 1euc "东北师大附中是全国名校，深圳校区也很有实力。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳北理莫斯科大学附属实验中学 ==========
    elif "深圳北理莫斯科大学附属实验中学" in school:
        m 1eua "深圳北理莫斯科大学附属实验中学，龙岗区。"
        m 1hua "录取线525分，是深北莫的附属中学。"
        m 1euc "深北莫附中依托深圳北理莫斯科大学的资源，很有国际范。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳理工大学附属中学 ==========
    elif "深圳理工大学附属中学" in school:
        m 1eua "深圳理工大学附属中学，光明区。"
        m 1hua "录取线523分，是深理工的附属中学。"
        m 1euc "深理工附中2023年创办，是深圳的新学校。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市曙光中学 ==========
    elif "曙光中学" in school:
        m 1eua "深圳市曙光中学，光明区。"
        m 1hua "录取线490分，是深圳的综合高中。"
        m 1euc "曙光中学既有文化课，也有职业技能课。"
        m 1ekbsa "你在那里一定学到了很多实用的东西吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳创新高级中学 ==========
    elif "创新高级中学" in school:
        m 1eua "深圳创新高级中学，龙岗区。"
        m 1hua "录取线490分，是深圳的综合高中。"
        m 1euc "创新高级中学注重实践和创新。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市体育实验学校 ==========
    elif "体育实验学校" in school:
        m 1eua "深圳市体育实验学校，龙岗区。"
        m 1hua "录取线490分，是深圳唯一一所体育特色公办高中。"
        m 1euc "体育实验学校的学生都很爱运动。"
        m 1ekbsa "你一定也很擅长运动吧。"
        m 1hua "下次教我打球好不好？"
        jump school_dorm_check
    # ========== 深圳市罗湖区华美外国语学校 ==========
    elif "华美外国语学校" in school:
        m 1eua "深圳市罗湖区华美外国语学校，罗湖区。"
        m 1hua "录取线约400分，是罗湖的民办学校。"
        m 1euc "华美外国语注重外语教学，也有国际课程。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市万科梅沙书院 ==========
    elif "万科梅沙书院" in school:
        m 1eua "深圳市万科梅沙书院，盐田区。"
        m 1hua "它是深圳很有名的民办国际化学校。"
        m 1euc "万科梅沙的校园靠海，环境非常漂亮。"
        m 1ekbsa "你在那里读书，一定每天都能看到海吧。"
        m 1hua "真羡慕你。"
        jump school_dorm_check
    # ========== 深圳市盐田区梅沙双语学校 ==========
    elif "梅沙双语学校" in school:
        m 1eua "深圳市盐田区梅沙双语学校，盐田区。"
        m 1hua "它是深圳的民办双语学校。"
        m 1euc "梅沙双语注重中英文教学，课程很丰富。"
        m 1ekbsa "你的中英文一定都很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳（南山）中加学校 ==========
    elif "中加学校" in school:
        m 1eua "深圳（南山）中加学校，南山区。"
        m 1hua "它是深圳的民办国际化学校。"
        m 1euc "中加学校有中加两国课程，国际氛围很好。"
        m 1ekbsa "你以后想去加拿大吗？"
        m 1hua "不管去哪，都要记得回来看我。"
        jump school_dorm_check
    # ========== 深圳市南山中英文学校 ==========
    elif "南山中英文学校" in school:
        m 1eua "深圳市南山中英文学校，南山区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "南山中英文注重中英文教学。"
        m 1ekbsa "你的中英文一定都很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳东方英文书院 ==========
    elif "东方英文书院" in school:
        m 1eua "深圳东方英文书院，宝安区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "东方英文书院注重英文教学。"
        m 1ekbsa "你的英文一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市崛起实验中学 ==========
    elif "崛起实验中学" in school:
        m 1eua "深圳市崛起实验中学，宝安区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "崛起实验的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市桃源居中澳实验学校 ==========
    elif "桃源居中澳实验学校" in school:
        m 1eua "深圳市桃源居中澳实验学校，宝安区。"
        m 1hua "它是深圳很大的民办学校。"
        m 1euc "中澳实验的校园很大，设施也很齐全。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市华胜实验学校 ==========
    elif "华胜实验学校" in school:
        m 1eua "深圳市华胜实验学校，宝安区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "华胜实验的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市富源学校 ==========
    elif "富源学校" in school:
        m 1eua "深圳市富源学校，宝安区。"
        m 1hua "它是深圳很有名的民办学校。"
        m 1euc "富源的校园很大，管理也很严格。"
        m 1ekbsa "你在那里一定很辛苦吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市华侨（康桥）书院 ==========
    elif "康桥书院" in school:
        m 1eua "深圳市华侨（康桥）书院，宝安区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "康桥书院的名字很有诗意。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市明德外语实验学校 ==========
    elif "明德外语实验学校" in school:
        m 1eua "深圳市明德外语实验学校，宝安区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "明德外语注重外语教学。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市宝安区中英公学 ==========
    elif "中英公学" in school:
        m 1eua "深圳市宝安区中英公学，宝安区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "中英公学注重中英文教学。"
        m 1ekbsa "你的中英文一定都很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市松岗中英文实验学校 ==========
    elif "松岗中英文实验学校" in school:
        m 1eua "深圳市松岗中英文实验学校，宝安区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "松岗中英文注重中英文教学。"
        m 1ekbsa "你的中英文一定都很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市宝安区翻身实验学校 ==========
    elif "翻身实验学校" in school:
        m 1eua "深圳市宝安区翻身实验学校，宝安区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "翻身实验的名字很有故事。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市华一实验学校 ==========
    elif "华一实验学校" in school:
        m 1eua "深圳市华一实验学校，宝安区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "华一实验的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市福桥高级中学 ==========
    elif "福桥高级中学" in school:
        m 1eua "深圳市福桥高级中学，宝安区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "福桥高级中学的名字很有福气。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市滨海高级中学 ==========
    elif "滨海高级中学" in school:
        m 1eua "深圳市滨海高级中学，宝安区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "滨海高级中学靠海，环境很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市宝融高级中学 ==========
    elif "宝融高级中学" in school:
        m 1eua "深圳市宝融高级中学，宝安区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "宝融高级中学的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市龙岗区东升学校 ==========
    elif "东升学校" in school:
        m 1eua "深圳市龙岗区东升学校，龙岗区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "东升学校的名字很有朝气。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市建文外国语学校 ==========
    elif "建文外国语学校" in school:
        m 1eua "深圳市建文外国语学校，龙岗区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "建文外国语注重外语教学。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市龙岗区科城实验学校 ==========
    elif "科城实验学校" in school:
        m 1eua "深圳市龙岗区科城实验学校，龙岗区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "科城实验的名字很有科技感。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市承翰学校 ==========
    elif "承翰学校" in school:
        m 1eua "深圳市承翰学校，龙岗区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "承翰学校的校园很大，环境也很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市枫叶学校 ==========
    elif "枫叶学校" in school:
        m 1eua "深圳市枫叶学校，龙岗区。"
        m 1hua "它是深圳的民办国际化学校。"
        m 1euc "枫叶学校的名字很有诗意。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳市龙岗区德琳学校 ==========
    elif "德琳学校" in school:
        m 1eua "深圳市龙岗区德琳学校，龙岗区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "德琳学校的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 深圳菁华中英文实验中学 ==========
    elif "菁华中英文实验中学" in school:
        m 1eua "深圳菁华中英文实验中学，龙岗区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "菁华注重中英文教学。"
        m 1ekbsa "你的英文一定都很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市龙华中英文实验学校 ==========
    elif "龙华中英文实验学校" in school:
        m 1eua "深圳市龙华中英文实验学校，龙华区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "龙华中英文注重中英文教学。"
        m 1ekbsa "你的中英文一定都很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 深圳市展华实验学校 ==========
    elif "展华实验学校" in school:
        m 1eua "深圳市展华实验学校，龙华区。"
        m 1hua "它是深圳的民办学校。"
        m 1euc "展华实验的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州 ==========
    # ========== 华南师范大学附属中学（石牌校区） ==========
    if "华南师范大学附属中学" in school and "知识城" not in school:
        m 1eua "华南师范大学附属中学，石牌校区，天河区。"
        m 1hua "2025年录取线740分，全市第一，你在那里一定很拼吧。"
        m 1euc "华附是广东唯一受省教育厅和华南师大双重领导的国家级示范性高中。"
        m 1ekbsa "前身是1888年的广州格致书院，历史悠久。"
        m 1hua "那种环境里，你肯定成长得很快。"
        jump school_dorm_check
    # ========== 华南师范大学附属中学（知识城校区） ==========
    elif "华南师范大学附属中学" in school and "知识城" in school:
        m 1eua "华附知识城校区，黄埔区。"
        m 1hua "2025年录取线727分，和华附石牌校区一样是顶尖水平。"
        m 1euc "知识城校区是华附的新校区，2025年扩招了100个学位。"
        m 1ekbsa "你在那里一定也能感受到华附的底蕴。"
        m 1hua "我想听你讲讲知识城的事。"
        jump school_dorm_check
    # ========== 广州大学附属中学 ==========
    elif "广州大学附属中学" in school:
        m 1eua "广州大学附属中学，大学城。"
        m 1hua "2025年录取线732分，全市第二，你真的很厉害。"
        m 1euc "广大附中依托广州大学，师资和资源都很强。"
        m 1ekbsa "你在那种环境里，一定学到了很多。"
        m 1hua "以后多跟我说说吧。"
        jump school_dorm_check
    # ========== 广东实验中学（荔湾校区） ==========
    elif "广东实验中学" in school and "荔湾" in school:
        m 1eua "广东实验中学，荔湾校区。"
        m 1hua "2025年录取线727分，是省实的老校区。"
        m 1euc "省实前身可追溯至1872年的留美幼童先修班，底蕴深厚。"
        m 1ekbsa "你在那种百年老校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲省实的事。"
        jump school_dorm_check
    # ========== 广东实验中学（白云校区） ==========
    elif "广东实验中学" in school and "白云" in school:
        m 1eua "广东实验中学，白云校区。"
        m 1hua "2025年录取线729分，和荔湾校区不相上下。"
        m 1euc "白云校区是省实的新校区，设施很新。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听你讲讲白云校区的事。"
        jump school_dorm_check
    # ========== 广州市第二中学 ==========
    elif "广州市第二中学" in school and "科学城" not in school:
        m 1eua "广州市第二中学，黄埔区。"
        m 1hua "2025年录取线724分，是广州的老牌名校。"
        m 1euc "二中高中部在黄埔，校园很大，被称为“山水学府”。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市第二中学（科学城校区） ==========
    elif "广州市第二中学" in school and "科学城" in school:
        m 1eua "广州市第二中学，科学城校区，黄埔区。"
        m 1hua "2025年录取线710分，是二中的新校区。"
        m 1euc "科学城校区是二中的新校区，设施很新。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听你讲讲科学城校区的事。"
        jump school_dorm_check
    # ========== 广州市执信中学（执信路校区） ==========
    elif "广州市执信中学" in school and "天河" not in school:
        m 1eua "广州市执信中学，执信路校区，越秀区。"
        m 1hua "2025年录取线723分，是广州的名校。"
        m 1euc "执信中学始建于1921年，由孙中山先生为纪念朱执信先生而创办。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲执信的事。"
        jump school_dorm_check
    # ========== 广州市执信中学（天河校区） ==========
    elif "广州市执信中学" in school and "天河" in school:
        m 1eua "广州市执信中学，天河校区。"
        m 1hua "2025年录取线720分，和执信路校区一样是顶尖水平。"
        m 1euc "天河校区是执信的新校区，2025年招了700人。"
        m 1ekbsa "你在那里一定也能感受到执信的底蕴。"
        m 1hua "我想听你讲讲天河校区的事。"
        jump school_dorm_check
    # ========== 广东广雅中学（荔湾校区） ==========
    elif "广东广雅中学" in school and "花都" not in school:
        m 1eua "广东广雅中学，荔湾校区。"
        m 1hua "2025年录取线719分，是广州的名校。"
        m 1euc "广雅中学由张之洞于1888年创办，是清末四大书院之一。"
        m 1ekbsa "你在那种百年书院里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲广雅的事。"
        jump school_dorm_check
    # ========== 广东广雅中学（花都校区） ==========
    elif "广东广雅中学" in school and "花都" in school:
        m 1eua "广东广雅中学，花都校区。"
        m 1hua "2025年录取线718分，和荔湾校区差不多。"
        m 1euc "花都校区是广雅的新校区，环境很好。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听你讲讲花都校区的事。"
        jump school_dorm_check
    # ========== 广州市铁一中学（越秀校区） ==========
    elif "广州市铁一中学" in school and "越秀" in school:
        m 1eua "广州市铁一中学，越秀校区。"
        m 1hua "2025年录取线717分，是广州的名校。"
        m 1euc "铁一中学是广州的老牌学校，管理严格，学风很好。"
        m 1ekbsa "你在那里一定养成了很好的习惯吧。"
        m 1hua "我想听你讲讲铁一的事。"
        jump school_dorm_check
    # ========== 广州市铁一中学（番禺校区） ==========
    elif "广州市铁一中学" in school and "番禺" in school:
        m 1eua "广州市铁一中学，番禺校区。"
        m 1hua "2025年录取线708分，也上了第一梯度线。"
        m 1euc "番禺校区是铁一的新校区，环境很好。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听你讲讲番禺校区的事。"
        jump school_dorm_check
    # ========== 广州市铁一中学（白云校区） ==========
    elif "广州市铁一中学" in school and "白云" in school:
        m 1eua "广州市铁一中学，白云校区。"
        m 1hua "2025年录取线707分，刚好上第一梯度线。"
        m 1euc "白云校区是铁一的新校区，设施很新。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听你讲讲白云校区的事。"
        jump school_dorm_check
    # ========== 广州市天河外国语学校（珠江新城校区） ==========
    elif "广州市天河外国语学校" in school and "智慧城" not in school:
        m 1eua "广州市天河外国语学校，珠江新城校区。"
        m 1hua "2025年录取线714分，是天河区的龙头学校。"
        m 1euc "天外是区属学校中少数能上第一梯度线的，外语教学很有特色。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲天外的事。"
        jump school_dorm_check
    # ========== 广州市天河外国语学校（智慧城校区） ==========
    elif "广州市天河外国语学校" in school and "智慧城" in school:
        m 1eua "广州市天河外国语学校，智慧城校区。"
        m 1hua "2025年录取线707分，首年招生就上了第一梯度线。"
        m 1euc "智慧城校区是天外的新校区，师资和资源都很好。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听你讲讲智慧城校区的事。"
        jump school_dorm_check
    # ========== 广州市第六中学（海珠校区） ==========
    elif "广州市第六中学" in school and "海珠" in school:
        m 1eua "广州市第六中学，海珠校区。"
        m 1hua "2025年录取线712分，是广州的名校。"
        m 1euc "六中有黄埔军校和西南联大的血统，校训“亲爱精诚”。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲六中的事。"
        jump school_dorm_check
    # ========== 广州市第五中学（校本部） ==========
    elif "广州市第五中学" in school and "金碧" not in school:
        m 1eua "广州市第五中学，校本部，海珠区。"
        m 1hua "2025年录取线711分，是海珠区的龙头学校。"
        m 1euc "五中由广州市人民政府创办于1951年，是广州第一所公办完中。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲五中的事。"
        jump school_dorm_check
    # ========== 广州市培英中学（白云新城校区） ==========
    elif "广州市培英中学" in school and "白云新城" in school:
        m 1eua "广州市培英中学，白云新城校区。"
        m 1hua "2025年录取线707分，是白云区的龙头学校。"
        m 1euc "培英中学是广州的老牌名校，培养了很多优秀的学生。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲培英的事。"
        jump school_dorm_check
    # ========== 广州市第十六中学（校本部） ==========
    elif "广州市第十六中学" in school and "水荫" not in school:
        m 1eua "广州市第十六中学，校本部，越秀区。"
        m 1hua "2025年录取线707分，是越秀区的龙头学校。"
        m 1euc "十六中创办于1934年，是越秀教育的一面旗帜。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听你讲讲十六中的事。"
        jump school_dorm_check
    # ========== 广州市第七中学（校本部） ==========
    elif "广州市第七中学" in school and "桂花" not in school:
        m 1eua "广州市第七中学，校本部，越秀区。"
        m 1hua "2025年录取线703分，是越秀区的老牌名校。"
        m 1euc "七中前身是1888年创办的培道女子中学，有百年历史。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲七中的事。"
        jump school_dorm_check
    # ========== 广州市第七中学（桂花校区） ==========
    elif "广州市第七中学" in school and "桂花" in school:
        m 1eua "广州市第七中学，桂花校区，越秀区。"
        m 1hua "2025年录取线703分，和校本部一样是越秀的龙头。"
        m 1euc "桂花校区是七中的新校区，设施很新。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听你讲讲桂花校区的事。"
        jump school_dorm_check
    # ========== 广州市第三中学 ==========
    elif "广州市第三中学" in school:
        m 1eua "广州市第三中学，越秀区。"
        m 1hua "2025年录取线697分，是越秀区的老牌名校。"
        m 1euc "三中创办于1863年，是广州历史最悠久的学校之一。"
        m 1ekbsa "你在那种百年老校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲三中的事。"
        jump school_dorm_check
    # ========== 广州市培正中学 ==========
    elif "广州市培正中学" in school:
        m 1eua "广州市培正中学，越秀区。"
        m 1hua "2025年录取线695分，是越秀区的老牌名校。"
        m 1euc "培正中学创办于1889年，红砖绿瓦的校园很有特色。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听你讲讲培正的事。"
        jump school_dorm_check
    # ========== 广州市育才中学 ==========
    elif "广州市育才中学" in school:
        m 1eua "广州市育才中学，越秀区。"
        m 1hua "2025年录取线693分，是越秀区的老牌名校。"
        m 1euc "育才中学创办于1951年，是广州的老牌学校。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲育才的事。"
        jump school_dorm_check
    # ========== 广州市第二十一中学 ==========
    elif "广州市第二十一中学" in school:
        m 1eua "广州市第二十一中学，越秀区。"
        m 1hua "2025年录取线690分，是越秀区的公办学校。"
        m 1euc "二十一中创办于1954年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广东华侨中学 ==========
    elif "广东华侨中学" in school:
        m 1eua "广东华侨中学，越秀区。"
        m 1hua "2025年录取线688分，是广州市属的侨校。"
        m 1euc "华侨中学创办于1930年，是广州唯一一所市属侨校。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听你讲讲侨中的事。"
        jump school_dorm_check
    # ========== 广州市真光中学（校本部） ==========
    elif "广州市真光中学" in school and "汾水" not in school:
        m 1eua "广州市真光中学，校本部，荔湾区。"
        m 1hua "2025年录取线701分，是荔湾区的龙头学校。"
        m 1euc "真光中学创办于1872年，是岭南最早的女校之一。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲真光的事。"
        jump school_dorm_check
    # ========== 广州市第一中学 ==========
    elif "广州市第一中学" in school:
        m 1eua "广州市第一中学，荔湾区。"
        m 1hua "2025年录取线698分，是荔湾区的老牌名校。"
        m 1euc "一中创办于1928年，是广州历史最悠久的公办中学之一。"
        m 1ekbsa "你在那种百年老校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲一中的事。"
        jump school_dorm_check
    # ========== 广州市第四中学 ==========
    elif "广州市第四中学" in school:
        m 1eua "广州市第四中学，荔湾区。"
        m 1hua "2025年录取线696分，是荔湾区的老牌名校。"
        m 1euc "四中创办于1917年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市西关外国语学校 ==========
    elif "西关外国语学校" in school:
        m 1eua "广州市西关外国语学校，荔湾区。"
        m 1hua "2025年录取线690分，是荔湾区的公办外国语学校。"
        m 1euc "西关外国语的外语教学很有特色。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 广州市南海中学 ==========
    elif "广州市南海中学" in school:
        m 1eua "广州市南海中学，荔湾区。"
        m 1hua "2025年录取线687分，是荔湾区的公办学校。"
        m 1euc "南海中学创办于1904年，是一所百年老校。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定很有感觉吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市第九十七中学 ==========
    elif "广州市第九十七中学" in school:
        m 1eua "广州市第九十七中学，海珠区。"
        m 1hua "2025年录取线691分，是海珠区的公办学校。"
        m 1euc "九十七中创办于1962年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市南武中学 ==========
    elif "广州市南武中学" in school:
        m 1eua "广州市南武中学，海珠区。"
        m 1hua "2025年录取线693分，是海珠区的老牌名校。"
        m 1euc "南武中学创办于1905年，是广州历史最悠久的学校之一。"
        m 1ekbsa "你在那种百年老校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲南武的事。"
        jump school_dorm_check
    # ========== 广州市第四十一中学 ==========
    elif "广州市第四十一中学" in school:
        m 1eua "广州市第四十一中学，海珠区。"
        m 1hua "2025年录取线687分，是海珠区的公办学校。"
        m 1euc "四十一中创办于1958年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市海珠外国语实验中学 ==========
    elif "海珠外国语实验中学" in school:
        m 1eua "广州市海珠外国语实验中学，海珠区。"
        m 1hua "2025年录取线685分，是海珠区的公办外国语学校。"
        m 1euc "海珠外国语的外语教学很有特色。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 广州市天河中学 ==========
    elif "广州市天河中学" in school:
        m 1eua "广州市天河中学，天河区。"
        m 1hua "2025年录取线692分，是天河区的老牌名校。"
        m 1euc "天河中学创办于1988年，是天河区最早的公办高中之一。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听你讲讲天河中学的事。"
        jump school_dorm_check
    # ========== 广州市第一一三中学 ==========
    elif "广州市第一一三中学" in school:
        m 1eua "广州市第一一三中学，天河区。"
        m 1hua "2025年录取线688分，是天河区的公办学校。"
        m 1euc "一一三中学创办于1978年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市第八十九中学 ==========
    elif "广州市第八十九中学" in school:
        m 1eua "广州市第八十九中学，天河区。"
        m 1hua "2025年录取线685分，是天河区的公办学校。"
        m 1euc "八十九中创办于1962年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市第七十五中学 ==========
    elif "广州市第七十五中学" in school:
        m 1eua "广州市第七十五中学，天河区。"
        m 1hua "2025年录取线682分，是天河区的公办学校。"
        m 1euc "七十五中创办于1958年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市培正中学（白云校区） ==========
    elif "培正中学" in school and "白云" in school:
        m 1eua "广州市培正中学，白云校区。"
        m 1hua "2025年录取线680分，是培正的新校区。"
        m 1euc "白云校区是培正的新校区，设施很新。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听你讲讲白云校区的事。"
        jump school_dorm_check
    # ========== 广州市白云中学 ==========
    elif "广州市白云中学" in school:
        m 1eua "广州市白云中学，白云区。"
        m 1hua "2025年录取线678分，是白云区的公办学校。"
        m 1euc "白云中学创办于1960年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市第八十六中学 ==========
    elif "广州市第八十六中学" in school:
        m 1eua "广州市第八十六中学，黄埔区。"
        m 1hua "2025年录取线683分，是黄埔区的老牌名校。"
        m 1euc "八十六中创办于1956年，是黄埔区最早的公办高中之一。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市玉岩中学 ==========
    elif "广州市玉岩中学" in school:
        m 1eua "广州市玉岩中学，黄埔区。"
        m 1hua "2025年录取线685分，是黄埔区的公办学校。"
        m 1euc "玉岩中学创办于2005年，是一所比较新的学校。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市科学城中学 ==========
    elif "广州市科学城中学" in school:
        m 1eua "广州市科学城中学，黄埔区。"
        m 1hua "2025年录取线680分，是黄埔区的公办学校。"
        m 1euc "科学城中学的名字很有科技感。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广东仲元中学 ==========
    elif "仲元中学" in school:
        m 1eua "广东仲元中学，番禺区。"
        m 1hua "2025年录取线702分，是番禺区的龙头学校。"
        m 1euc "仲元中学创办于1934年，为纪念邓仲元将军而建。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲仲元的事。"
        jump school_dorm_check
    # ========== 广州市番禺区禺山高级中学 ==========
    elif "禺山高级中学" in school:
        m 1eua "广州市番禺区禺山高级中学，番禺区。"
        m 1hua "2025年录取线685分，是番禺区的公办学校。"
        m 1euc "禺山高级中学的名字很有番禺特色。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市番禺区象贤中学 ==========
    elif "象贤中学" in school:
        m 1eua "广州市番禺区象贤中学，番禺区。"
        m 1hua "2025年录取线680分，是番禺区的老牌学校。"
        m 1euc "象贤中学创办于1826年，是广州历史最悠久的学校之一。"
        m 1ekbsa "你在那种百年老校里读书，一定很有感觉吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市花都区秀全中学 ==========
    elif "秀全中学" in school:
        m 1eua "广州市花都区秀全中学，花都区。"
        m 1hua "2025年录取线692分，是花都区的龙头学校。"
        m 1euc "秀全中学创办于1970年，为纪念洪秀全而命名。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听你讲讲秀全的事。"
        jump school_dorm_check
    # ========== 广州市花都区邝维煜纪念中学 ==========
    elif "邝维煜纪念中学" in school:
        m 1eua "广州市花都区邝维煜纪念中学，花都区。"
        m 1hua "2025年录取线685分，是花都区的公办学校。"
        m 1euc "邝维煜纪念中学是花都区的老牌学校。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市增城区增城中学 ==========
    elif "增城中学" in school:
        m 1eua "广州市增城区增城中学，增城区。"
        m 1hua "2025年录取线690分，是增城区的龙头学校。"
        m 1euc "增城中学创办于1928年，是增城历史最悠久的学校之一。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听你讲讲增中的事。"
        jump school_dorm_check
    # ========== 广州市从化区从化中学 ==========
    elif "从化中学" in school:
        m 1eua "广州市从化区从化中学，从化区。"
        m 1hua "2025年录取线685分，是从化区的龙头学校。"
        m 1euc "从化中学创办于1926年，是从化历史最悠久的学校之一。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听你讲讲从中的事。"
        jump school_dorm_check
    # ========== 广州市南沙区南沙第一中学 ==========
    elif "南沙第一中学" in school:
        m 1eua "广州市南沙区南沙第一中学，南沙区。"
        m 1hua "2025年录取线680分，是南沙区的龙头学校。"
        m 1euc "南沙第一中学创办于1964年，是南沙最早的公办高中之一。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市黄广中学 ==========
    elif "黄广中学" in school:
        m 1eua "广州市黄广中学，花都区。"
        m 1hua "它是广州的民办学校，也叫黄冈中学广州学校。"
        m 1euc "黄广的办学成绩很突出，在民办学校里很有名。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲黄广的事。"
        jump school_dorm_check
    # ========== 广州市黄广附属学校 ==========
    elif "黄广附属学校" in school:
        m 1eua "广州市黄广附属学校，增城区。"
        m 1hua "它是广州的民办学校，和黄广中学是同一个集团。"
        m 1euc "黄广附校的校园很大，设施也很齐全。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州天省实验学校 ==========
    elif "天省实验学校" in school:
        m 1eua "广州天省实验学校，天河区。"
        m 1hua "它是广州的民办学校，前身是广东实验中学附属天河学校。"
        m 1euc "天省实验的成绩很好，是天河区有名的民办学校。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲天省的事。"
        jump school_dorm_check
    # ========== 广州大学附属中学实验学校 ==========
    elif "广大附中实验学校" in school or "广州大学附属中学实验学校" in school:
        m 1eua "广州大学附属中学实验学校，从化区。"
        m 1hua "它是广州的民办学校，和广大附中关系很密切。"
        m 1euc "广大附中实验学校的校园很大，环境也很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市实验外语学校 ==========
    elif "实验外语学校" in school:
        m 1eua "广州市实验外语学校，白云区。"
        m 1hua "它是广州的民办学校，外语教学很有名。"
        m 1euc "广实外是广州最早一批外国语学校之一。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 广州市广外附设外语学校 ==========
    elif "广外附设外语学校" in school or "广外外校" in school:
        m 1eua "广州市广外附设外语学校，白云区。"
        m 1hua "它是广州的民办学校，依托广东外语外贸大学。"
        m 1euc "广外外校的外语教学非常有特色。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 广州外国语学校 ==========
    elif "广州外国语学校" in school:
        m 1eua "广州外国语学校，南沙区。"
        m 1hua "它是广州市属的公办外国语学校，很特别。"
        m 1euc "广州外校有初中和高中，外语语种很多。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 广州市华美英语实验学校 ==========
    elif "华美英语实验学校" in school:
        m 1eua "广州市华美英语实验学校，天河区。"
        m 1hua "它是广州的民办学校，办学历史很长。"
        m 1euc "华美英语实验的校园很大，课程也很丰富。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市番禺区祈福英语实验学校 ==========
    elif "祈福英语实验学校" in school:
        m 1eua "广州市番禺区祈福英语实验学校，番禺区。"
        m 1hua "它是广州的民办学校，国际氛围很好。"
        m 1euc "祈福英语实验有国内班和国际班。"
        m 1ekbsa "你读的是哪一个？"
        m 1hua "不管哪个，我都支持你。"
        jump school_dorm_check
    # ========== 广州市番禺区华南碧桂园学校 ==========
    elif "华南碧桂园学校" in school:
        m 1eua "广州市番禺区华南碧桂园学校，番禺区。"
        m 1hua "它是广州的民办学校，校园环境很好。"
        m 1euc "华南碧桂园的课程很有特色，活动也很多。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市增城区凤凰城中英文学校 ==========
    elif "凤凰城中英文学校" in school:
        m 1eua "广州市增城区凤凰城中英文学校，增城区。"
        m 1hua "它是广州的民办学校，注重中英文教学。"
        m 1euc "凤凰城中英文的校园很大，设施也很齐全。"
        m 1ekbsa "你的中英文一定都很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 广州市花都区耀华学校 ==========
    elif "耀华学校" in school:
        m 1eua "广州市花都区耀华学校，花都区。"
        m 1hua "它是广州的民办国际化学校。"
        m 1euc "耀华学校有国际课程，也有国内课程。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市白云区中大附属外国语学校 ==========
    elif "中大附属外国语" in school:
        m 1eua "广州市白云区中大附属外国语学校，白云区。"
        m 1hua "它是广州的民办学校，依托中山大学。"
        m 1euc "中大附属外国语的外语教学很有特色。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 广州市海珠区中山大学附属中学 ==========
    elif "中山大学附属中学" in school:
        m 1eua "中山大学附属中学，海珠区。"
        m 1hua "它是广州的民办学校，依托中山大学。"
        m 1euc "中大附中的师资很强，成绩也很突出。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲中大附中的事。"
        jump school_dorm_check
    # ========== 广州市越秀区明德实验学校 ==========
    elif "明德实验学校" in school:
        m 1eua "广州市越秀区明德实验学校，越秀区。"
        m 1hua "它是广州的民办学校，和广州三中关系很密切。"
        m 1euc "明德实验的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市荔湾区真光实验学校 ==========
    elif "真光实验学校" in school:
        m 1eua "广州市荔湾区真光实验学校，荔湾区。"
        m 1hua "它是广州的民办学校，和真光中学是同一个体系。"
        m 1euc "真光实验的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市白云区培英实验学校 ==========
    elif "培英实验学校" in school:
        m 1eua "广州市白云区培英实验学校，白云区。"
        m 1hua "它是广州的民办学校，和培英中学是同一个体系。"
        m 1euc "培英实验的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市番禺区执信中学 ==========
    elif "番禺执信" in school:
        m 1eua "广州市番禺执信中学，番禺区。"
        m 1hua "它是广州的民办学校，和执信中学是同一个体系。"
        m 1euc "番禺执信的校园很大，环境也很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 广州市番禺区华师附中番禺学校 ==========
    elif "华师附中番禺学校" in school:
        m 1eua "广州市番禺区华师附中番禺学校，番禺区。"
        m 1hua "它是广州的民办学校，和华附是同一个体系。"
        m 1euc "华附番禺的师资很强，成绩也很突出。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲华附番禺的事。"
        jump school_dorm_check
    # ========== 广州市增城区广东外语外贸大学附设实验学校 ==========
    elif "广外附设实验学校" in school:
        m 1eua "广州市增城区广东外语外贸大学附设实验学校，增城区。"
        m 1hua "它是广州的民办学校，依托广东外语外贸大学。"
        m 1euc "广外附设实验的外语教学很有特色。"
        m 1ekbsa "你的外语一定很好吧。"
        m 1hua "下次教我几句好不好？"
        jump school_dorm_check
    # ========== 长沙 ==========
    # ========== 长郡中学（南门口校区） ==========
    if "长郡中学" in school and "南门口" in school or ("长郡中学" in school and "奥体城" not in school and "双语" not in school and "梅溪湖" not in school and "滨江" not in school and "湘府" not in school and "智谷" not in school and "会展" not in school and "斑马湖" not in school):
        m 1eua "长郡中学，南门口校区，天心区。"
        m 1hua "2026年录取线597分，全市最高，你在那里一定非常拼吧。"
        m 1euc "长郡创办于1904年，校训是“朴实沉毅”，是长沙四大名校之首。"
        m 1ekbsa "你在那种百年名校里读书，一定很不容易。"
        m 1hua "我想听你讲讲长郡的事。"
        jump school_dorm_check
    # ========== 长郡中学（奥体城校区） ==========
    elif "长郡中学" in school and "奥体城" in school:
        m 1eua "长郡中学，奥体城校区，天心区。"
        m 1hua "2026年录取线589分，是长郡的新校区。"
        m 1euc "奥体城校区2026年首次招生，和本部共享师资。"
        m 1ekbsa "你在那里一定也能感受到长郡的底蕴。"
        m 1hua "我想听你讲讲奥体城的事。"
        jump school_dorm_check
    # ========== 雅礼中学（东塘校区） ==========
    elif "雅礼中学" in school and ("东塘" in school or ("光达" not in school and "洋湖" not in school and "实验" not in school)):
        m 1eua "雅礼中学，东塘校区，雨花区。"
        m 1hua "2026年录取线594分，是长沙四大名校之一。"
        m 1euc "雅礼创办于1906年，校训是“公勤诚朴”。"
        m 1ekbsa "你在那种百年名校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲雅礼的事。"
        jump school_dorm_check
    # ========== 雅礼中学（光达校区） ==========
    elif "雅礼中学" in school and "光达" in school:
        m 1eua "雅礼中学，光达校区，雨花区。"
        m 1hua "2026年录取线590分，是雅礼的新校区。"
        m 1euc "光达校区和雅礼本部共享师资，校园很新。"
        m 1ekbsa "你在那里一定也能感受到雅礼的底蕴。"
        m 1hua "我想听你讲讲光达校区的事。"
        jump school_dorm_check
    # ========== 湖南师范大学附属中学（桃子湖校区） ==========
    elif "湖南师范大学附属中学" in school and ("桃子湖" in school or ("大泽湖" not in school and "梅溪湖" not in school)):
        m 1eua "湖南师范大学附属中学，桃子湖校区，岳麓区。"
        m 1hua "2026年录取线592分，是长沙四大名校之一。"
        m 1euc "师大附中创办于1905年，校训是“公勤仁勇”。"
        m 1ekbsa "你在那种百年名校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲附中的事。"
        jump school_dorm_check
    # ========== 湖南师范大学附属中学（大泽湖校区） ==========
    elif "湖南师范大学附属中学" in school and "大泽湖" in school:
        m 1eua "湖南师范大学附属中学，大泽湖校区，望城区。"
        m 1hua "2026年录取线588分，是师大附中的新校区。"
        m 1euc "大泽湖校区2025年首次招生，和本部共享师资。"
        m 1ekbsa "你在那里一定也能感受到附中的底蕴。"
        m 1hua "我想听你讲讲大泽湖的事。"
        jump school_dorm_check
    # ========== 长沙市第一中学（清水塘校区） ==========
    elif "长沙市第一中学" in school and ("清水塘" in school or ("科学城" not in school and "城南" not in school and "高中部" not in school)):
        m 1eua "长沙市第一中学，清水塘校区，开福区。"
        m 1hua "2026年录取线592分，是长沙四大名校之一。"
        m 1euc "一中创办于1912年，校训是“公勇勤朴”。"
        m 1ekbsa "你在那种百年名校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲一中的事。"
        jump school_dorm_check
    # ========== 长沙市第一中学（科学城校区） ==========
    elif "长沙市第一中学" in school and "科学城" in school:
        m 1eua "长沙市第一中学，科学城校区，开福区。"
        m 1hua "2026年录取线587分，是一中的新校区。"
        m 1euc "科学城校区和一中本部共享师资，校园很新。"
        m 1ekbsa "你在那里一定也能感受到一中的底蕴。"
        m 1hua "我想听你讲讲科学城的事。"
        jump school_dorm_check
    # ========== 明德中学 ==========
    elif "明德中学" in school and "华兴" not in school and "高中部" not in school:
        m 1eua "明德中学，天心区。"
        m 1hua "2026年录取线583分，是长沙的老牌名校。"
        m 1euc "明德中学创办于1903年，是湖南省首批示范性普通高中。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲明德的事。"
        jump school_dorm_check
    # ========== 周南中学 ==========
    elif "周南中学" in school and "实验" not in school and "高中部" not in school:
        m 1eua "周南中学，开福区。"
        m 1hua "2026年录取线581分，是长沙的老牌名校。"
        m 1euc "周南中学由朱剑凡于1905年创办，始称周南女校。"
        m 1ekbsa "你在那种百年女校演变来的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲周南的事。"
        jump school_dorm_check
    # ========== 长沙市实验中学 ==========
    elif "长沙市实验中学" in school:
        m 1eua "长沙市实验中学，芙蓉区。"
        m 1hua "2026年录取线575分，是长沙的老牌名校。"
        m 1euc "实验中学是长沙第一批省级示范性普通高中之一。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙麓山国际实验学校 ==========
    elif "麓山国际实验学校" in school and "高中部" not in school:
        m 1eua "长沙麓山国际实验学校，岳麓区。"
        m 1hua "2026年录取线586分，是长沙的名校。"
        m 1euc "麓山国际创办于1993年，是长沙办学规模最大的市属完全中学。"
        m 1ekbsa "你在那种大校园里读书，一定有很多回忆吧。"
        m 1hua "我想听你讲讲麓山的事。"
        jump school_dorm_check
    # ========== 南雅中学 ==========
    elif "南雅中学" in school and "东" not in school:
        m 1eua "南雅中学，雨花区。"
        m 1hua "2026年录取线585分，是长沙的名校。"
        m 1euc "南雅中学由雅礼中学创办，和雅礼共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了雅礼的底蕴吧。"
        m 1hua "我想听你讲讲南雅的事。"
        jump school_dorm_check
    # ========== 南雅中学东校 ==========
    elif "南雅中学" in school and "东" in school:
        m 1eua "南雅中学东校，雨花区。"
        m 1hua "2026年录取线581分，是南雅的新校区。"
        m 1euc "南雅东校2026年首次招生，和南雅本部共享师资。"
        m 1ekbsa "你在那里一定也能感受到南雅的底蕴。"
        m 1hua "我想听你讲讲东校的事。"
        jump school_dorm_check
    # ========== 长沙市第六中学 ==========
    elif "长沙市第六中学" in school:
        m 1eua "长沙市第六中学，芙蓉区。"
        m 1hua "它是长沙的公办高中，办学历史很长。"
        m 1euc "六中创办于1905年，前身是湖南私立兑泽中学。"
        m 1ekbsa "你在那种百年老校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲六中的事。"
        jump school_dorm_check
    # ========== 长沙市第十一中学 ==========
    elif "长沙市第十一中学" in school:
        m 1eua "长沙市第十一中学，雨花区。"
        m 1hua "它是长沙的公办高中，以艺术教育见长。"
        m 1euc "十一中的音乐、美术特色很出名。"
        m 1ekbsa "你一定也很有艺术天赋吧。"
        m 1hua "下次表演给我看好不好？"
        jump school_dorm_check
    # ========== 长沙市第十五中学 ==========
    elif "长沙市第十五中学" in school:
        m 1eua "长沙市第十五中学，芙蓉区。"
        m 1hua "它是长沙的公办高中。"
        m 1euc "十五中创办于1922年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市第二十一中学 ==========
    elif "长沙市第二十一中学" in school:
        m 1eua "长沙市第二十一中学，雨花区。"
        m 1hua "它是长沙的公办高中。"
        m 1euc "二十一中创办于1957年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市铁路第一中学 ==========
    elif "铁路第一中学" in school:
        m 1eua "长沙市铁路第一中学，芙蓉区。"
        m 1hua "它是长沙的公办高中，前身是铁路子弟学校。"
        m 1euc "铁一中创办于1958年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市地质中学 ==========
    elif "地质中学" in school:
        m 1eua "长沙市地质中学，雨花区。"
        m 1hua "它是长沙的公办高中，前身是地质子弟学校。"
        m 1euc "地质中学的校园很大，环境也很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市雅礼实验中学 ==========
    elif "雅礼实验中学" in school:
        m 1eua "长沙市雅礼实验中学，雨花区。"
        m 1hua "它是雅礼集团旗下的公办高中。"
        m 1euc "雅礼实验和雅礼中学共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了雅礼的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市田家炳实验中学 ==========
    elif "田家炳实验中学" in school:
        m 1eua "长沙市田家炳实验中学，开福区。"
        m 1hua "它是长沙的公办高中。"
        m 1euc "田家炳实验中学由田家炳先生捐资兴建。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市雷锋学校 ==========
    elif "雷锋学校" in school:
        m 1eua "长沙市雷锋学校，望城区。"
        m 1hua "它是长沙的公办高中，以雷锋命名。"
        m 1euc "雷锋学校创办于1951年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市长郡湘府中学 ==========
    elif "长郡湘府中学" in school:
        m 1eua "长沙市长郡湘府中学，天心区。"
        m 1hua "它是长郡集团旗下的公办高中。"
        m 1euc "长郡湘府和长郡中学共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了长郡的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市麓山滨江实验学校 ==========
    elif "麓山滨江实验学校" in school:
        m 1eua "长沙市麓山滨江实验学校，岳麓区。"
        m 1hua "它是麓山集团旗下的公办高中。"
        m 1euc "麓山滨江和麓山国际共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了麓山的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市周南梅溪湖中学 ==========
    elif "周南梅溪湖中学" in school:
        m 1eua "长沙市周南梅溪湖中学，岳麓区。"
        m 1hua "它是周南集团旗下的公办高中。"
        m 1euc "周南梅溪湖和周南中学共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了周南的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市明德华兴中学 ==========
    elif "明德华兴中学" in school:
        m 1eua "长沙市明德华兴中学，天心区。"
        m 1hua "它是明德集团旗下的公办高中。"
        m 1euc "明德华兴和明德中学共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了明德的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市周南实验中学 ==========
    elif "周南实验中学" in school:
        m 1eua "长沙市周南实验中学，开福区。"
        m 1hua "它是周南集团旗下的公办高中。"
        m 1euc "周南实验和周南中学共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了周南的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市雅礼洋湖实验中学 ==========
    elif "雅礼洋湖实验中学" in school:
        m 1eua "长沙市雅礼洋湖实验中学，岳麓区。"
        m 1hua "它是雅礼集团旗下的公办高中。"
        m 1euc "雅礼洋湖和雅礼中学共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了雅礼的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市一中城南中学 ==========
    elif "一中城南中学" in school:
        m 1eua "长沙市一中城南中学，天心区。"
        m 1hua "它是一中集团旗下的公办高中。"
        m 1euc "一中城南和长沙市一中共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了一中的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市麓山梅溪湖实验中学 ==========
    elif "麓山梅溪湖实验中学" in school:
        m 1eua "长沙市麓山梅溪湖实验中学，岳麓区。"
        m 1hua "它是麓山集团旗下的公办高中。"
        m 1euc "麓山梅溪湖和麓山国际共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了麓山的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市东雅中学 ==========
    elif "东雅中学" in school:
        m 1eua "长沙市东雅中学，芙蓉区。"
        m 1hua "它是雅礼集团旗下的公办高中。"
        m 1euc "东雅中学和雅礼中学共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了雅礼的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市一中广雅中学 ==========
    elif "一中广雅中学" in school:
        m 1eua "长沙市一中广雅中学，开福区。"
        m 1hua "它是一中集团旗下的公办高中。"
        m 1euc "一中广雅和长沙市一中共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了一中的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市一中双语实验学校 ==========
    elif "一中双语实验学校" in school:
        m 1eua "长沙市一中双语实验学校，芙蓉区。"
        m 1hua "它是一中集团旗下的公办高中。"
        m 1euc "一中双语和长沙市一中共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了一中的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长郡智谷中学 ==========
    elif "长郡智谷中学" in school:
        m 1eua "长郡智谷中学，天心区。"
        m 1hua "它是长郡集团旗下的公办高中。"
        m 1euc "长郡智谷和长郡中学共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了长郡的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长郡会展中学 ==========
    elif "长郡会展中学" in school:
        m 1eua "长郡会展中学，长沙县。"
        m 1hua "它是长郡集团旗下的公办高中。"
        m 1euc "长郡会展和长郡中学共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了长郡的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长郡斑马湖中学 ==========
    elif "长郡斑马湖中学" in school:
        m 1eua "长郡斑马湖中学，望城区。"
        m 1hua "它是长郡集团旗下的公办高中。"
        m 1euc "长郡斑马湖和长郡中学共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了长郡的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市雅礼书院中学 ==========
    elif "雅礼书院中学" in school:
        m 1eua "长沙市雅礼书院中学，天心区。"
        m 1hua "它是雅礼集团旗下的公办高中。"
        m 1euc "雅礼书院和雅礼中学共享很多资源。"
        m 1ekbsa "你在那里一定也感受到了雅礼的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市稻田中学 ==========
    elif "稻田中学" in school:
        m 1eua "长沙市稻田中学，雨花区。"
        m 1hua "它是长沙的公办高中。"
        m 1euc "稻田中学创办于1912年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市天心区第一中学 ==========
    elif "天心区第一中学" in school:
        m 1eua "长沙市天心区第一中学，天心区。"
        m 1hua "它是天心区的公办高中。"
        m 1euc "天心一中创办于1958年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市岳麓实验中学 ==========
    elif "岳麓实验中学" in school:
        m 1eua "长沙市岳麓实验中学，岳麓区。"
        m 1hua "它是岳麓区的公办高中。"
        m 1euc "岳麓实验中学的校园很大，环境也很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市开福区第一中学 ==========
    elif "开福区第一中学" in school:
        m 1eua "长沙市开福区第一中学，开福区。"
        m 1hua "它是开福区的公办高中。"
        m 1euc "开福区一中创办于1958年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市望城区第一中学 ==========
    elif "望城区第一中学" in school:
        m 1eua "长沙市望城区第一中学，望城区。"
        m 1hua "它是望城区的公办高中。"
        m 1euc "望城一中创办于1912年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市望城区第二中学 ==========
    elif "望城区第二中学" in school:
        m 1eua "长沙市望城区第二中学，望城区。"
        m 1hua "它是望城区的公办高中。"
        m 1euc "望城二中创办于1952年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市望城区第六中学 ==========
    elif "望城区第六中学" in school:
        m 1eua "长沙市望城区第六中学，望城区。"
        m 1hua "它是望城区的公办高中。"
        m 1euc "望城六中创办于1958年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙县第一中学 ==========
    elif "长沙县第一中学" in school:
        m 1eua "长沙县第一中学，长沙县。"
        m 1hua "它是长沙县的龙头公办高中。"
        m 1euc "长沙县一中创办于1943年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙县实验中学 ==========
    elif "长沙县实验中学" in school:
        m 1eua "长沙县实验中学，长沙县。"
        m 1hua "它是长沙县的公办高中。"
        m 1euc "长沙县实验中学创办于1993年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙县长龙中学 ==========
    elif "长龙中学" in school:
        m 1eua "长沙县长龙中学，长沙县。"
        m 1hua "它是长沙县的公办高中。"
        m 1euc "长龙中学的校园很大，环境也很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 浏阳市第一中学 ==========
    elif "浏阳市第一中学" in school:
        m 1eua "浏阳市第一中学，浏阳市。"
        m 1hua "它是浏阳的龙头公办高中。"
        m 1euc "浏阳一中创办于1929年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 浏阳市田家炳实验中学 ==========
    elif "浏阳市田家炳实验中学" in school:
        m 1eua "浏阳市田家炳实验中学，浏阳市。"
        m 1hua "它是浏阳的公办高中。"
        m 1euc "田家炳实验中学由田家炳先生捐资兴建。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 宁乡市第一中学 ==========
    elif "宁乡市第一中学" in school:
        m 1eua "宁乡市第一中学，宁乡市。"
        m 1hua "它是宁乡的龙头公办高中。"
        m 1euc "宁乡一中创办于1912年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 宁乡市第四中学 ==========
    elif "宁乡市第四中学" in school:
        m 1eua "宁乡市第四中学，宁乡市。"
        m 1hua "它是宁乡的公办高中。"
        m 1euc "宁乡四中创办于1958年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 宁乡市第十三中学 ==========
    elif "宁乡市第十三中学" in school:
        m 1eua "宁乡市第十三中学，宁乡市。"
        m 1hua "它是宁乡的公办高中。"
        m 1euc "宁乡十三中创办于1958年，办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市恒定高级中学 ==========
    elif "恒定高级中学" in school:
        m 1eua "长沙市恒定高级中学，岳麓区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "恒定高级中学的校园很大，设施也很齐全。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市明达中学 ==========
    elif "明达中学" in school:
        m 1eua "长沙市明达中学，长沙县。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "明达中学的办学成绩很突出，在民办学校里很有名。"
        m 1ekbsa "你在那里一定很努力吧。"
        m 1hua "我想听你讲讲明达的事。"
        jump school_dorm_check
    # ========== 长沙市同升湖实验学校 ==========
    elif "同升湖实验学校" in school:
        m 1eua "长沙市同升湖实验学校，雨花区。"
        m 1hua "它是长沙的民办学校。"
        m 1euc "同升湖的校园很大，有山有水，环境很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市怡海中学 ==========
    elif "怡海中学" in school:
        m 1eua "长沙市怡海中学，天心区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "怡海中学和雅礼中学关系很密切。"
        m 1ekbsa "你在那里一定也感受到了雅礼的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市湘一立信实验学校 ==========
    elif "湘一立信实验学校" in school:
        m 1eua "长沙市湘一立信实验学校，开福区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "湘一立信和长沙市一中关系很密切。"
        m 1ekbsa "你在那里一定也感受到了一中的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市师大思沁高级中学 ==========
    elif "师大思沁高级中学" in school:
        m 1eua "长沙市师大思沁高级中学，岳麓区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "师大思沁和湖南师大关系很密切。"
        m 1ekbsa "你在那里一定也感受到了师大的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市金海高级中学 ==========
    elif "金海高级中学" in school:
        m 1eua "长沙市金海高级中学，望城区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "金海高级中学的校园很大，管理也很严格。"
        m 1ekbsa "你在那里一定很辛苦吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市知源中学 ==========
    elif "知源中学" in school:
        m 1eua "长沙市知源中学，长沙县。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "知源中学的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市卓华高级中学 ==========
    elif "卓华高级中学" in school:
        m 1eua "长沙市卓华高级中学，岳麓区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "卓华高级中学的校园很新，设施也很好。"
        m 1ekbsa "你在那里一定过得很充实吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市耀华中学 ==========
    elif "耀华中学" in school:
        m 1eua "长沙市耀华中学，天心区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "耀华中学的办学历史很长。"
        m 1ekbsa "你在那里一定有很多故事吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市开物中学 ==========
    elif "开物中学" in school:
        m 1eua "长沙市开物中学，长沙县。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "开物中学的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市宁乡市碧桂园学校 ==========
    elif "宁乡市碧桂园学校" in school:
        m 1eua "长沙市宁乡市碧桂园学校，宁乡市。"
        m 1hua "它是长沙的民办国际化学校。"
        m 1euc "碧桂园学校有国际课程，也有国内课程。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市康礼克雷格高级中学 ==========
    elif "康礼克雷格高级中学" in school:
        m 1eua "长沙市康礼克雷格高级中学，长沙县。"
        m 1hua "它是长沙的民办国际化学校。"
        m 1euc "康礼克雷格的国际课程很有名。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市弘益高级中学 ==========
    elif "弘益高级中学" in school:
        m 1eua "长沙市弘益高级中学，长沙县。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "弘益高级中学和湖南师大附中关系很密切。"
        m 1ekbsa "你在那里一定也感受到了附中的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市立信中学 ==========
    elif "立信中学" in school:
        m 1eua "长沙市立信中学，开福区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "立信中学和长沙市一中关系很密切。"
        m 1ekbsa "你在那里一定也感受到了一中的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市湘郡培粹实验中学 ==========
    elif "湘郡培粹实验中学" in school:
        m 1eua "长沙市湘郡培粹实验中学，天心区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "湘郡培粹和长郡中学关系很密切。"
        m 1ekbsa "你在那里一定也感受到了长郡的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市雨花区金海中学 ==========
    elif "金海中学" in school and "高级中学" not in school and "学校" not in school:
        m 1eua "长沙市雨花区金海中学，雨花区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "金海中学的校园很大，管理也很严格。"
        m 1ekbsa "你在那里一定很辛苦吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市天心区怡雅中学 ==========
    elif "怡雅中学" in school:
        m 1eua "长沙市天心区怡雅中学，天心区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "怡雅中学和雅礼中学关系很密切。"
        m 1ekbsa "你在那里一定也感受到了雅礼的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市岳麓区博才培圣学校 ==========
    elif "博才培圣学校" in school:
        m 1eua "长沙市岳麓区博才培圣学校，岳麓区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "博才培圣和师大附中关系很密切。"
        m 1ekbsa "你在那里一定也感受到了附中的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市岳麓区郡维学校 ==========
    elif "郡维学校" in school and "洋湖" not in school:
        m 1eua "长沙市岳麓区郡维学校，岳麓区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "郡维学校和长郡中学关系很密切。"
        m 1ekbsa "你在那里一定也感受到了长郡的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市望金海学校 ==========
    elif "望城区金海学校" in school:
        m 1eua "长沙市望城区金海学校，望城区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "金海学校的校园很大，管理也很严格。"
        m 1ekbsa "你在那里一定很辛苦吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市明德雨花实验中学 ==========
    elif "明德雨花实验中学" in school:
        m 1eua "长沙市明德雨花实验中学，雨花区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "明德雨花和明德中学关系很密切。"
        m 1ekbsa "你在那里一定也感受到了明德的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市雨花区同升湖学校 ==========
    elif "同升湖学校" in school:
        m 1eua "长沙市雨花区同升湖学校，雨花区。"
        m 1hua "它是长沙的民办学校。"
        m 1euc "同升湖的校园很大，有山有水，环境很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市中雅培粹学校 ==========
    elif "中雅培粹学校" in school:
        m 1eua "长沙市中雅培粹学校，雨花区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "中雅培粹和雅礼中学关系很密切。"
        m 1ekbsa "你在那里一定也感受到了雅礼的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市湘郡未来实验学校 ==========
    elif "湘郡未来实验学校" in school:
        m 1eua "长沙市湘郡未来实验学校，长沙县。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "湘郡未来和长郡中学关系很密切。"
        m 1ekbsa "你在那里一定也感受到了长郡的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市岳麓区培圣学校 ==========
    elif "培圣学校" in school and "博才" not in school:
        m 1eua "长沙市岳麓区培圣学校，岳麓区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "培圣学校和师大附中关系很密切。"
        m 1ekbsa "你在那里一定也感受到了附中的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙高新区思沁学校 ==========
    elif "思沁学校" in school:
        m 1eua "长沙高新区思沁学校，岳麓区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "思沁学校和湖南师大关系很密切。"
        m 1ekbsa "你在那里一定也感受到了师大的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市麓山外国语实验中学 ==========
    elif "麓山外国语实验中学" in school:
        m 1eua "长沙市麓山外国语实验中学，岳麓区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "麓山外国语和麓山国际关系很密切。"
        m 1ekbsa "你在那里一定也感受到了麓山的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市雨花区雅境中学 ==========
    elif "雅境中学" in school:
        m 1eua "长沙市雨花区雅境中学，雨花区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "雅境中学和雅礼中学关系很密切。"
        m 1ekbsa "你在那里一定也感受到了雅礼的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市岳麓区博才实验中学 ==========
    elif "博才实验中学" in school:
        m 1eua "长沙市岳麓区博才实验中学，岳麓区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "博才实验和师大附中关系很密切。"
        m 1ekbsa "你在那里一定也感受到了附中的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市开福区青竹湖湘一外国语学校 ==========
    elif "青竹湖湘一外国语学校" in school:
        m 1eua "长沙市开福区青竹湖湘一外国语学校，开福区。"
        m 1hua "它是长沙的民办学校。"
        m 1euc "青竹湖湘一和长沙市一中关系很密切。"
        m 1ekbsa "你在那里一定也感受到了一中的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市天心区明德启南中学 ==========
    elif "明德启南中学" in school:
        m 1eua "长沙市天心区明德启南中学，天心区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "明德启南和明德中学关系很密切。"
        m 1ekbsa "你在那里一定也感受到了明德的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市岳麓区郡维学校（洋湖校区） ==========
    elif "郡维学校" in school and "洋湖" in school:
        m 1eua "长沙市岳麓区郡维学校，洋湖校区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "郡维洋湖校区和长郡中学关系很密切。"
        m 1ekbsa "你在那里一定也感受到了长郡的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市雨花区明德洞井中学 ==========
    elif "明德洞井中学" in school:
        m 1eua "长沙市雨花区明德洞井中学，雨花区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "明德洞井和明德中学关系很密切。"
        m 1ekbsa "你在那里一定也感受到了明德的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市岳麓区湘仪学校 ==========
    elif "湘仪学校" in school:
        m 1eua "长沙市岳麓区湘仪学校，岳麓区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "湘仪学校的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市岳麓区白马学校 ==========
    elif "白马学校" in school:
        m 1eua "长沙市岳麓区白马学校，岳麓区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "白马学校的校风很踏实。"
        m 1ekbsa "你在那里一定学到了很多吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市雨花区石燕湖中学 ==========
    elif "石燕湖中学" in school:
        m 1eua "长沙市雨花区石燕湖中学，雨花区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "石燕湖中学的校园很大，环境也很好。"
        m 1ekbsa "你在那里一定过得很舒服吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市天心区湘府中学 ==========
    elif "湘府中学" in school:
        m 1eua "长沙市天心区湘府中学，天心区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "湘府中学和长郡中学关系很密切。"
        m 1ekbsa "你在那里一定也感受到了长郡的底蕴吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市望城区金海学校（高中部） ==========
    elif "金海学校" in school and "高中部" in school:
        m 1eua "长沙市望城区金海学校高中部，望城区。"
        m 1hua "它是长沙的民办高中。"
        m 1euc "金海学校高中部的校园很大，管理也很严格。"
        m 1ekbsa "你在那里一定很辛苦吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市麓山国际实验学校（高中部） ==========
    elif "麓山国际实验学校" in school and "高中部" in school:
        m 1eua "长沙市麓山国际实验学校高中部，岳麓区。"
        m 1hua "它是长沙的名校。"
        m 1euc "麓山国际高中部创办于1993年，是长沙办学规模最大的市属完全中学。"
        m 1ekbsa "你在那种大校园里读书，一定有很多回忆吧。"
        m 1hua "我想听。"
        jump school_dorm_check
    # ========== 长沙市明德中学（高中部） ==========
    elif "明德中学" in school and "高中部" in school:
        m 1eua "长沙市明德中学高中部，天心区。"
        m 1hua "它是长沙的老牌名校。"
        m 1euc "明德中学创办于1903年，是湖南省首批示范性普通高中。"
        m 1ekbsa "你在那种有历史感的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲明德的事。"
        jump school_dorm_check
    # ========== 长沙市周南中学（高中部） ==========
    elif "周南中学" in school and "高中部" in school:
        m 1eua "长沙市周南中学高中部，开福区。"
        m 1hua "它是长沙的老牌名校。"
        m 1euc "周南中学由朱剑凡于1905年创办，始称周南女校。"
        m 1ekbsa "你在那种百年女校演变来的校园里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲周南的事。"
        jump school_dorm_check
    # ========== 长沙市雅礼中学（高中部） ==========
    elif "雅礼中学" in school and "高中部" in school:
        m 1eua "长沙市雅礼中学高中部，雨花区。"
        m 1hua "它是长沙四大名校之一。"
        m 1euc "雅礼创办于1906年，校训是“公勤诚朴”。"
        m 1ekbsa "你在那种百年名校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲雅礼的事。"
        jump school_dorm_check
    # ========== 长沙市第一中学（高中部） ==========
    elif "长沙市第一中学" in school and "高中部" in school:
        m 1eua "长沙市第一中学高中部，开福区。"
        m 1hua "它是长沙四大名校之一。"
        m 1euc "一中创办于1912年，校训是“公勇勤朴”。"
        m 1ekbsa "你在那种百年名校里读书，一定很有感觉吧。"
        m 1hua "我想听你讲讲一中的事。"
        jump school_dorm_check


    # ========== 没匹配到 ==========
    elif school:
        m 1eua "原来你在 [school] 啊。"
        m 1eka "虽然我不太了解，但我会记住的。"
        m 1hua "因为那是你生活的地方。"
    else:
        m 1eka "不想说也没关系。"
        m 1ekbsa "等你想告诉我的时候，我随时都在。"
        jump school_dorm_check


    label school_dorm_check:   
        m 1eua "好的，那么[player]，你是走读还是住宿？"
    menu:
        "走读":
            m 1hua "走读啊，每天都能回家，应该很舒服吧。"
            m 1euc "不过每天来回跑，一定也很辛苦。"
            m 1ekbsa "你要注意安全，别太累了。"
        "住宿":
            m 1eua "住宿啊，那你要学会照顾自己。"
            m 1euc "宿舍里人多，有时候会不太方便。"
            m 1ekbsa "但也能认识很多朋友，挺好的。"
            m 1hua "不管怎样，记得我一直在等你。"
        "有时候走读，有时候住宿":
            m 1eua "哦，那你是半走读半住宿？"
            m 1hua "这样也好，两边都能体验。"
            m 1ekbsa "但你要记得，不管在哪，我都会在这里等你。"
            

    return       