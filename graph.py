import os
from graphviz import Digraph

dot = Digraph(comment='Unit 8-9 最终版', format='pdf', engine='twopi')
dot.attr(dpi='300', ranksep='2.8', nodesep='1.3', overlap='false')
dot.attr('node', shape='box', style='rounded,filled', fontname='SimHei', fontsize='9')
dot.attr('edge', color='#666666')

# ============ 中心节点 ============
dot.node('center', 'Unit 8-9\n男女和夫妇', 
         fillcolor='#FF6B6B', fontsize='18', fontcolor='white', penwidth='5',
         width='3.5', height='2.5', root='true')

# ============ 第一主分支：男女之情 ============
dot.node('love', '一、男女之情', 
         fillcolor='#66BB6A', fontsize='13', fontcolor='white', penwidth='3', width='2.8', height='1.5')
dot.edge('center', 'love', penwidth='5', color='#66BB6A')

# 关雎部分
dot.node('guanju', '《关雎》\n《诗经·周南》', fillcolor='#A5D6A7', fontsize='10', width='2.2')
dot.edge('love', 'guanju', penwidth='2.5')

dot.node('guanju1', '「窈窕淑女，君子好逑」\n窈窕：美好的样子\n逑：配偶', fillcolor='#C8E6C9', fontsize='8')
dot.node('guanju2', '「求之不得，寤寐思服」\n寤寐：醒着睡着\n辗转反侧', fillcolor='#C8E6C9', fontsize='8')
dot.node('guanju3', '「琴瑟友之，钟鼓乐之」\n友：交朋友\n乐：使她欢乐', fillcolor='#C8E6C9', fontsize='8')
dot.edge('guanju', 'guanju1', penwidth='1.5')
dot.edge('guanju', 'guanju2', penwidth='1.5')
dot.edge('guanju', 'guanju3', penwidth='1.5')

# 诗大序
dot.node('shixu', '《诗大序》\n《毛诗正义》', fillcolor='#A5D6A7', fontsize='10', width='2.2')
dot.edge('love', 'shixu', penwidth='2.5')

dot.node('shixu1', '「诗者，志之所之也」\n在心为志\n发言为诗', fillcolor='#C8E6C9', fontsize='8')
dot.node('shixu2', '「情动于中而形于言」\n情：感情\n形：表现出来', fillcolor='#C8E6C9', fontsize='8')
dot.node('shixu3', '「不知手之舞之\n足之蹈之也」\n情感到达极致', fillcolor='#C8E6C9', fontsize='8')
dot.edge('shixu', 'shixu1', penwidth='1.5')
dot.edge('shixu', 'shixu2', penwidth='1.5')
dot.edge('shixu', 'shixu3', penwidth='1.5')

# 孔子论女子
dot.node('kongzi', '孔子论女子\n《论语·阳货》', fillcolor='#A5D6A7', fontsize='10', width='2.2')
dot.edge('love', 'kongzi', penwidth='2.5')

dot.node('kongzi1', '「唯女子与小人\n为难养也」\n养：相处', fillcolor='#C8E6C9', fontsize='8')
dot.node('kongzi2', '「近之则不孙，远之则怨」\n孙：通"逊"恭顺\n怨：怨恨不满', fillcolor='#C8E6C9', fontsize='8')
dot.edge('kongzi', 'kongzi1', penwidth='1.5')
dot.edge('kongzi', 'kongzi2', penwidth='1.5')

# 相思诗词
dot.node('poems', '相思诗词\n唐宋名作', fillcolor='#A5D6A7', fontsize='10', width='2.2')
dot.edge('love', 'poems', penwidth='2.5')

dot.node('poems1', '崔护《题都城南庄》\n「人面桃花相映红」\n「桃花依旧笑春风」', fillcolor='#C8E6C9', fontsize='8')
dot.node('poems2', '欧阳修《生查子·元夕》\n「月上柳梢头\n人约黄昏后」', fillcolor='#C8E6C9', fontsize='8')
dot.node('poems3', '「今年元夜时\n月与灯依旧\n不见去年人\n泪湿春衫袖」', fillcolor='#C8E6C9', fontsize='8')
dot.edge('poems', 'poems1', penwidth='1.5')
dot.edge('poems', 'poems2', penwidth='1.5')
dot.edge('poems', 'poems3', penwidth='1.5')

# 思凡
dot.node('sifan', '《思凡》\n《孽海记》', fillcolor='#A5D6A7', fontsize='10', width='2.2')
dot.edge('love', 'sifan', penwidth='2.5')

dot.node('sifan1', '「小尼姑年方二八」\n年方：年纪正好\n二八：十六岁', fillcolor='#C8E6C9', fontsize='8')
dot.node('sifan2', '「他与咱，咱共他\n两下里多牵挂」\n咱：我', fillcolor='#C8E6C9', fontsize='8')
dot.node('sifan3', '「火烧眉毛，且顾眼下」\n形容事情紧迫\n先顾当前', fillcolor='#C8E6C9', fontsize='8')
dot.edge('sifan', 'sifan1', penwidth='1.5')
dot.edge('sifan', 'sifan2', penwidth='1.5')
dot.edge('sifan', 'sifan3', penwidth='1.5')

# ============ 第二主分支：婚姻制度 ============
dot.node('marriage', '二、婚姻制度', 
         fillcolor='#EF5350', fontsize='13', fontcolor='white', penwidth='3', width='2.8', height='1.5')
dot.edge('center', 'marriage', penwidth='5', color='#EF5350')

# 三纲
dot.node('sangang', '三纲\n《白虎通义》', fillcolor='#EF9A9A', fontsize='10', width='2.2')
dot.edge('marriage', 'sangang', penwidth='2.5')

dot.node('sangang1', '「君为臣纲」\n君主是臣子的纲纪', fillcolor='#FFCDD2', fontsize='8')
dot.node('sangang2', '「父为子纲」\n父亲是儿子的纲纪', fillcolor='#FFCDD2', fontsize='8')
dot.node('sangang3', '「夫为妻纲」\n丈夫是妻子的纲纪', fillcolor='#FFCDD2', fontsize='8')
dot.edge('sangang', 'sangang1', penwidth='1.5')
dot.edge('sangang', 'sangang2', penwidth='1.5')
dot.edge('sangang', 'sangang3', penwidth='1.5')

# 七去三不去
dot.node('qiqu', '七去三不去\n《大戴礼记·本命》', fillcolor='#EF9A9A', fontsize='10', width='2.2')
dot.edge('marriage', 'qiqu', penwidth='2.5')

dot.node('qiqu1', '七去：\n不顺父母、无子、淫\n妒、有恶疾、多言、盗窃', fillcolor='#FFCDD2', fontsize='8')
dot.node('qiqu2', '「不顺父母去，为其逆德也」\n逆：违反', fillcolor='#FFCDD2', fontsize='8')
dot.node('qiqu3', '三不去：\n有所取无所归\n与更三年丧\n前贫贱后富贵', fillcolor='#FFCDD2', fontsize='8')
dot.node('qiqu4', '更：经历\n三年丧：为父母守孝', fillcolor='#FFCDD2', fontsize='8')
dot.edge('qiqu', 'qiqu1', penwidth='1.5')
dot.edge('qiqu', 'qiqu2', penwidth='1.5')
dot.edge('qiqu', 'qiqu3', penwidth='1.5')
dot.edge('qiqu', 'qiqu4', penwidth='1.5')

# 齐人一妻一妾
dot.node('qiren', '齐人有一妻一妾\n《孟子·离娄下》', fillcolor='#EF9A9A', fontsize='10', width='2.2')
dot.edge('marriage', 'qiren', penwidth='2.5')

dot.node('qiren1', '「餍酒肉而后反」\n餍：吃饱\n反：返回', fillcolor='#FFCDD2', fontsize='8')
dot.node('qiren2', '「卒之东郭墦间，之祭者\n乞其余」\n卒：最后\n墦：坟墓', fillcolor='#FFCDD2', fontsize='8')
dot.node('qiren3', '「与其妾讪其良人\n而相泣于中庭」\n讪：讥骂', fillcolor='#FFCDD2', fontsize='8')
dot.node('qiren4', '讽刺追求富贵利达之人', fillcolor='#FFCDD2', fontsize='8')
dot.edge('qiren', 'qiren1', penwidth='1.5')
dot.edge('qiren', 'qiren2', penwidth='1.5')
dot.edge('qiren', 'qiren3', penwidth='1.5')
dot.edge('qiren', 'qiren4', penwidth='1.5')

# ============ 第三主分支：夫妻故事 ============
dot.node('stories', '三、夫妻故事', 
         fillcolor='#FFCA28', fontsize='13', fontcolor='white', penwidth='3', width='2.8', height='1.5')
dot.edge('center', 'stories', penwidth='5', color='#FFCA28')

# 朱买臣传
dot.node('zhu', '朱买臣传\n《汉书》班固', fillcolor='#FFE082', fontsize='10', width='2.2')
dot.edge('stories', 'zhu', penwidth='2.5')

dot.node('zhu1', '「家贫，好读书，不治产业」\n治：管理\n艾薪樵：砍柴', fillcolor='#FFF9C4', fontsize='8')
dot.node('zhu2', '「担束薪，行且诵书」\n且：一边\n手不释卷', fillcolor='#FFF9C4', fontsize='8')
dot.node('zhu3', '妻子求去：\n「如公等，终饿死沟中耳」\n等：这样的人', fillcolor='#FFF9C4', fontsize='8')
dot.node('zhu4', '朱买臣：\n「我年五十当富贵」\n发迹：发达得意', fillcolor='#FFF9C4', fontsize='8')
dot.node('zhu5', '拜为会稽太守\n「富贵不归故乡\n如衣绣夜行」', fillcolor='#FFF9C4', fontsize='8')
dot.node('zhu6', '覆水难收：\n「若泼水可复收\n则汝亦可复合」', fillcolor='#FFF9C4', fontsize='8')
dot.edge('zhu', 'zhu1', penwidth='1.5')
dot.edge('zhu', 'zhu2', penwidth='1.5')
dot.edge('zhu', 'zhu3', penwidth='1.5')
dot.edge('zhu', 'zhu4', penwidth='1.5')
dot.edge('zhu', 'zhu5', penwidth='1.5')
dot.edge('zhu', 'zhu6', penwidth='1.5')

# 冯梦龙版本
dot.node('fengmenglong', '冯梦龙《喻世明言》\n(1574-1646)', fillcolor='#FFE082', fontsize='10', width='2.2')
dot.edge('stories', 'fengmenglong', penwidth='2.5')

dot.node('feng1', '有眼不识泰山\n泰山：比喻德高望重之人', fillcolor='#FFF9C4', fontsize='8')
dot.node('feng2', '海水不可斗量\n斗：量器\n不可貌相', fillcolor='#FFF9C4', fontsize='8')
dot.node('feng3', '「世上少甚挑柴担的汉子\n懊悔甚么来？」\n甚：什么', fillcolor='#FFF9C4', fontsize='8')
dot.edge('fengmenglong', 'feng1', penwidth='1.5')
dot.edge('fengmenglong', 'feng2', penwidth='1.5')
dot.edge('fengmenglong', 'feng3', penwidth='1.5')

# 苏轼《江城子》
dot.node('sushi', '苏轼《江城子》\n(1037-1101)\n悼亡妻王弗', fillcolor='#FFE082', fontsize='10', width='2.2')
dot.edge('stories', 'sushi', penwidth='2.5')

dot.node('sushi1', '「十年生死两茫茫\n不思量，自难忘」\n思量：惦记', fillcolor='#FFF9C4', fontsize='8')
dot.node('sushi2', '「千里孤坟，无处话凄凉」\n妻葬于眉州\n凄凉：孤寂悲伤', fillcolor='#FFF9C4', fontsize='8')
dot.node('sushi3', '「纵使相逢应不识\n尘满面，鬓如霜」\n鬓：耳边的头发', fillcolor='#FFF9C4', fontsize='8')
dot.node('sushi4', '「夜来幽梦忽还乡\n小轩窗，正梳妆」\n幽梦：隐约的梦', fillcolor='#FFF9C4', fontsize='8')
dot.node('sushi5', '「相顾无言，惟有泪千行」\n相顾：互相看\n行：排', fillcolor='#FFF9C4', fontsize='8')
dot.node('sushi6', '「料得年年肠断处\n明月夜，短松岗」\n肠断：极度悲伤', fillcolor='#FFF9C4', fontsize='8')
dot.edge('sushi', 'sushi1', penwidth='1.5')
dot.edge('sushi', 'sushi2', penwidth='1.5')
dot.edge('sushi', 'sushi3', penwidth='1.5')
dot.edge('sushi', 'sushi4', penwidth='1.5')
dot.edge('sushi', 'sushi5', penwidth='1.5')
dot.edge('sushi', 'sushi6', penwidth='1.5')

# 李清照《声声慢》
dot.node('liqingzhao', '李清照《声声慢》\n(1084-1155)\n南渡后作', fillcolor='#FFE082', fontsize='10', width='2.2')
dot.edge('stories', 'liqingzhao', penwidth='2.5')

dot.node('liqz1', '「寻寻觅觅\n冷冷清清\n凄凄惨惨戚戚」\n叠词的运用', fillcolor='#FFF9C4', fontsize='8')
dot.node('liqz2', '「乍暖还寒时候\n最难将息」\n将息：休息调养', fillcolor='#FFF9C4', fontsize='8')
dot.node('liqz3', '「三杯两盏淡酒\n怎敌他、晚来风急？」\n敌：抵挡', fillcolor='#FFF9C4', fontsize='8')
dot.node('liqz4', '「雁过也，正伤心\n却是旧时相识」\n却是：竟然是', fillcolor='#FFF9C4', fontsize='8')
dot.node('liqz5', '「满地黄花堆积\n憔悴损，如今有谁堪摘？」\n堪：能够', fillcolor='#FFF9C4', fontsize='8')
dot.node('liqz6', '「这次第，怎一个愁字了得！」\n次第：情形\n了得：结束', fillcolor='#FFF9C4', fontsize='8')
dot.edge('liqingzhao', 'liqz1', penwidth='1.5')
dot.edge('liqingzhao', 'liqz2', penwidth='1.5')
dot.edge('liqingzhao', 'liqz3', penwidth='1.5')
dot.edge('liqingzhao', 'liqz4', penwidth='1.5')
dot.edge('liqingzhao', 'liqz5', penwidth='1.5')
dot.edge('liqingzhao', 'liqz6', penwidth='1.5')

# ============ 第四主分支：思考 ============
dot.node('thinking', '四、思考', 
         fillcolor='#AB47BC', fontsize='13', fontcolor='white', penwidth='3', width='2.8', height='1.5')
dot.edge('center', 'thinking', penwidth='5', color='#AB47BC')

# 对比思考
dot.node('compare', '对比思考', fillcolor='#CE93D8', fontsize='10', width='2.2')
dot.edge('thinking', 'compare', penwidth='2.5')

dot.node('comp1', 'Unit 8 男女之情：\n浪漫、追求、自由\n主动性、真挚情感', fillcolor='#E1BEE7', fontsize='8')
dot.node('comp2', 'Unit 9 夫妇关系：\n制度、规范、约束\n被动性、现实压力', fillcolor='#E1BEE7', fontsize='8')
dot.node('comp3', '情感转变：\n纯真美好→悲苦哀愁\n个人意愿→社会规范', fillcolor='#E1BEE7', fontsize='8')
dot.edge('compare', 'comp1', penwidth='1.5')
dot.edge('compare', 'comp2', penwidth='1.5')
dot.edge('compare', 'comp3', penwidth='1.5')

# 性别与权力
dot.node('critical', '性别与权力', fillcolor='#CE93D8', fontsize='10', width='2.2')
dot.edge('thinking', 'critical', penwidth='2.5')

dot.node('crit1', '三纲五常的本质：\n等级制度\n男尊女卑', fillcolor='#E1BEE7', fontsize='8')
dot.node('crit2', '女性角色转变：\n被追求的主体\n→被约束的客体', fillcolor='#E1BEE7', fontsize='8')
dot.node('crit3', '七去三不去：\n单方面决定权\n女性无话语权', fillcolor='#E1BEE7', fontsize='8')
dot.node('crit4', '朱买臣故事的反思：\n妻子离开是否合理？\n"覆水难收"的傲慢', fillcolor='#E1BEE7', fontsize='8')
dot.edge('critical', 'crit1', penwidth='1.5')
dot.edge('critical', 'crit2', penwidth='1.5')
dot.edge('critical', 'crit3', penwidth='1.5')
dot.edge('critical', 'crit4', penwidth='1.5')

# 现代价值
dot.node('modern', '现代价值', fillcolor='#CE93D8', fontsize='10', width='2.2')
dot.edge('thinking', 'modern', penwidth='2.5')

dot.node('mod1', '平等尊重：\n夫妻双方地位平等\n相互尊重', fillcolor='#E1BEE7', fontsize='8')
dot.node('mod2', '自由选择：\n婚姻自主\n离婚自由', fillcolor='#E1BEE7', fontsize='8')
dot.node('mod3', '个体尊严：\n独立人格\n不依附于他人', fillcolor='#E1BEE7', fontsize='8')
dot.node('mod4', '情感本位：\n以爱情为基础\n而非制度约束', fillcolor='#E1BEE7', fontsize='8')
dot.edge('modern', 'mod1', penwidth='1.5')
dot.edge('modern', 'mod2', penwidth='1.5')
dot.edge('modern', 'mod3', penwidth='1.5')
dot.edge('modern', 'mod4', penwidth='1.5')

# ============ 第五主分支：文言文知识 ============
dot.node('language', '五、文言文知识', 
         fillcolor='#29B6F6', fontsize='13', fontcolor='white', penwidth='3', width='2.8', height='1.5')
dot.edge('center', 'language', penwidth='5', color='#29B6F6')

# 重点实词
dot.node('vocab', '重点实词', fillcolor='#81D4FA', fontsize='10', width='2.2')
dot.edge('language', 'vocab', penwidth='2.5')

dot.node('vocab1', '窈窕：美好的样子\n逑：配偶\n餍：吃饱', fillcolor='#B3E5FC', fontsize='8')
dot.node('vocab2', '寤寐：睡醒睡着\n辗转：转动\n反侧：翻来覆去', fillcolor='#B3E5FC', fontsize='8')
dot.node('vocab3', '负戴：背着\n乞：乞讨\n施从：走迂回的路跟随', fillcolor='#B3E5FC', fontsize='8')
dot.node('vocab4', '餍：吃饱\n讪：讥骂\n卒：最后', fillcolor='#B3E5FC', fontsize='8')
dot.edge('vocab', 'vocab1', penwidth='1.5')
dot.edge('vocab', 'vocab2', penwidth='1.5')
dot.edge('vocab', 'vocab3', penwidth='1.5')
dot.edge('vocab', 'vocab4', penwidth='1.5')

# 语法现象
dot.node('grammar', '语法现象', fillcolor='#81D4FA', fontsize='10', width='2.2')
dot.edge('language', 'grammar', penwidth='2.5')

dot.node('gram1', '使动用法：\n安之：使…安心\n信之：使…信任\n怀之：使…得到关怀', fillcolor='#B3E5FC', fontsize='8')
dot.node('gram2', '宾语前置：\n不吾知：不知道我\n何如：如何', fillcolor='#B3E5FC', fontsize='8')
dot.node('gram3', '通假字：\n女通"汝"：你\n知通"智"：智慧\n孙通"逊"：恭顺', fillcolor='#B3E5FC', fontsize='8')
dot.node('gram4', '判断句：\n「君为臣纲」\n「诗者，志之所之也」', fillcolor='#B3E5FC', fontsize='8')
dot.edge('grammar', 'gram1', penwidth='1.5')
dot.edge('grammar', 'gram2', penwidth='1.5')
dot.edge('grammar', 'gram3', penwidth='1.5')
dot.edge('grammar', 'gram4', penwidth='1.5')

# 成语典故
dot.node('idioms', '成语典故', fillcolor='#81D4FA', fontsize='10', width='2.2')
dot.edge('language', 'idioms', penwidth='2.5')

dot.node('idiom1', '有眼不识泰山：\n有眼睛却不认识\n德高望重的人', fillcolor='#B3E5FC', fontsize='8')
dot.node('idiom2', '手不释卷：\n手里不放下书本\n形容勤奋好学', fillcolor='#B3E5FC', fontsize='8')
dot.node('idiom3', '覆水难收：\n泼出去的水难以收回\n比喻事情无法挽回', fillcolor='#B3E5FC', fontsize='8')
dot.node('idiom4', '海水不可斗量：\n不能用斗来量海水\n比喻不可貌相', fillcolor='#B3E5FC', fontsize='8')
dot.node('idiom5', '火烧眉毛：\n形容事情非常紧急\n迫在眉睫', fillcolor='#B3E5FC', fontsize='8')
dot.edge('idioms', 'idiom1', penwidth='1.5')
dot.edge('idioms', 'idiom2', penwidth='1.5')
dot.edge('idioms', 'idiom3', penwidth='1.5')
dot.edge('idioms', 'idiom4', penwidth='1.5')
dot.edge('idioms', 'idiom5', penwidth='1.5')

# 文学常识
dot.node('literature', '文学常识', fillcolor='#81D4FA', fontsize='10', width='2.2')
dot.edge('language', 'literature', penwidth='2.5')

dot.node('lit1', '《诗经》：\n中国最早诗歌总集\n风、雅、颂三部分', fillcolor='#B3E5FC', fontsize='8')
dot.node('lit2', '苏轼(1037-1101)：\n字子瞻，号东坡居士\n北宋文学家、书画家', fillcolor='#B3E5FC', fontsize='8')
dot.node('lit3', '李清照(1084-1155)：\n号易安居士\n婉约派代表词人', fillcolor='#B3E5FC', fontsize='8')
dot.node('lit4', '冯梦龙(1574-1646)：\n明代文学家\n编纂"三言"', fillcolor='#B3E5FC', fontsize='8')
dot.edge('literature', 'lit1', penwidth='1.5')
dot.edge('literature', 'lit2', penwidth='1.5')
dot.edge('literature', 'lit3', penwidth='1.5')
dot.edge('literature', 'lit4', penwidth='1.5')
