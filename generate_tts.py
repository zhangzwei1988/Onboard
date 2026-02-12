"""
拍学机新手引导 - TTS音频生成脚本
使用方法：
1. pip install edge-tts
2. python generate_tts.py
3. 生成的mp3文件会放在 audio/ 文件夹
4. 把 audio/ 文件夹和 onboarding.html、bg/ 放同一目录

语音：zh-CN-XiaoyiNeural（微软小艺，偏童声，活泼可爱）
备选：zh-CN-XiaoxiaoNeural（小晓，年轻女声，情感丰富）
"""

import asyncio
import os
import edge_tts

# 语音选择 - XiaoyiNeural 最接近小孩声音
VOICE = "zh-CN-XiaoyiNeural"
# 语速稍慢一点，适合儿童听
RATE = "-10%"
# 音调稍高
PITCH = "+5Hz"

# 所有旁白文本
narrations = {
    "scene1": "亚瑟爷爷是一位博物学家。小时候，他发现了一个秘密——大自然里的每一种生物，都在悄悄说话。爷爷把这些神奇的声音叫做，「自然之语」。",
    "scene2a": "他去过会下雨的森林，听过大象的脚步声。",
    "scene2b": "他爬过冰冷的雪山，听过企鹅爸爸的呼唤。",
    "scene2c": "他还坐船出海，听过鲸鱼在水下唱歌。",
    "scene3book": "爷爷走过森林、雪山和大海，把一路上听到的声音、遇见的生物，都记录在一本特别的书里——爷爷给它取了一个名字，叫《万物之书》。爷爷一辈子的发现，都藏在这本书里。",
    "scene4": "可是，爷爷慢慢老了，走不动了。他翻开《万物之书》，发现还有好多好多空白的页。那些没来得及听到的声音，成了爷爷最大的遗憾。",
    "scene5": "亲爱的小探险家：帮爷爷把书填满吧！去听听你家门口的花、树、小虫子都在说什么？等你发现了新的声音，记得回来讲给爷爷听哦！——爱你的，亚瑟爷爷。",
    "scene6": "咕咕！你就是爷爷说的小探险家吧？我等你好久啦！我是咕咕！以后有问题都可以问我！来，我教你收集自然之语！",
    "scene7": "看到那朵花了吗？它正在说话呢！按下红色按钮，就能收集到它的声音。",
    "scene7done": "咕咕！你听到了吗！这些小星星，就是花的自然之语。收集越多，爷爷的书就越丰富哦！",
    "scene8": "爷爷的第一个任务：到外面去，拍一张照片吧！花、虫子、树叶、云朵——什么都可以！你家门口藏着什么声音呢？咕咕好期待！",
    # 场景触发引导
    "trigger1": "咕咕！拍得不错！想知道这是什么吗？按紫色按钮问我！",
    "trigger2": "对了！你也可以按住黄色按钮直接跟我说话，就像对讲机一样！",
    "trigger3": "咕咕！你已经收集了10段自然之语！爷爷的书又丰富了一点，继续加油！",
    "trigger4": "这就是爷爷的《万物之书》！你收集到的每一种生物，都会记录在这里。看，这是你发现的！点开看看？",
    "trigger5": "这里是探险任务！爷爷给你准备了一些小挑战，完成就能获得更多星星哦！",
    "trigger6": "欢迎来到魔法工坊！在这里，你可以把自然之语变成一幅画。选一张照片，试试看？",
    "trigger7": "这是你的探险背包！照片、创作、故事……你的宝贝都收在这里啦！",
    "trigger8": "咕咕咕咕！！这是你第一次听到「凤蝶」的声音！它已经被写进爷爷的书里啦！",
    "trigger9": "哇！你获得了一枚探险家徽章！这是爷爷给厉害的探险家准备的荣誉勋章。去背包里看看你的徽章吧！",
    "trigger10": "咕咕！你升级啦！你现在是Lv2好奇宝贝了！收集越多自然之语，就能听懂越多大自然的秘密哦！",
}


async def generate_all():
    os.makedirs("audio", exist_ok=True)
    
    for name, text in narrations.items():
        output = f"audio/{name}.mp3"
        print(f"🔊 生成: {output}")
        
        communicate = edge_tts.Communicate(
            text, 
            VOICE, 
            rate=RATE, 
            pitch=PITCH
        )
        await communicate.save(output)
    
    print(f"\n✅ 全部完成！共生成 {len(narrations)} 个音频文件")
    print("📁 文件位于 audio/ 目录")
    print("\n目录结构应为：")
    print("├── onboarding.html")
    print("├── bg/")
    print("│   ├── scene1.png")
    print("│   ├── scene2a.png ... ")
    print("└── audio/")
    print("    ├── scene1.mp3")
    print("    ├── scene2a.mp3 ...")


if __name__ == "__main__":
    asyncio.run(generate_all())
