label part1:
   "他的眼神中的善意和同情打动了我，看来五郎真的很担心我。"
   "他的眼神中的善意和同情打动了我，看来五郎真的很担心我。"
   "这一瞬间， 我放开了三郎的衣袖。"
   "在这几乎空荡的前厅，四郎注视着所有人的神情，把我细微的举动收入眼中，轻轻皱眉，不知道想着什么。"
   "我最在乎谁的感受？"
menu:
    "三郎":
        $ three_l += 10 
        jump part1_1
    "四郎":
        $ four_l += 10
        jump part1_1
    "五郎":
        $ five_l += 10
        jump part1_1
label part1_1:
    mc2 "姐姐我福大命大，没死，只是现在再不吃饭的话，一定离死不远了。"
    five "（放开手，走向厨房）哦，稍等片刻，我把厨房的烧鸡给你带过来。"
    four "（递给我一杯茶）萧姑娘这几天去哪里了？令堂与五弟甚是担心。"
    mc2 "（接过茶杯）你三哥请我喝茶去了。山上的路可不好走，有豺狼虎豹，又有山贼。"
    five"（端出美酒与佳肴）那岂不是很危险？"
    mc2 "姐姐我可是京都的大姐大，谁敢欺负我啊。 就是被路上的小白猫抓了几下。"
    three "（心不在焉）七郎可在？既然他不想见到我， 我还是先离开吧。"
    mc2 "别走，你在山上这么“照顾”我， 你的情谊我怎么还呀。"
    mc2 "（小声）你要是走了，我怎么和我父母说清楚呢？你说我是遇见了一只白猫还是白虎呀？"
    three "（轻笑）我只见过市井无赖，可是还没见过像姑娘这样猖狂的无赖。你就不怕你们的酒楼被我拆了？"
    mc2 "你才不会呢，小白虎是守卫西凉的神兽，而我在路上遇到的小白猫是一个送我回家的小甜心哈哈。"
    mc2 "（递给他一个抹布）小七平时都在打扫客房，你去二楼，帮帮他吧。"
    three "（食指遮住双唇）既然你这么相信我，我就暂时留下。"
    three "（接着抹布，眼睛转了转）我先上楼看看。"
    "此时，表叔刚刚从昏迷中苏醒，奈何眼前的三郎，在表叔眼里就像是阴间的鬼差。"
    "当三郎和表叔对视时，表叔又被吓晕过去了。"
    "以我看来，三郎和小七的关系不太好，我应该询问谁好呢？"
    menu:
        "四郎":
            $ four_l += 5
            mc2 "三郎和小七之间有什么矛盾吗？"
            four "萧姑娘好像很在乎我三哥？"
            mc2 "问问不行吗？"
            four "（微微一笑）你看起来很疲惫，今天好好休息，明日我再告诉你吧。"
            mc2 "明天我就忘了呀。"
            four "那就后天再说吧。(指着客房)令尊令堂好像醒了，快去看看他们吧。"
            "四郎好像不太喜欢聊八卦这类的东西，看来我是问错人了。"
            jump part1_2
        "五郎":
            $ five_l += 5
            five "（点点头，一脸八卦）哇，何止矛盾啊，那简直是三天三夜说不完—"
            four " (手肘轻垂五郎的手臂）先让萧姑娘好好休息吧。"
            five "对，对。你先好好休息，要是晚上睡不着，我可以给你做宵夜。"
            mc2 "我要是三更半夜突然饿了呢？"
            five "就算是三更半夜， 我也会起来的。"
            mc2 "怎么对我这么好？（敲了敲他的脑袋）是不是在想心术不正的东西？"
            five "天地良心，我可是一片冰心在玉壶。姐姐你刚刚逢凶化吉，我心疼还来不及，怎么会有歹念？"
            mc2 "我怎么知道你怎么想的？哦，你是不是一贯喜欢用美食讨女孩子欢心啊？"
            five "当然不是，我还是第一次特地给女孩子做饭。"
            mc2 "胡说八道，我们店里女顾客的食物不是你做的？"
            five "当然不一样啦，给顾客做饭是我店里的义务，给可爱的女孩子做饭是我自己的决定。"
            jump part1_2
label part1_2:
    "三言两语后，我向爹娘解释了我为何在山上呆了两三天。"
    "我先是胡乱编了一个故事，陈述这离奇的遭遇。"
    mom "你说你一个女孩子在山上遇险，这两三天竟没有被豺狼虎豹吞噬，而且皮肤看起来还白里透红的，这是怎么回事啊。"
    mc2 "（振振有词）山上有一个蒙着面的高人说什么我是文曲星下凡，日日夜夜与我谈心，他说我只要经历九九八十一难就能成仙啦。"
    mc2 "他此次下凡就为了保护我的，可惜第三天的时候，三郎在山上与我相遇时，那位神仙就不翼而飞了。"
    mom "这怎么听起来有点耳熟呢？"
    z "可不是嘛，这不就是西游记和七侠五义吗？"
    mc2 "（咳了一声）有那么简单就好了，这事可没完呢，这仙君还问了我一些很玄奥的问题呢"
    mom "什么问题啊？"
    mc2 "（绞尽脑汁，想起来说书的一个段子）何水无鱼? 何山无石? 何树无枝? 何子无父? 何女无夫? 何城无市？"
    mom "这听起来的确有些深奥，你们觉得答案是什么啊。"
    "三郎嘴角轻扬，不知道是已经知道了答案还是被我娘的反应逗笑了。"
    "五郎的眼神飘向了我，眼睛眨了眨，似乎想到了什么好玩的事。"
    "四郎看起来很宁静，不过倒是对我的那个题目有些感兴趣。我最期待谁的答案？"
    menu:
        "三郎":
            "（小声）本尊曾经听过这个段子。比起答案，你说谎却不脸红的样子更有趣"
            "（坐下） 五弟，你平时不是鬼点子最多了吗？何不说说？逗大家开心？"
            jump part1_3
       # "四郎":

       # "五郎":
label part1_3:
    "done"
        

show black
"测试版到此结束，您是否想查看游戏的更多更新？"
menu:
    "是":
        "请在脸书，推特，ig关注我们。FB:@mayflowerstudiogames, Twitter: @MayflowerDev, Ig:@mayflowerstudiogames "
        "一定要填这份更新通知哦。  https://forms.gle/QN7ZmudcyJaZvn2h8 "

image creditscroll:
    Text([
"{b}Designed and Built By:{/b} \nMayflower Studio Games \n \n \n"
"\n{b}English Translation:{/b} \nEllie Lau and Mayflower Studio Games \n"
"\n{b}Script written by:{/b} \nMayflower Studio Games \n "
"\n{b}XinQiJi Poem Translation by: {/b} \n许渊冲 \n "
"\n{b}Music:{/b} \n许诗茵 \n麥振鴻 \nAdrian Von Ziegler \n宫西希 \n汪睿 \n秦时明月歌曲 \n聂薇 \n曾经艺也 \n大话西游三大唐东 \n变奏的梦想 \nきずな \n"
"\n{b}Drama:{/b} \nThe Untamed \nThe Return of Condor Heroes \nNoble Aspirations \nThe Fairies of Liao Zhai \nThe Longest day in Chang'an \nAshes of Love \nRise of Phoenixes \nHappy Mitan \nMy Own Swordsman \nThe Magic Blade \nEternal Love \nEverybody Stand By2 \nIncisive Great Teacher \nA Weaver on the Horizon \nThe Glory of Tang Dynasty \nBattle Through the Heavens \n"
"\n{b}Audio:{/b} Royalty Free Music\n"
"\n{b}Special Thanks:{/b} \nEvelyn Chin \nEllie Lau \nThe Asian Drama Community"], outlines=[(1, "#fff", 0, 0)])
    anchor (0.5, 0.0)
    pos (0.5, 1.0)
    linear 15.0 ypos 0.0 yanchor 1.0