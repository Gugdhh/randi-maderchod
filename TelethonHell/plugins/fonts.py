from TelethonHell.plugins import *

normal_str = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
one = "đ đ â­ đ đ đ đ â â đ đ đ đ đ đ đ đ â đ đ đ đ đ đ đ â¨"
two = "đŦ đ­ đŽ đ¯ đ° đą đ˛ đŗ đ´ đĩ đļ đˇ đ¸ đš đē đģ đŧ đŊ đž đŋ đ đ đ đ đ đ"
three = "đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ  đĄ đĸ đŖ đ¤ đĨ đĻ đ§ đ¨ đŠ"
four = "đ đĩ đ đ đ¸ đš đĸ đģ đŧ đĨ đĻ đŋ đ đŠ đĒ đĢ đŦ đ đŽ đ¯ đ° đą đ˛ đŗ đ´ đĩ"
five = "đ¸ đš â đģ đŧ đŊ đž â đ đ đ đ đ â đ â â â đ đ đ đ đ đ đ â¤"
six = "īŧĄ īŧĸ īŧŖ īŧ¤ īŧĨ īŧĻ īŧ§ īŧ¨ īŧŠ īŧĒ īŧĢ īŧŦ īŧ­ īŧŽ īŧ¯ īŧ° īŧą īŧ˛ īŧŗ īŧ´ īŧĩ īŧļ īŧˇ īŧ¸ īŧš īŧē"
seven = "ęĒ áĨ áĨ´ áĻ ęĢ á ģ á§ ęĢ ę ¸ ę š á ęĒļ ęĒ ęĒ ęĒŽ Ī ęĒ áĨ áĻ ęĒģ ęĒ ęĒ á­ áĨ ęĒ Æē"
eight = "á´ Ę á´ á´ á´ ę° Éĸ Ę ÉĒ á´ á´ Ę á´ É´ á´ á´ Q Ę ęą á´ á´ á´  á´Ą x Ę á´ĸ"
nine = "Z â X M Î âŠ âĨ S á´ Î Ô O N W ËĨ â Åŋ I H â â˛ Æ áĄ Æ á  â"
ten = "đ° đą đ˛ đŗ đ´ đĩ đļ đˇ đ¸ đš đē đģ đŧ đŊ đž đŋ đ đ đ đ đ đ đ đ đ đ"
eleven = "âļ âˇ â¸ âš âē âģ âŧ âŊ âž âŋ â â â â â â â â â â â â â â â â"
twelve = "ā¸ āš Ī āš Ņ ÅĻ īģŽ Ņ āš × Đē É­ āš ā¸  āš ×§ áģŖ Đŗ ā¸Ŗ Õ ā¸ĸ ×Š ā¸Ŧ × ×Ĩ Õš"
thirteen = "Į ÉŽ Æ É É Ę Éĸ ÉĻ É¨ Ę Ķ Ę Ę Õŧ Ö Ö ÕĻ Ę Ö Čļ Ę Ę ÕĄ Ķŧ Ę Ę"
fourteen = "á á° á á´ á áĻ áļ á áĨ á  áĻ á áˇ á á§ áŽ á¤ á á á áŦ á á á áŠ á"
fifteen = "Ä áĒ Æ É É Ę É  É§ Äą Ę Æ Æ Éą Å ÆĄ â ÕĻ āŊ Ę ÉŦ Åŗ Ûˇ áŋŗ Ōŗ á§ Ę"
sixteen = "ā¸ āš Âĸ āģ Ä f āē h i ā¸§ k l āš āē āģ p āš r Å t ā¸ ā¸ āē x ā¸¯ āē"
seventeen = "đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ đ"
eighteen = "đ đ đ đ đ đ đ đ đ đ đ đ đ  đĄ đĸ đŖ đ¤ đĨ đĻ đ§ đ¨ đŠ đĒ đĢ đŦ đ­"
nineteen = "Îą Đ˛ Âĸ â Ņ Æ g ĐŊ Îš ×  Đē â Đŧ Îˇ Ī Ī q Ņ Ņ Ņ Ī ÎŊ Ī Ī Ņ z"
twenty = "Ã Ã Ã Ã Ã ÂŖ G H Ã J K L M Ãą Ã Ãž Q R Â§ â  Ã V W Ã ÂĨ Z"
twentyone = "âŗ ā¸ŋ âĩ Ä É âŖ â˛ âą§ Å J â­ âą  âĨ âĻ Ã âą Q âą¤ â´ âŽ É V âŠ Ķž É âąĢ"
twentytwo = "å äš å áĒ äš å áļ å ä¸¨ īž Ō ãĨ įĒ å  ã åŠ É å°ē ä¸ ã ãŠ á¯ åąą äš ã äš"
twentythree = "īž äš á ã äš īŊˇ ã  ã īž īž ãē īž īžļ å ãŽ īŊą ã å°ē ä¸ īŊ˛ ã˛ â W īž īž äš"
twentyfour = "Ä áĒ Æ É É Ę É  É§ Äą Ę Æ Æ Éą Å ÆĄ â ÕĻ āŊ Ę ÉŦ Åŗ Ûˇ áŋŗ Ōŗ á§ Ę"

@hell_cmd(pattern="font(?:\s|$)([\s\S]*)")
async def font(event):
    hell = await eor(event, "Changing font...")
    flag = event.text[6:]
    rply = await event.get_reply_message()
    if not rply:
        return await eod(hell, "Nothing given to change!")
    old = rply.text
    normie = normal_str.split(" ")
    prev = " ".join(old).upper()
    if not flag.isnumeric():
        return await eod(hell, "Give font numbers only!")
    match int(flag):
        case 1:
            to_ = one.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 2:
            to_ = two.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 3:
            to_ = three.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 4:
            to_ = four.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 5:
            to_ = five.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 6:
            to_ = six.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 7:
            to_ = seven.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 8:
            to_ = eight.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 9:
            to_ = nine.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 10:
            to_ = ten.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 11:
            to_ = eleven.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 12:
            to_ = twelve.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 13:
            to_ = thirteen.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 14:
            to_ = fourteen.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 15:
            to_ = fifteen.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 16:
            to_ = sixteen.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 17:
            to_ = seventeen.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 18:
            to_ = eighteen.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 19:
            to_ = nineteen.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 20:
            to_ = twenty.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 21:
            to_ = twentyone.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 22:
            to_ = twentytwo.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 23:
            to_ = twentythree.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case 24:
            to_ = twentyfour.split(" ")
            for normal in prev:
                if normal in normie:
                    new = to_[normie.index(normal)]
                    prev = prev.replace(normal, new)
            await hell.edit(prev)
        case _:
            await eod(hell, "Unsupported font!")


CmdHelp("fonts").add_command(
    "font", "<font number>", "Changes the replied text to desired font.", "font 07"
).add_extra(
    "đ Font Numbers", "01 to 23"
).add_info(
    "Font Changer."
).add_warning(
    "â Harmless Module"
).add()
