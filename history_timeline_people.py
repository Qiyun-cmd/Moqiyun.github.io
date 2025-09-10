from manim import *
from dataclasses import dataclass
from typing import List, Tuple
import textwrap
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *

# =========================
# 可调参数（全局外观与时长）
# =========================
CJK_FONT = "Noto Sans CJK SC"  # 若无该字体，请改为系统中文字体（如 "Source Han Sans SC"、"Microsoft YaHei"）
TITLE_FONT = CJK_FONT

BG_COLOR = "#0B0F19"
TEXT_COLOR = "#FFFFFF"
SUB_TEXT_COLOR = "#D0D8E3"
PANEL_BG_COLOR = "#0F172A"
PANEL_STROKE_OPACITY = 0.25
PANEL_FILL_OPACITY = 0.85
DESC_FONT_SIZE = 30
TITLE_FONT_SIZE = 48
DATE_FONT_SIZE = 32

# 进场节奏
HEAD_WRITE_T = 0.9
DESC_FADE_T = 0.6
ERA_BANNER_HOLD = 2.6
TITLE_SCENE_HOLD = 3.6
CLOSING_HOLD = 4.0

# 全局每项停留时长（含进/出场）
EVENT_TOTAL_HOLD = 10.0

# 按时代覆写时长（未填的用全局）
HOLD_BY_ERA = {
    "当代文明": 8.0,          # 当代更紧凑
    "近代文明细化": 11.0,      # 近代略长
    # "史前考古": 9.0,
    # "21 世纪科技专题": 9.5,
}
def hold_time_for_era(era: str) -> float:
    return HOLD_BY_ERA.get(era, EVENT_TOTAL_HOLD)

# “人物分批页”：把某时代里连续的【人物】合并为一页网格展示
PEOPLE_BATCH = {
    "当代文明": dict(enable=True, size=8, page_hold=9.5),   # 每页最多 8 人
    # 其他时代如需分批，也可加： "21 世纪科技专题": dict(enable=True, size=8, page_hold=9.5)
}

# 人物卡片样式
PERSON_STYLE = dict(
    dashed_bar=True,  # 人物卡左侧色带改为“虚线”
    avatar=True       # 人物卡标题前放圆形头像占位（首字/首字母）
)

# =========================
# 数据结构
# =========================
@dataclass
class EraInfo:
    key: str
    name: str
    period: str
    color: str

@dataclass
class EventItem:
    era: str
    date: str
    title: str  # 标题可带【人物】标签
    desc: str

# =========================
# 时代信息（包含主轴与独立专题）
# =========================
ERA_INFOS = {
    "史前考古": EraInfo("史前考古", "史前考古", "前 10000 年 - 前 3000 年", "#14B8A6"),
    "前古典文明延伸": EraInfo("前古典文明延伸", "前古典文明延伸", "公元前 3000 年 - 公元前 1000 年", "#F6C247"),
    "古典文明深化": EraInfo("古典文明深化", "古典文明深化", "公元前 1000 年 - 公元 500 年", "#2AA2FF"),
    "中世纪扩展": EraInfo("中世纪扩展", "中世纪扩展", "公元 500 年 - 1500 年", "#8B5CF6"),
    "近代文明细化": EraInfo("近代文明细化", "近代文明细化", "1500 年 - 1900 年", "#22C55E"),
    "现代文明拓展": EraInfo("现代文明拓展", "现代文明拓展", "1900 年 - 2000 年", "#F59E0B"),
    "当代文明": EraInfo("当代文明", "当代文明", "2000 年至今", "#EF4444"),
    "21 世纪科技专题": EraInfo("21 世纪科技专题", "21 世纪科技专题", "2000 年 - 至今（科技）", "#06B6D4"),
}

# =========================
# 主时间轴数据（含人物标签）
# =========================
EVENTS: List[EventItem] = [
    # ===== 前古典文明延伸 =====
    EventItem("前古典文明延伸", "前 3000 年", "苏美尔楔形文字",
              "苏美尔人发明楔形文字，成为两河流域行政与文学的载体，推动早期国家治理与文化传承。"),
    EventItem("前古典文明延伸", "前 2650 年", "【人物】伊姆何特普",
              "埃及建筑师与医者，主持修建阶梯金字塔，被誉为“建筑/医学之父”之一。"),
    EventItem("前古典文明延伸", "前 2600 年", "吉萨金字塔群",
              "胡夫金字塔工程展现古埃及数学、天文与工程实力，王权与宗教信仰的物质象征。"),
    EventItem("前古典文明延伸", "前 2400 年", "不列颠巨石阵",
              "关于其天文指向与礼仪功能的争议延续至今，反映对季节与天象的早期观测。"),
    EventItem("前古典文明延伸", "前 2334 年", "阿卡德帝国",
              "萨尔贡统一两河，奠定早期“帝国”范式；楔形文字成为跨区域的行政与外交工具。"),
    EventItem("前古典文明延伸", "前 2334 年", "【人物】萨尔贡一世",
              "开创中央集权的跨城邦帝国治理，影响两河流域政治格局。"),
    EventItem("前古典文明延伸", "前 2100 年", "《吉尔伽美什史诗》",
              "王权、友谊与洪水神话的史诗定型，被视为世界最早的长篇文学之一。"),
    EventItem("前古典文明延伸", "前 1792 年", "《汉谟拉比法典》",
              "以“以眼还眼”的同态原则确立秩序，系统规范社会权利与义务，对后世法律影响深远。"),
    EventItem("前古典文明延伸", "前 1792 年", "【人物】汉谟拉比",
              "主持编纂《汉谟拉比法典》，将习惯法成文化与公开化。"),
    EventItem("前古典文明延伸", "前 1500 年", "印度河流域文明",
              "印章文字未破译，城市规划标准化（街道、排水）显示高度组织化的社会形态。"),
    EventItem("前古典文明延伸", "前 1300 年", "商朝甲骨文成熟",
              "甲骨卜辞记录祭祀、战争、农业，为研究商代社会结构与信仰提供直证史料。"),
    EventItem("前古典文明延伸", "前 1200 年", "青铜时代崩溃",
              "地中海东部多个政体在数十年内衰亡，贸易链断裂、人口迁徙与铁器普及重塑文明版图。"),
    EventItem("前古典文明延伸", "前 1200 年", "奥尔梅克文明",
              "中美洲早期文明崛起，巨石头像与礼仪中心影响玛雅与阿兹特克文明。"),
    EventItem("前古典文明延伸", "前 1050 年", "腓尼基字母",
              "以少量字母表征音素，降低识字门槛，深刻影响希腊、拉丁与希伯来文字系统。"),
    EventItem("前古典文明延伸", "前 1046 年", "西周建立与礼乐秩序",
              "“天命”观念与分封制确立，礼乐文明成为政治合法性与社会秩序的重要基石。"),

    # ===== 古典文明深化 =====
    EventItem("古典文明深化", "前 800 年 - 前 500 年", "荷马史诗与希腊精神",
              "《伊利亚特》《奥德赛》构筑英雄原型与伦理观，奠定西方文学与价值源头。"),
    EventItem("古典文明深化", "前 776 年", "奥林匹克祭典",
              "城邦以竞技代替流血，奥林匹亚祭典成为泛希腊认同与和平竞逐象征。"),
    EventItem("古典文明深化", "前 600 年", "波斯帝国与行省制",
              "行省制、统一货币与文化宽容促进欧亚非的大规模交融，丝绸之路西段雏形出现。"),
    EventItem("古典文明深化", "前 6 世纪", "【人物】老子",
              "道家代表，“道法自然、无为而治”，影响东亚政治与哲学传统。"),
    EventItem("古典文明深化", "前 5 世纪", "【人物】释迦牟尼",
              "创立佛教，以“四谛”“中道”影响南亚与东亚宗教伦理。"),
    EventItem("古典文明深化", "前 551 年 - 前 479 年", "孔子与百家争鸣",
              "“仁、礼”体系化，诸子百家兴起，塑造东亚伦理与政治哲学。"),
    EventItem("古典文明深化", "前 551 年", "【人物】孔子",
              "以仁义礼智重构社会伦理，教育普及理念奠定学术传统。"),
    EventItem("古典文明深化", "前 490 年 - 前 479 年", "希波战争",
              "希腊城邦抵抗波斯扩张，保卫城邦自治并催生雅典民主与海上同盟。"),
    EventItem("古典文明深化", "前 470 年", "【人物】苏格拉底",
              "“产婆术”启发式提问，强调德性即知识，奠定西方哲学方法。"),
    EventItem("古典文明深化", "前 509 年", "罗马共和国与法治传统",
              "元老院、执政官、公民大会的政治架构；《十二铜表法》与公民权奠定法治基石。"),
    EventItem("古典文明深化", "前 427 年", "【人物】柏拉图",
              "理念论与学院传统奠定形而上学基座，政治哲学影响深远。"),
    EventItem("古典文明深化", "前 384 年", "【人物】亚里士多德",
              "系统化逻辑、伦理、政治与自然学；奠定科学分类与演绎方法。"),
    EventItem("古典文明深化", "前 334 年", "【人物】亚历山大大帝",
              "横跨欧亚非的征服促进“希腊化时代”文化交流与学术传播。"),
    EventItem("古典文明深化", "前 323 年", "希腊化时代与亚历山大城",
              "亚历山大城成学术中心，图书馆达 70 万卷，欧几里得、阿基米德成果传播。"),
    EventItem("古典文明深化", "前 300 年", "【人物】欧几里得",
              "《几何原本》公理化传统奠基，影响数学与科学方法两千年。"),
    EventItem("古典文明深化", "前 287 年", "【人物】阿基米德",
              "杠杆原理、浮力定律与几何方法，数学与工程学双料先驱。"),
    EventItem("古典文明深化", "前 260 年", "【人物】阿育王",
              "以法治与慈悲治理，推动佛教与石刻法诏传播，巩固南亚版图。"),
    EventItem("古典文明深化", "前 221 年", "秦始皇统一",
              "书同文、车同轨、度量衡统一，官僚体制与大一统范式确立。"),
    EventItem("古典文明深化", "前 221 年", "【人物】秦始皇",
              "中央集权与制度整合的实践者，奠定中国国家治理框架。"),
    EventItem("古典文明深化", "前 138 年", "张骞通西域与丝绸之路",
              "中原与中亚、地中海贸易网络相连，丝绸、玻璃、香料与思想交换。"),
    EventItem("古典文明深化", "前 138 年", "【人物】张骞",
              "两度出使西域，打通东西通道，拓展对世界地理与文明的认知。"),
    EventItem("古典文明深化", "公元 1 世纪", "【人物】耶稣",
              "以博爱、救赎与天国福音启发信仰传统，影响两千年文明史。"),
    EventItem("古典文明深化", "公元 1 世纪", "基督教的兴起",
              "4 世纪成为国教，深刻影响西方伦理、艺术与政治格局。"),
    EventItem("古典文明深化", "公元 105 年", "蔡伦改进造纸术",
              "用树皮麻头降本，纸张取代竹简与帛书，知识传播显著加速。"),
    EventItem("古典文明深化", "公元 105 年", "【人物】蔡伦",
              "改进造纸术，让书写材料平价化，奠定知识普及的物质基础。"),
    EventItem("古典文明深化", "公元 313 年", "《米兰赦令》",
              "承认宗教宽容，基督教在帝国内合法。"),
    EventItem("古典文明深化", "公元 313 年", "【人物】君士坦丁大帝",
              "君权与宗教关系奠基者，迁都君士坦丁堡，连接古典与中世纪。"),
    EventItem("古典文明深化", "公元 395 年", "罗马帝国分裂",
              "帝国分为东西两部；拜占庭保存希腊罗马遗产，连接古典与中世纪。"),
    EventItem("古典文明深化", "公元 476 年", "西罗马帝国灭亡",
              "西欧进入封建化与地方化中世纪，古典秩序让位于地域政权。"),

    # ===== 中世纪扩展 =====
    EventItem("中世纪扩展", "公元 581 年", "隋：大运河与科举滥觞",
              "短暂统一但制度影响深远，大运河串联南北，选官机制为唐宋奠基。"),
    EventItem("中世纪扩展", "公元 618 年 - 907 年", "唐：世界都会与丝路盛景",
              "长安为多元文化汇聚中心，律令与对外交流塑造“开放帝国”。"),
    EventItem("中世纪扩展", "公元 610/622 年", "【人物】穆罕默德",
              "宣示一神信仰并建社群秩序，《古兰经》奠定伊斯兰文明核心。"),
    EventItem("中世纪扩展", "公元 622 年", "伊斯兰文明与知识网络",
              "代数、医学、天文学突破与翻译运动，构建跨西班牙至印度的知识网络。"),
    EventItem("中世纪扩展", "公元 751 年", "造纸术西传",
              "怛罗斯之后，造纸术由阿拉伯人传入欧洲，助推文艺复兴与宗教改革。"),
    EventItem("中世纪扩展", "公元 800 年", "查理曼加冕",
              "加冕为“罗马人的皇帝”，拉丁基督教世界的政治秩序与文化复兴重启。"),
    EventItem("中世纪扩展", "公元 800 年", "【人物】查理曼",
              "推动教育与行政改革，奠定中世纪西欧政治与文化基座。"),
    EventItem("中世纪扩展", "公元 868 年", "敦煌《金刚经》雕版印刷",
              "现存可确证年代最早的印刷书，标志知识复制效率飞跃。"),
    EventItem("中世纪扩展", "公元 1015 年", "【人物】伊本·海赛姆",
              "《光学书》奠定实验与光学传统，被誉为“现代科学方法”先驱。"),
    EventItem("中世纪扩展", "公元 1020 年", "【人物】伊本·西拿",
              "《医典》系统化医学与药理学，数百年为欧陆医学院教材。"),
    EventItem("中世纪扩展", "公元 1041 年", "毕昇活字印刷",
              "活字理念出现，为金属活字与现代印刷奠基。"),
    EventItem("中世纪扩展", "公元 1086 年", "【人物】沈括",
              "《梦溪笔谈》汇聚天文、地理、工程与自然观察，体现实验与记录精神。"),
    EventItem("中世纪扩展", "1096 年 - 1291 年", "十字军东征与交流",
              "虽充满暴力，但促进东西方交流，欧洲重获亚里士多德与指南针等知识。"),
    EventItem("中世纪扩展", "公元 1206 年", "蒙古帝国的汇通与征服",
              "横贯欧亚的大帝国促进商路畅通，也带来战争破坏与疾病传播。"),
    EventItem("中世纪扩展", "公元 1206 年", "【人物】成吉思汗",
              "以军政组织与后勤体系整合欧亚草原，重塑大陆交流格局。"),
    EventItem("中世纪扩展", "公元 1215 年", "《大宪章》",
              "以法律限制王权，确立“王在法下”，近代宪政思想源头。"),
    EventItem("中世纪扩展", "公元 1299 年", "【人物】马可·波罗",
              "游记拓展欧洲对东方的想象与地理认知。"),
    EventItem("中世纪扩展", "1347 年 - 1351 年", "黑死病与人文主义萌芽",
              "人口骤减动摇神权统治，公共卫生观念与医学进步、人文主义思潮兴起。"),
    EventItem("中世纪扩展", "公元 1405 年", "【人物】郑和",
              "七下西洋扩展印度洋交流圈，展现造船与航海组织能力。"),
    EventItem("中世纪扩展", "公元 1439 年", "古腾堡金属活字印刷",
              "改良金属活字与油墨，印刷术从精英化走向大众化。"),
    EventItem("中世纪扩展", "公元 1439 年", "【人物】古腾堡",
              "系统化集成印刷技术，让书籍复制成本骤降、知识传播加速。"),
    EventItem("中世纪扩展", "公元 1453 年", "拜占庭灭亡与文艺复兴前夜",
              "希腊学者携手稿入意大利，奥斯曼控制商路促进新航路开辟。"),

    # ===== 近代文明细化 =====
    EventItem("近代文明细化", "公元 1500 年", "【人物】达·芬奇",
              "艺术—科学跨界典范，《维特鲁威人》《大西洋手稿》体现工程与解剖探索。"),
    EventItem("近代文明细化", "公元 1517 年", "宗教改革的引爆",
              "路德《九十五条论纲》反对赎罪券，信仰、政治与印刷传播联动变革。"),
    EventItem("近代文明细化", "公元 1517 年", "【人物】马丁·路德",
              "以“因信称义”挑战教权，推动信仰自由与良心权利。"),
    EventItem("近代文明细化", "公元 1543 年", "哥白尼与日心说",
              "《天体运行论》挑战地心说与神学权威，开启科学革命。"),
    EventItem("近代文明细化", "公元 1543 年", "【人物】哥白尼",
              "用数学与观测重置宇宙模型的坐标。"),
    EventItem("近代文明细化", "1564 年 - 1642 年", "伽利略与实验科学",
              "望远镜观测与科学方法普及，奠定实验科学范式。"),
    EventItem("近代文明细化", "公元 1600 年", "英国东印度公司",
              "特许商业帝国，开辟全球贸易网络，形塑公司—帝国的殖民模式。"),
    EventItem("近代文明细化", "公元 1609 年", "【人物】开普勒",
              "行星三定律揭示天体和谐的数学结构，为牛顿奠基。"),
    EventItem("近代文明细化", "公元 1637 年", "【人物】笛卡尔",
              "方法怀疑与解析几何，确立理性与坐标化自然的现代视角。"),
    EventItem("近代文明细化", "公元 1648 年", "威斯特伐利亚和约",
              "确立“属地主权”，现代主权国家体系与国际法秩序里程碑。"),
    EventItem("近代文明细化", "公元 1687 年", "牛顿与经典力学",
              "《原理》以数学统一天地运动规律，科学取代神学成解释自然的主导。"),
    EventItem("近代文明细化", "公元 1687 年", "【人物】牛顿",
              "微积分、万有引力、光学三重奏，现代科学地基建造者之一。"),
    EventItem("近代文明细化", "公元 1689 年", "《英国权利法案》",
              "限制君权、保障议会与公民自由，明确立宪精神。"),
    EventItem("近代文明细化", "公元 1752 年", "【人物】本杰明·富兰克林",
              "避雷针与电学实验推动电学近代化，也是公共事业与外交改革者。"),
    EventItem("近代文明细化", "公元 1762 年", "【人物】卢梭",
              "《社会契约论》与公意概念，塑造现代民主与自由平等理念。"),
    EventItem("近代文明细化", "公元 1765 年", "瓦特与蒸汽机",
              "改良蒸汽机引爆工业革命，工厂制度兴起、城市化加速。"),
    EventItem("近代文明细化", "公元 1765 年", "【人物】詹姆斯·瓦特",
              "冷凝器等改良让蒸汽机高效可靠，开启能量转化新时代。"),
    EventItem("近代文明细化", "公元 1776 年", "亚当·斯密与市场秩序",
              "《国富论》提出“看不见的手”，奠定古典经济学与自由竞争理论。"),
    EventItem("近代文明细化", "公元 1776 年", "【人物】亚当·斯密",
              "以分工与市场机制解释财富增长路径，奠基政治经济学。"),
    EventItem("近代文明细化", "公元 1787 年", "美国宪法",
              "联邦制与三权分立写入根本法，成为后世宪政范式参照。"),
    EventItem("近代文明细化", "公元 1787 年", "【人物】詹姆斯·麦迪逊",
              "《联邦党人文集》作者之一，被称为“美国宪法之父”。"),
    EventItem("近代文明细化", "公元 1789 年", "《人权宣言》",
              "“人生而自由平等”，将启蒙思想转化为法律文献。"),
    EventItem("近代文明细化", "公元 1804 年", "【人物】拿破仑",
              "《拿破仑法典》推动民法体系现代化与权利平等的法律表达。"),
    EventItem("近代文明细化", "公元 1831 年", "【人物】法拉第",
              "电磁感应与电机雏形，连接科学基础与工程实践。"),
    EventItem("近代文明细化", "公元 1859 年", "达尔文与进化论",
              "《物种起源》颠覆神创论，改变生物学并影响哲学与社会学。"),
    EventItem("近代文明细化", "公元 1859 年", "【人物】达尔文",
              "自然选择解释生物多样性，促使生命观从静态到动态变革。"),
    EventItem("近代文明细化", "公元 1864 年", "【人物】路易·巴斯德",
              "细菌致病学与巴氏消毒法奠定现代微生物与公共卫生。"),
    EventItem("近代文明细化", "公元 1866 年", "【人物】孟德尔",
              "豌豆遗传实验揭示分离与独立分配定律，现代遗传学滥觞。"),
    EventItem("近代文明细化", "公元 1869 年", "门捷列夫与元素周期表",
              "以周期性规律整合化学知识，并预测未知元素。"),
    EventItem("近代文明细化", "公元 1869 年", "【人物】门捷列夫",
              "按原子量与性质排布元素并预测空位，验证科学预见力。"),
    EventItem("近代文明细化", "公元 1879 年", "白炽灯与电气时代",
              "电力照明系统点亮城市夜晚，通讯与生活方式革命性变化。"),
    EventItem("近代文明细化", "公元 1879 年", "【人物】托马斯·爱迪生",
              "发明体系与电力系统工程整合，让电气时代走向规模应用。"),
    EventItem("近代文明细化", "公元 1888 年", "【人物】尼古拉·特斯拉",
              "交流感应电机与多相电力系统，支撑长距离输电与电气化普及。"),
    EventItem("近代文明细化", "公元 1895 年", "X 射线与量子曙光",
              "X 射线与镭的发现推动量子物理与医学影像的诞生。"),
    EventItem("近代文明细化", "公元 1895 年", "【人物】伦琴",
              "发现 X 射线并率先用于成像，开启医学影像学。"),
    EventItem("近代文明细化", "公元 1898 年", "【人物】玛丽·居里",
              "发现镭与钋，放射性研究开辟现代核科学与医疗新方向。"),

    # ===== 现代文明拓展 =====
    EventItem("现代文明拓展", "公元 1900 年", "【人物】普朗克",
              "能量子化假设开启量子论，现代物理第二支柱的发端。"),
    EventItem("现代文明拓展", "公元 1903 年", "受控动力飞行",
              "莱特兄弟试飞成功，航空时代开启，交通与战争样态被改写。"),
    EventItem("现代文明拓展", "公元 1905/1915 年", "相对论与现代物理学",
              "狭义与广义相对论颠覆绝对时空观，为核能与宇宙学奠定理论支柱。"),
    EventItem("现代文明拓展", "公元 1905 年", "【人物】爱因斯坦",
              "相对论与光电效应，时空观革命与量子诠释双线发展。"),
    EventItem("现代文明拓展", "公元 1913 年", "【人物】哈伯 / 博施",
              "氨合成实现工业化，化肥规模生产支撑现代农业与人口增长。"),
    EventItem("现代文明拓展", "公元 1917 年", "十月革命与新制度实验",
              "第一个社会主义国家诞生，20 世纪两极对峙格局形成。"),
    EventItem("现代文明拓展", "公元 1928/1943 年", "青霉素与抗生素时代",
              "从发现到量产应用，极大提升人类寿命，改写传染病史。"),
    EventItem("现代文明拓展", "公元 1928 年", "【人物】弗莱明",
              "偶然发现青霉素抑菌效应，拉开抗生素时代序幕。"),
    EventItem("现代文明拓展", "公元 1929 年", "大萧条与宏观经济",
              "全球经济衰退催生凯恩斯主义与福利国家，宏观政策体系确立。"),
    EventItem("现代文明拓展", "公元 1929 年", "【人物】哈勃",
              "发现退行速度与红移关系，提出宇宙膨胀证据。"),
    EventItem("现代文明拓展", "公元 1936 年", "【人物】凯恩斯",
              "《就业、利息和货币通论》重塑经济学与政府调控理念。"),
    EventItem("现代文明拓展", "公元 1945 年", "联合国成立",
              "多边主义与国际合作的制度化平台诞生。"),
    EventItem("现代文明拓展", "公元 1946 年", "ENIAC 与信息时代开端",
              "第一台电子计算机问世，随后晶体管与集成电路推动计算机小型化与普及。"),
    EventItem("现代文明拓展", "公元 1947 年", "晶体管与电子工业革命",
              "取代电子管成为核心元件，电子设备小型化与大众化。"),
    EventItem("现代文明拓展", "公元 1947 年", "【人物】巴丁 / 布拉顿 / 肖克利",
              "发明晶体管，现代电子与计算产业的基石。"),
    EventItem("现代文明拓展", "公元 1948 年", "【人物】克劳德·香农",
              "信息熵与信道容量，通信与计算的共同语言确立。"),
    EventItem("现代文明拓展", "公元 1953 年", "【人物】沃森 / 克里克 / 富兰克林",
              "DNA 双螺旋结构阐明，分子生物学时代开启（致敬富兰克林贡献）。"),
    EventItem("现代文明拓展", "公元 1955 年", "【人物】乔纳斯·索尔克",
              "脊髓灰质炎疫苗广泛接种，公共卫生成就拯救无数儿童。"),
    EventItem("现代文明拓展", "公元 1957/1969 年", "太空时代：从卫星到登月",
              "“斯普特尼克 1 号”与“阿波罗 11 号”标记人类迈入太空时代。"),
    EventItem("现代文明拓展", "公元 1962 年", "【人物】蕾切尔·卡森",
              "《寂静的春天》激发现代环境保护运动与化学品风险治理。"),
    EventItem("现代文明拓展", "公元 1963 年", "【人物】马丁·路德·金",
              "“我有一个梦想”推动民权立法与反歧视议程。"),
    EventItem("现代文明拓展", "公元 1965 年", "【人物】诺曼·鲍洛格",
              "高产小麦育种支撑“绿色革命”，缓解多国饥荒。"),
    EventItem("现代文明拓展", "公元 1969 年", "互联网前传：ARPANET",
              "军事通信网络演化为互联网，TCP/IP 与万维网引爆信息革命。"),
    EventItem("现代文明拓展", "公元 1969 年", "【人物】尼尔·阿姆斯特朗",
              "人类首次踏足月球，拓展地—月文明半径的象征时刻。"),
    EventItem("现代文明拓展", "公元 1973 年", "【人物】袁隆平",
              "杂交水稻实现规模化增产，守护粮食安全与人类福祉。"),
    EventItem("现代文明拓展", "公元 1974 年", "【人物】文顿·瑟夫 / 鲍勃·卡恩",
              "TCP/IP 奠基，互联网的语言与互联性确立。"),
    EventItem("现代文明拓展", "公元 1979 年", "【人物】王选",
              "汉字激光照排系统，推动中文信息化与出版业现代化。"),
    EventItem("现代文明拓展", "公元 1983 年", "【人物】卡里·穆利斯",
              "PCR 技术让分子检测与基因工程迈入高速路。"),
    EventItem("现代文明拓展", "公元 1989 年", "柏林墙倒塌",
              "冷战象征坍塌，欧洲一体化与全球化加速。"),
    EventItem("现代文明拓展", "公元 1989/1991 年", "【人物】蒂姆·伯纳斯-李",
              "提出并实现万维网与超文本协议，让互联网走向大众与商业。"),
    EventItem("现代文明拓展", "公元 1990 年", "人类基因组计划",
              "进入分子层级的生命科学时代，为基因治疗与个性化医疗奠基，也引发伦理讨论。"),
    EventItem("现代文明拓展", "公元 1991 年", "【人物】林纳斯·托瓦兹",
              "开源操作系统 Linux 引领协作式软件开发与互联网基础设施。"),

    # ===== 当代文明 =====
    EventItem("当代文明", "公元 2001 年", "维基百科与开放知识",
              "协作式知识生产与开放内容运动壮大，改变知识获取与共享方式。"),
    EventItem("当代文明", "公元 2001 年", "【人物】吉米·威尔士 / 拉里·桑格",
              "共同发起维基百科，塑造开放协作与众包知识的新范式。"),
    EventItem("当代文明", "公元 2006 年", "【人物】山中伸弥",
              "iPS 细胞技术为再生医学提供新路径，重塑细胞命运观念。"),
    EventItem("当代文明", "公元 2007 年", "智能手机与移动互联网",
              "iPhone 引领智能手机普及，社交媒体与共享经济重塑社交与商业模式。"),
    EventItem("当代文明", "公元 2007 年", "【人物】史蒂夫·乔布斯",
              "多触控与应用生态整合进手机，重构个人计算与媒介形态。"),
    EventItem("当代文明", "公元 2008 年", "全球金融危机",
              "引发监管改革与量化宽松，也推动金融科技与风险治理反思。"),
    EventItem("当代文明", "公元 2012 年", "希格斯玻色子被证实",
              "大型强子对撞机实证希格斯机制，标准模型关键拼图落位。"),
    EventItem("当代文明", "公元 2012 年", "【人物】彼得·希格斯 / 弗朗索瓦·安格勒",
              "理论预言经实验确认，粒子物理标准模型完善。"),
    EventItem("当代文明", "公元 2012 年", "【人物】杜德纳 / 夏彭捷",
              "CRISPR 基因编辑奠基，精准编辑为医疗与农业开新局。"),
    EventItem("当代文明", "公元 2012 年", "【人物】Hinton / LeCun / Bengio",
              "深度学习三巨头推动神经网络复兴，打通感知任务的实用化。"),
    EventItem("当代文明", "公元 2015 年", "《巴黎协定》",
              "全球气候治理达成共识，“净零排放”和可持续转型成为共同行动目标。"),
    EventItem("当代文明", "公元 2015 年", "【人物】屠呦呦",
              "青蒿素拯救数百万疟疾患者，体现传统中草药与现代科学的结合。"),
    EventItem("当代文明", "公元 2016 年", "AlphaGo 与深度学习",
              "围棋胜利标志复杂决策突破，深度学习广泛应用并引发就业与伦理讨论。"),
    EventItem("当代文明", "公元 2016 年", "【人物】德米斯·哈萨比斯 / 大卫·西尔弗",
              "以深度强化学习实现围棋突破，推动通用决策智能研究。"),
    EventItem("当代文明", "公元 2020 年", "新冠疫情与 mRNA 疫苗",
              "大流行推动生物技术应急能力与线上社会实践，也暴露全球公共卫生短板。"),
    EventItem("当代文明", "公元 2020 年", "【人物】卡里科 / 魏斯曼",
              "mRNA 疫苗技术成熟落地，验证核酸药物的广泛潜力。"),
    EventItem("当代文明", "公元 2021 年", "GPT-3.5 与生成式 AI",
              "具备强大的文本生成与复杂问答能力，推动智能写作、客服等应用变革。"),
    EventItem("当代文明", "公元 2022 年", "NFT 与数字艺术市场",
              "区块链赋能确权与交易，数字艺术获得稀缺性与可交易性。"),
    EventItem("当代文明", "公元 2022 年", "【人物】Beeple",
              "数字艺术商业模式示范，引发主流艺术市场对链上确权的重估。"),
    EventItem("当代文明", "公元 2023 年", "《黑神话：悟空》与文化出海",
              "以中国神话与传统美学吸引全球玩家，验证本土文化题材国际潜力。"),
    EventItem("当代文明", "公元 2024 年", "申遗与文旅数字化",
              "北京中轴线、春节申遗成功；行动计划推动 VR/AR 等在文旅场景落地。"),
    EventItem("当代文明", "公元 2025 年", "VR 电影规范与国风百老汇",
              "VR 电影纳入管理体系并获“龙标”；《丝路之声》巡演推动文旅融合与东西方交流。"),
]

# =========================
# 独立篇章数据（史前考古 / 21 世纪科技）
# =========================
PREHISTORY_EVENTS = [
    EventItem("史前考古", "前 10000 年", "新石器革命与驯化",
              "新月沃地开始栽培谷物/驯化家畜，定居化萌芽。"),
    EventItem("史前考古", "前 9600–前 8200 年", "哥贝克力石阵",
              "目前最早的大型礼仪性遗址群，或显示“先礼仪后农业”的社会组织。"),
    EventItem("史前考古", "前 9000 年", "耶利哥古城",
              "城墙与塔楼表明公共工程与安全观念的早期形成。"),
    EventItem("史前考古", "前 7000 年", "陶器与稻作扩散",
              "中国河姆渡、贾湖等遗址的陶器与早期稻作，技术与食谱多样化。"),
    EventItem("史前考古", "前 6500–前 5700 年", "恰塔霍裕克",
              "密集聚落、壁画与家祭，展现早期都市生活形态。"),
    EventItem("史前考古", "前 5500–前 4500 年", "铜冶炼与金属工艺",
              "从自然铜到冶炼铜，器物功能与社会分工出现新层级。"),
    EventItem("史前考古", "前 4000 年", "轮子与车轴",
              "运输与生产效率革命，促进贸易网络扩大。"),
    EventItem("史前考古", "前 3300 年", "乌鲁克期城市化",
              "庙宇与行政体系发展，城邦政治崛起。"),
    EventItem("史前考古", "前 3300–前 2300 年", "良渚文明玉礼制",
              "王权象征与礼仪系统成熟，东亚复杂社会的重要标志。"),
]

TECH21_EVENTS = [
    EventItem("21 世纪科技专题", "2001 年", "人类基因组草图公布",
              "生命科学进入分子层级时代，推动精准医疗与群体遗传研究。"),
    EventItem("21 世纪科技专题", "2004 年", "【人物】埃隆·马斯克（团队）",
              "推动电动车全栈与可复用火箭商业化，影响清洁能源与航天。"),
    EventItem("21 世纪科技专题", "2008 年", "Android 与移动生态",
              "开放生态推动智能手机全球普及，应用分发生态繁荣。"),
    EventItem("21 世纪科技专题", "2012 年", "【人物】Hinton / LeCun / Bengio",
              "深度学习复兴，ImageNet 突破带来计算机视觉飞跃。"),
    EventItem("21 世纪科技专题", "2012 年", "【人物】杜德纳 / 夏彭捷",
              "CRISPR 基因编辑奠基，生命科学与农业进入“可编辑”时代。"),
    EventItem("21 世纪科技专题", "2014 年", "钙钛矿太阳能电池",
              "高效率低成本路线崛起，推动光伏技术迭代。"),
    EventItem("21 世纪科技专题", "2016 年", "AlphaGo 里程碑",
              "复杂决策智能示范，带动深度学习在产业落地。"),
    EventItem("21 世纪科技专题", "2017 年", "【人物】Vaswani 等",
              "Transformer 架构提出，“注意力机制”统一语言与多模态表示。"),
    EventItem("21 世纪科技专题", "2019 年", "【人物】Goodenough / Yoshino / Whittingham",
              "锂电三位奠基者获诺奖，电动车与储能革命的关键底座。"),
    EventItem("21 世纪科技专题", "2020 年", "mRNA 疫苗规模化",
              "快速设计与量产展示核酸药物的公共卫生潜力。"),
    EventItem("21 世纪科技专题", "2021 年", "生成式 AI（GPT-3.5）",
              "大模型驱动自然语言与多任务泛化，应用场景爆发。"),
    EventItem("21 世纪科技专题", "2022 年", "惯性约束聚变“点火”里程碑",
              "NIF 实验实现净能量增益，迈出重要一步（仍需工程化）。"),
]

# =========================
# 工具函数
# =========================
def wrap_cn(text: str, width: int = 28):
    # 对中文/无空格文本友好的换行
    return textwrap.wrap(text, width=width, break_long_words=True, break_on_hyphens=False)

def make_paragraph(text: str, width_chars: int, font_size: int, color=SUB_TEXT_COLOR):
    lines = wrap_cn(text, width=width_chars)
    mlines = [Text(line, font=CJK_FONT, font_size=font_size, color=color) for line in lines]
    group = VGroup(*mlines).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
    return group

# =========================
# 分批工具（把某时代的连续【人物】合并为网格页）
# =========================
@dataclass
class PeopleBatch:
    era: str
    people: List[EventItem]

def is_person(ev) -> bool:
    return isinstance(ev, EventItem) and ev.title.startswith("【人物】")

def build_playlist(events: List[EventItem]) -> List:
    """把指定时代的连续‘人物’合并成批量页，其余保持单条事件"""
    units = []
    i = 0
    n = len(events)
    while i < n:
        ev = events[i]
        cfg = PEOPLE_BATCH.get(ev.era, dict(enable=False))
        if cfg.get("enable") and is_person(ev):
            group = [ev]
            j = i + 1
            while j < n and events[j].era == ev.era and is_person(events[j]) and len(group) < cfg["size"]:
                group.append(events[j])
                j += 1
            units.append(PeopleBatch(era=ev.era, people=group))
            i = j
        else:
            units.append(ev)
            i += 1
    return units

def is_people_batch(x) -> bool:
    return isinstance(x, PeopleBatch)

# =========================
# 主类：人物拓展版（含分批/虚线/头像/时长调节）
# =========================
class HistoryCulturalTimelinePeople(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # 片头
        title = Text("文明流变·人物拓展版：人类历史文化动态时间轴", font=TITLE_FONT, font_size=58, color=TEXT_COLOR)
        title.set_color_by_gradient("#60A5FA", "#F472B6", "#F59E0B")
        subtitle = Text("含【人物】标签 · 分批展示 · 可调时长", font=CJK_FONT, font_size=30, color=SUB_TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(title, shift=UP, lag_ratio=0.2), FadeIn(subtitle, shift=DOWN), run_time=1.6)
        self.wait(TITLE_SCENE_HOLD)
        self.play(FadeOut(VGroup(title, subtitle), shift=UP, run_time=0.8))

        # 进度条
        progress_group, progress_tracker = self._build_progress_bar()
        progress_group.to_edge(DOWN, buff=0.35)
        self.add(progress_group)

        # 播放列表（单事件 + 人物批量页）
        units = build_playlist(EVENTS)
        total_units = len(units)

        # 底部时代刻度（基于 units）
        placeholder_events = [EventItem(u.era, "", "", "") if is_people_batch(u) else u for u in units]
        era_ticks, _ = self._build_era_ticks(progress_group, placeholder_events)
        self.add(era_ticks)

        # 播放循环
        current_era = None
        for idx, item in enumerate(units):
            item_era = item.era if is_people_batch(item) else item.era

            if item_era != current_era:
                current_era = item_era
                era_info = ERA_INFOS[current_era]
                banner = self._era_banner(era_info)
                self.play(FadeIn(banner, shift=UP, run_time=0.6))
                self.wait(ERA_BANNER_HOLD)
                self.play(FadeOut(banner, shift=UP, run_time=0.6))

            era_color = ERA_INFOS[current_era].color
            if is_people_batch(item):
                # 批量人物页
                page = self._people_batch_page(current_era, item.people, era_color)
                self.play(FadeIn(page.panel, shift=DOWN, run_time=0.45))
                self.play(FadeIn(page.title, shift=DOWN, run_time=0.4))
                self.play(LaggedStart(*[FadeIn(c, shift=UP, run_time=0.25) for c in page.grid], lag_ratio=0.06))
                self.wait(PEOPLE_BATCH[current_era]["page_hold"])
                self.play(FadeOut(page, shift=UP, run_time=0.55))
            else:
                ev = item
                card = self._event_card(ev, era_color, max_width=min(config.frame_width * 0.9, 13.0))
                card.shift(UP * 0.2)
                self.play(FadeIn(card.bg, shift=DOWN, run_time=0.45), FadeIn(card.bar, shift=DOWN, run_time=0.45))
                self.play(Write(card.date, run_time=HEAD_WRITE_T * 0.6))
                if hasattr(card, "tag_chip") and card.tag_chip is not None:
                    self.play(FadeIn(card.tag_chip, shift=RIGHT, run_time=0.4))
                if hasattr(card, "avatar") and card.avatar is not None:
                    self.play(FadeIn(card.avatar, shift=RIGHT, run_time=0.4))
                self.play(Write(card.title, run_time=HEAD_WRITE_T))
                self.play(FadeIn(card.desc, shift=DOWN, run_time=DESC_FADE_T))
                self.wait(hold_time_for_era(current_era))
                self.play(FadeOut(card, shift=UP, run_time=0.55))

            # 进度条推进
            self.play(progress_tracker.animate.set_value((idx + 1) / total_units), run_time=0.6, rate_func=smooth)

        # 片尾
        closing = VGroup(
            Text("谢谢观看", font=TITLE_FONT, font_size=58, color=TEXT_COLOR),
            Text("愿我们在历史中看见个人与时代的双向成就", font=CJK_FONT, font_size=34, color=SUB_TEXT_COLOR)
        ).arrange(DOWN, buff=0.4)
        closing.set_y(0.5)
        self.play(FadeIn(closing, shift=UP, run_time=0.8))
        self.wait(CLOSING_HOLD)
        self.play(FadeOut(closing, shift=UP, run_time=0.8))

    # 时代横幅
    def _era_banner(self, era_info: EraInfo) -> VGroup:
        width = min(config.frame_width * 0.9, 12.5)
        bg = RoundedRectangle(
            corner_radius=0.18, width=width, height=1.4,
            fill_color=era_info.color, fill_opacity=0.18,
            stroke_color=era_info.color, stroke_opacity=0.9, stroke_width=2.5
        )
        name = Text(era_info.name, font=CJK_FONT, font_size=44, color=era_info.color, weight=BOLD)
        period = Text(era_info.period, font=CJK_FONT, font_size=28, color=SUB_TEXT_COLOR)
        group = VGroup(name, period).arrange(DOWN, buff=0.12).move_to(bg.get_center())
        return VGroup(bg, group)

    # 事件/人物卡（人物=虚线柱 + 头像占位）
    def _event_card(self, ev: EventItem, era_color: str, max_width: float = 12.0) -> VGroup:
        date_txt = Text(ev.date, font=CJK_FONT, font_size=DATE_FONT_SIZE, color=TEXT_COLOR)
        tag, plain_title = self._parse_title_tag(ev.title)
        title_txt = Text(plain_title, font=TITLE_FONT, font_size=TITLE_FONT_SIZE, color=TEXT_COLOR, weight=BOLD)
        desc_group = make_paragraph(ev.desc, width_chars=28, font_size=DESC_FONT_SIZE, color=SUB_TEXT_COLOR)

        content_width = max_width - 1.2
        if desc_group.width > content_width:
            desc_group.scale_to_fit_width(content_width)

        header_dummy = VGroup(date_txt, title_txt).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        est_height = header_dummy.height + 0.35 + desc_group.height + 1.0
        bg = RoundedRectangle(
            corner_radius=0.16, width=max_width, height=max(est_height, 2.8),
            fill_color=PANEL_BG_COLOR, fill_opacity=PANEL_FILL_OPACITY,
            stroke_color=WHITE, stroke_opacity=PANEL_STROKE_OPACITY, stroke_width=2
        )

        # 左侧色带：人物=虚线；事件=实心
        if tag == "人物" and PERSON_STYLE["dashed_bar"]:
            bar = self._make_dashed_bar(bg.height, era_color, width=0.18)
            bar.move_to(bg.get_left() + RIGHT * (0.09))
        else:
            bar = Rectangle(width=0.18, height=bg.height, fill_color=era_color, fill_opacity=1.0, stroke_width=0)
            bar.move_to(bg.get_left() + RIGHT * (bar.width * 0.5))

        # 标题头部：日期 + [人物标签] + [头像] + 标题
        header_elems = [date_txt]
        tag_chip = None
        if tag:
            tag_chip = self._make_tag_chip(tag, era_color)
            header_elems.append(tag_chip)

        avatar = None
        if tag == "人物" and PERSON_STYLE["avatar"]:
            initial = self._initial_char(plain_title)
            avatar = self._make_avatar_chip(initial, era_color)
            header_elems.append(avatar)

        header_elems.append(title_txt)
        header = VGroup(*header_elems).arrange(RIGHT, buff=0.4, aligned_edge=DOWN)

        padding_x, padding_y = 0.6, 0.5
        header.next_to(bg.get_top(), DOWN, buff=padding_y).align_to(bg, LEFT).shift(RIGHT * (padding_x + 0.12))
        desc_group.next_to(header, DOWN, buff=0.35).align_to(header, LEFT)

        card = VGroup(bg, bar, header, desc_group).move_to(ORIGIN)
        card.bg, card.bar = bg, bar
        card.date, card.title, card.desc = date_txt, title_txt, desc_group
        card.tag_chip = tag_chip
        card.avatar = avatar
        return card

    # 标签解析
    def _parse_title_tag(self, text: str) -> Tuple[str, str]:
        if text.startswith("【") and "】" in text:
            idx = text.index("】")
            tag = text[1:idx]
            pure = text[idx+1:].strip()
            return tag, pure
        return None, text

    # 头像/虚线/批量页工具
    def _initial_char(self, name: str) -> str:
        if not name:
            return "?"
        c = name[0]
        return c.upper() if ("a" <= c.lower() <= "z") else c

    def _make_tag_chip(self, tag: str, color: str) -> VGroup:
        label = Text(tag, font=CJK_FONT, font_size=24, color=color, weight=BOLD)
        pad_x, pad_y = 0.18, 0.04
        box = RoundedRectangle(corner_radius=0.12, width=label.width + pad_x * 2, height=label.height + pad_y * 2,
                               stroke_color=color, stroke_width=2.2, stroke_opacity=0.95,
                               fill_color=color, fill_opacity=0.15)
        label.move_to(box.get_center())
        return VGroup(box, label)

    def _make_avatar_chip(self, initial: str, color: str) -> VGroup:
        circ = Circle(radius=0.24, stroke_color=color, stroke_width=2.5, fill_color=color, fill_opacity=0.12)
        txt = Text(initial, font=CJK_FONT, font_size=22, color=color, weight=BOLD)
        txt.move_to(circ.get_center())
        return VGroup(circ, txt)

    def _make_dashed_bar(self, height: float, color: str, width: float = 0.18, dash: float = 0.22, gap: float = 0.12):
        y = -height/2 + dash/2
        segs = VGroup()
        while y < height/2:
            h = min(dash, height/2 - y + dash/2)
            r = Rectangle(width=width, height=h, fill_color=color, fill_opacity=1.0, stroke_width=0)
            r.move_to([0, y, 0])
            segs.add(r)
            y += dash + gap
        segs.move_to(ORIGIN)
        return segs

    def _compact_person_card(self, ev: EventItem, era_color: str, max_w=3.8) -> VGroup:
        tag, name = self._parse_title_tag(ev.title)
        initial = self._initial_char(name)
        avatar = self._make_avatar_chip(initial, era_color)
        name_t = Text(name, font=CJK_FONT, font_size=26, color=TEXT_COLOR, weight=BOLD)
        summary = ev.desc.strip()
        summary = summary if len(summary) <= 28 else summary[:28] + "…"
        desc_t = Text(summary, font=CJK_FONT, font_size=22, color=SUB_TEXT_COLOR)
        col = VGroup(avatar, name_t, desc_t).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        pad = 0.28
        bg = RoundedRectangle(corner_radius=0.14, width=max_w, height=max(2.0, col.height + pad*2),
                              fill_color=PANEL_BG_COLOR, fill_opacity=PANEL_FILL_OPACITY,
                              stroke_color=WHITE, stroke_opacity=PANEL_STROKE_OPACITY, stroke_width=1.6)
        col.move_to(bg.get_center()).align_to(bg, LEFT).shift(RIGHT*0.24)
        bar = Rectangle(width=0.12, height=bg.height, fill_color=era_color, fill_opacity=1.0, stroke_width=0)
        bar.move_to(bg.get_left() + RIGHT*(bar.width*0.5))
        card = VGroup(bg, bar, col)
        card.bg, card.bar = bg, bar
        return card

    def _people_batch_page(self, era: str, people: List[EventItem], era_color: str) -> VGroup:
        title = Text(f"{era} · 人物群像", font=CJK_FONT, font_size=36, color=era_color, weight=BOLD)
        cards = [self._compact_person_card(p, era_color) for p in people]
        grid = VGroup(*cards).arrange_in_grid(rows=2, cols=4, buff=(0.4, 0.4), aligned_edge=LEFT)
        w = min(config.frame_width * 0.95, 13.5)
        h = max(4.5, grid.height + 1.4)
        panel = RoundedRectangle(corner_radius=0.18, width=w, height=h,
                                 fill_color=PANEL_BG_COLOR, fill_opacity=PANEL_FILL_OPACITY,
                                 stroke_color=WHITE, stroke_opacity=PANEL_STROKE_OPACITY, stroke_width=2)
        title.next_to(panel.get_top(), DOWN, buff=0.36).align_to(panel, LEFT).shift(RIGHT*0.5)
        grid.next_to(title, DOWN, buff=0.4).move_to([panel.get_center()[0], grid.get_center()[1]-0.2, 0])
        page = VGroup(panel, title, grid)
        page.panel, page.title, page.grid = panel, title, grid
        return page

    # 进度条与时代刻度
    def _build_progress_bar(self):
        w = min(config.frame_width * 0.75, 10.5)
        h = 0.24
        bg = RoundedRectangle(
            corner_radius=0.08, width=w, height=h,
            stroke_color=WHITE, stroke_opacity=0.4, stroke_width=1.2,
            fill_color=WHITE, fill_opacity=0.07
        )
        tracker = ValueTracker(0.0)

        def make_fill():
            ratio = tracker.get_value()
            fw = max(0.001, w * ratio)
            rect = Rectangle(width=fw, height=h * 0.64, fill_color="#38BDF8", fill_opacity=0.95, stroke_width=0)
            rect.move_to(bg.get_left() + RIGHT * (fw * 0.5))
            return rect

        fill = always_redraw(make_fill)
        label = Text("进度", font=CJK_FONT, font_size=22, color=SUB_TEXT_COLOR)
        label.next_to(bg, LEFT, buff=0.4).align_to(bg, DOWN)
        group = VGroup(bg, fill, label)
        return group, tracker

    def _build_era_ticks(self, progress_group: VGroup, events: List[EventItem]):
        bg = None
        for m in progress_group.submobjects:
            if isinstance(m, RoundedRectangle):
                bg = m
        if bg is None:
            return VGroup(), VGroup()

        total = len(events)
        left = bg.get_left()
        width = bg.width

        boundaries = []
        seen = set()
        for i, ev in enumerate(events):
            if ev.era not in seen:
                seen.add(ev.era)
                if i != 0:
                    boundaries.append(i)

        tick_group = VGroup()
        for b in boundaries:
            ratio = b / total
            x = left[0] + width * ratio
            tick = Line([x, bg.get_bottom()[1], 0], [x, bg.get_top()[1], 0],
                        stroke_color=WHITE, stroke_opacity=0.4, stroke_width=1.0)
            tick_group.add(tick)

        return tick_group, VGroup()

# =========================
# 独立篇章 Scene
# =========================
class PrehistoryArchaeologyChapter(HistoryCulturalTimelinePeople):
    def construct(self):
        global EVENTS
        EVENTS = PREHISTORY_EVENTS
        super().construct()

class Tech21CenturyChapter(HistoryCulturalTimelinePeople):
    def construct(self):
        global EVENTS
        EVENTS = TECH21_EVENTS
        PEOPLE_BATCH.setdefault("21 世纪科技专题", dict(enable=True, size=8, page_hold=9.5))
        super().construct()