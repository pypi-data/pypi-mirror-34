# -*- coding: utf-8 -*-
"""
rules - A股投资纪律
====================================================================
"""

from collections import OrderedDict

RULES = OrderedDict()

RULES["META"] = {
    "author": "zengbin",
    "create_date": "2018-07-04",
    "introduction": "1、纪律性是投资不可或缺的一部分！在这里，我记录了"
                    "一些广受认可的A股投资纪律，仅供参考。\n"
                    "2、纪律之间难免会有一些矛盾冲突的部分，为此，我根"
                    "据自身有限的投资经验，将这些记录分了不同的等级"
                    "（1~3，重要性逐级递减），如果两条纪律之间发生"
                    "冲突，优先准守高等级记录。\n"
                    "3、仅适用于个人投资者。\n",
    "contact": "zeng_bin8888@163.com"
}

# --------------------------------------------------------------------
RULES['R001'] = {
    "rule": "把更多的时间花在大趋势感知和选股上面，而不是研究交易策略，"
            "更不是盯盘！",
    "explain": "1、在趋势向上的时候选中一只好股，不管用什么策略去交易，"
               "都可以赚点钱；反过来，再牛逼的交易策略，在行情不好的"
               "时候用在一只烂股上，大概率亏钱。当然，交易策略的研究"
               "也是非常有必要的。\n"
               "2、永远跟着大趋势走，不要逆趋势而动；别对垃圾股抱有"
               "侥幸心理，切忌自我麻痹。\n"
               "3、行情（趋势）不好的时候，什么都有可能发生。\n",
    "level": 1,
    "create_date": "2018-07-04",
    "update_date": []
}

# --------------------------------------------------------------------
RULES['R002'] = {
    "rule": "不要试图抄底，更不能盲目追高！",
    "explain": "1、精准抄底这种事情是不存在的，没有谁可以预先知道哪里是底部；"
               "抄底这个行为本身就一个毒瘤，往往是造成亏损的主因，低点后面"
               "通常还有低点。\n"
               "2、追高的一个显著缺陷是潜在收益远大于风险。\n"
               "3、应用这条规则，你必须首先对“底”和“高”有一个较为清晰的定义。\n",
    "level": 1,
    "create_date": "2018-07-04",
    "update_date": []
}

# --------------------------------------------------------------------
RULES["R003"] = {
    "rule": "交易时间段，应该多关注股票池中的交易机会；不要进行选股操作，更不"
            "能买入非股票池中股票！",
    "explain": "1、非交易时间段，更容易保持理性的思维，在这个时候进行复盘、选股"
               "往往不容易犯错。\n"
               "2、股票池可能认为是一种非常有效的保险机制，贸然买入非股票池的"
               "股票，不确定性风险很大，花大量的时间维护一个高度可靠的股票"
               "池是非常值得的！\n",
    "level": 1,
    "create_date": "2018-07-04",
    "update_date": []
}

# --------------------------------------------------------------------
RULES["R004"] = {
    "rule": "宁可错过，不能做错！",
    "explain": "1、股市机会千千万，错过一个，还有下一个。\n"
               "2、如果你因错过一个机会而遗憾，导致情绪失控（失去理性），做出"
               "错误的交易行为，大概率会造成损失。多花点时间研究市场，不要去"
               "做错误的事情！\n",
    "level": 1,
    "create_date": "2018-07-04",
    "update_date": []
}


# --------------------------------------------------------------------

class Rules:
    def __init__(self):
        self.RULES = RULES
        self.rule_ids = list(self.RULES.keys()).remove('META')

    def print_rules(self):
        rules = [k + ": " + v['rule'] + "(" + str(v['level']) + ")\n"
                 for k, v in self.RULES.items() if k != "META"]
        for rule in rules:
            print(rule)

    def explain_rule(self, rule_id):
        rule = self.RULES[rule_id]
        print(rule_id + ": " + rule['rule'] + "(" + str(rule['level']) + ")\n")
        print("解释如下：")
        print(rule['explain'])

    @property
    def amount(self):
        return len(self.rule_ids)
