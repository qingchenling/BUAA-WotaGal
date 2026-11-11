# 路线系统：选线、最终选择、结局
#
# W11 开场选线 → W11-W16 个人线 → W17 最终选择 → W18-W20 结局卷
#
# 结局条件：
#   林若 HE：技艺值 ≥75 且完成「共同编舞」
#   叶子 HE：叶子好感 ≥60 且完成「记录与回应」
#   宋柯 HE：圈内知名度 ≥120 且完成「灯光同步试验」
#   BE 在任何情况下都可选。

# ============================================================
# 选线
# ============================================================
label route_gate:
    if week != ROUTE_SPLIT_WEEK or route is not None:
        return

    scene black
    p "下学期要上的企划，得先决定跟谁一起把它做出来。"

    menu:
        "跟林若一起，把那套旧编排重新打下来。":
            $ set_route("rin")

        "跟着叶子，把这一路都记下来。":
            $ set_route("yoko")

        "去找宋柯，试试把光和影对上。":
            $ set_route("songke")

    call route_announce
    return


label route_announce:
    if route == "rin":
        p "你给林若发了条消息。她回得很快，只有三个字：好，来练。"
    elif route == "yoko":
        p "你问叶子要不要一起。她说她得先确认一下电脑还有多少空间。"
    elif route == "songke":
        p "你在群聊里找到宋柯。她的头像还是那根旧电棒，没换过。"
    return


# ============================================================
# 最终选择（W17）
# ============================================================
label final_gate:
    if week != FINAL_CHOICE_WEEK or final_choice is not None:
        return

    $ he_ok = he_available()
    $ req_text = he_requirement_text()

    p "要做最后决定了。"
    if he_ok:
        p "（HE 条件：[req_text]。已满足。）"
    else:
        p "（HE 条件：[req_text]。还没满足，那个选项不会出现。）"

    if route == "rin":
        menu:
            "让不同水平的人都能进到这个节目里。" if he_ok:
                $ final_choice = "he"
            "保留原案，不把没成型的高难段强行搬上台。":
                $ final_choice = "be"

    elif route == "yoko":
        menu:
            "支持她把线下春航祭办起来。" if he_ok:
                $ final_choice = "he"
            "接受场地和现实条件，不把活动做成一团乱账。":
                $ final_choice = "be"

    elif route == "songke":
        menu:
            "把那场公开的边界试演办出来。" if he_ok:
                $ final_choice = "he"
            "接受联合企划延期，先做内部预演。":
                $ final_choice = "be"

    return


# ============================================================
# 路线关键事件（占位）
# ============================================================
# 这三段只是把旗标接上，让流程可以走通。
# 正式剧本接上后，删掉这里的占位，改由 w16_{route} 的剧情设置旗标。
label route_event_check:
    if route is None:
        return
    if week == 16:
        call route_event_w16 from _call_route_event_w16
    return


label route_event_w16:
    if route == "rin":
        p "你和林若把那套旧编排拆成了三个难度档，最难的那段留给她自己。"
        p "她犹豫了很久，最后说：可以，但我要留一段是我一个人的。"
        $ flag_co_choreo = True
        $ add_affection("rin", 20)

    elif route == "yoko":
        p "叶子把这一学期的素材剪成了一条片子，放给你看。"
        p "片尾停在一段没有光的画面上，她说这是她的回信。"
        $ flag_record_reply = True
        $ add_affection("yoko", 20)

    elif route == "songke":
        p "宋柯把灯光和光弧对了一遍，第一次没有人在旁边喊「不对」。"
        p "她说这只是内部测试，别高兴太早。"
        $ flag_light_sync = True
        $ add_fame_club(40)

    return


# ============================================================
# 结局卷 W18-W20
# ============================================================
label ending_rin_he:
    scene black
    p "正式演出那天，光弧在黑暗里划开一道口子。"
    p "台上有熟练的，也有刚学会怎么握棒的。慢半拍的地方，林若没有回头去补。"
    p "她在最亮的那一段留了自己的 solo，然后把光交给身后的人。"
    p "散场以后，她在后台说了一句话，声音很轻。"
    p "「这次不是替谁打的。」"
    jump game_end


label ending_rin_be:
    scene black
    p "那套旧编排最后没有上台。"
    p "你们把它从头到尾录了一遍，一次没错，也一次没有观众。"
    p "林若看完录像，很久没说话，最后说：留着吧，明年。"
    p "没有谁失败。只是这一次，它还没长好。"
    jump game_end


label ending_yoko_he:
    scene black
    p "春航祭的摊位摆在操场边上，不是舞台，也没有灯。"
    p "叶子把投影仪架在纸箱上。片子放到一半，风把幕布吹歪了。"
    p "她跑过去扶，回来的时候笑得很大声。"
    p "后来她说：「我不需要会打。我在的地方，也是社团。」"
    jump game_end


label ending_yoko_be:
    scene black
    p "活动没办成。场地批文卡在最后一关。"
    p "叶子把三个月的东西归档：素材、名单、报销单，还有一个叫「下一届」的文件夹。"
    p "她合上电脑说：那就明年。"
    p "你忽然觉得，她比谁都适合做这件事。"
    jump game_end


label ending_songke_he:
    scene black
    p "公开试演那天，第一排坐着几个最会挑刺的人。"
    p "灯光压下去的时候光弧起来，光弧落下的时候掌声起来。"
    p "宋柯站在侧幕，没有上台。"
    p "散场后她说：「这次没有人被点名，只有一套可以继续改的说明。」"
    jump game_end


label ending_songke_be:
    scene black
    p "联合企划延期了。"
    p "你们在空场地里做了一次内部预演，来的人不到十个。"
    p "宋柯把那份纪要发到群里，没有点任何人的名字。"
    p "她说：争论没有答案，但可以留一个能改的地方。"
    jump game_end


label ending_none:
    scene black
    p "学期结束了。你把这一学期收进一个文件夹。"
    p "有些事没做完，有些人没走近。"
    p "但社团还在。"
    jump game_end
