
core里面主要写数据流和逻辑还有api方法
其中变量都在datastore中定义，尽量不要在其他地方定义新变量
gameflow是用来记录游戏流的
api主要是用来记录改变变量流的方法，这样后续调试时可以方便找到谁调用了这些方法

对于ui，画面，文本和图像尽量往外放，只记录变量变化


具体执行（比如调用api函数来服务故事变化之类的）放到外面写，尽量保持core稳定



基础属性
week                当前周数



fame                知名度（特指校园内的，所以学校爬台>练习的场景=视频，）



person_skill         个人技艺值



echo_unlocked       是否解锁回声据点


剧情变量
团体线
member_count        社团人数
has_recruited       是否触发线上招新
has_first_stage     是否完成首次演出



个人线
linruo_route        林若个人线


技能池 
id 方便随机数抽取
name 名字
difficulty 难度
mastery 掌握度\熟练度
charm 观赏性\魅力值


