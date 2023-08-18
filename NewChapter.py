def create_html_with_chapter(chapter_number, chapter_content, html_filename):
  try:
    html_content = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
<title>Zenith Zombie MTL</title>
<link rel='stylesheet' href="../styles.css">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <div id="navbar-placeholder"></div>
  <div class="chapter-container">
    <h1>Chapter {chapter_number}</h1>
    <div class ="chapter" id="chapter">{chapter_content}</div>
    <div class="navigation">
      <button class="nav-button" onclick="prevChapter()">Previous Chapter</button>
      <button class="nav-button" onclick="nextChapter()">Next Chapter</button>
    </div>
  </div>
  <script type="text/javascript" src="../navbar.js"></script>
  <script type="text/javascript" src="../spacing.js"></script>
  <script>
    function nextChapter() {{
        window.location.href = `VWPWE-{chapter_number+1}.html`;
    }}
    function prevChapter() {{
        window.location.href = `VWPWE-{chapter_number-1}.html`;
    }}
  </script>
</body>
</html>'''

    with open(html_filename, 'w') as html_file:
      html_file.write(html_content)

    print(f'HTML file "{html_filename}" has been successfully created.')
  except Exception as e:
    print(f'An error occurred: {e}')

if __name__ == "__main__":
  chapter_number = 994
  chapter_content = '''Qin San disregarded Tang Yishan's anger, but he didn't expect Lin Le's hidden weapon talent to be so high. Lin Le's technique of releasing ten needles in a counter-flashing pattern was impressive. After the needles collided in pairs, three final rebounds hit the target's backyard. It was impossible to predict the needles' trajectory in such a short time. Tang Gaofeng was defeated immediately as he stepped forward. His eyes were also hit by Lin Le's homemade hand grenade-style anti-wolf spray. This kid was simply dominating with his concealed weapons, even without the use of the Eight Trigrams. He could probably make it to the top three.

Qin San also felt proud of Zhang Zhengxiong's talents. Especially his "power." His Four Symbols Manifestation was oppressive, and based on what his son-in-law (Ye Cang) said, he had coincidentally comprehended his "power" and the "domain of correctness." Except for Lin Le, a few super geniuses, and the exceptional son-in-law, it seemed there were no opponents left. The son-in-law was an exception. This was true variability. Qin San might even lose. Although he hadn't truly tried, he had a premonition that his son-in-law's strength was much more than that of his peers. The old man had always thought this kid's strength only surpassed his peers by a little. A bitter smile appeared on his face.

Qin San watched as Ye Cang defeated each opponent with a single blow. Apart from Zhong Yunxiao, whom he tormented repeatedly, the others were dispatched quickly. Ye Cang's mystifying stab was undoubtedly confusing for those who didn't understand its intricacies. But for those who understood, they could see that this stab was difficult to evade. For his opponents, the speed of this attack predicted their actions' blocks. Everything was deciphered by his eyes, his actions appearing to be delayed but were actually anticipated before the opponent's actions, making it appear as if he reacted faster than he should have.

"I remember he mentioned that his superpower allows him to see the trajectory of an opponent's attack a second or two in advance," Thorny Rose's words made Qin San even more sure. After a few encounters with him, Qin San felt his Eight Trigrams was being targeted.

When Ye Cang was fully concentrated, he could perceive the trajectory of his opponent's movements five seconds in advance. This was also one of the reasons he survived numerous perilous missions.

Cold Moon yawned, and Red Moon smiled, "According to Miss Cold Moon, when facing them..."

"Kill them with a single strike..."

Zhao Xiangyu stood aside, feeling a bit embarrassed. Though it sounded exaggerated, she knew Cold Moon was serious. She had seen her master's guidance. His blade was so fast that her eyes couldn't keep up, and it was icy even from a distance. Especially when he swung his blade, his lifeless eyes made it feel as if she had seen herself beheaded. This had kept her awake all night, and during a conversation, she had even asked Cold Moon if he was the most formidable here. Cold Moon shook her head, "Don't underestimate the people here. Take Huang Zhong, for instance. He's probably the most accomplished martial artist here. No one can surpass him."

Cold Moon also heard from Ye Cang that Huang Zhong was the strongest in the room. No one here could match him in solo combat, of course.

Zhao Xiangyu remembered the two moves that Uncle Huang had taught her and felt a bit strange. If it weren't for his white beard and eyebrows, he would look like a young man in his twenties like herself. However, he had the air of an old man, which didn't feel out of place at all. Although it seemed odd, his instructions were always incisive.

Moreover, his advice was very useful, and she gained many insights. He kept saying things like, "This stance is good for an ambush. Stand here, and if I'm in that thicket, your head and flanks would have been separated long ago. This spot is suitable for ambush, and that one is good for an ambush ambush. Dig a pit here, and you can ambush passersby. It's a must-pass route. Stand there, use long-range weapons to shoot, and so on." She felt like he was all about ambushes. He even taught a few tactics for forced ambushes and suicidal ambushes (a trap masked as an opportunity, actually being a lethal attack, like a retreat tactic; for example, a sudden counterattack, feigning panic, catching the opponent off guard, and then launching an extremely fast and precise attack). Also, if the opponent was good at close range, pretend to get close to them, make yourself seem reckless, then use hidden weapons to deal with them. Conversely, if the opponent was good at long range, pretend to distance yourself from them, but in reality, launch a surprise attack.

Zhao Xiangyu thought of the craft she was learning. Master Liu taught her to weave plant fibers, and Uncle Nei would teach her other sewing and tailoring skills. She was deeply moved; finally, there was proper teaching. Also, Master Liu's advice on tactical retreats, though it felt a bit inappropriate, was genuinely effective. She once managed to escape a difficult situation from Uncle Lele's hands and received praise.

"Brother Ye, take this!" Sun Yingying, the standout of the Sun family, immediately employed the third level of the Tyrant's Strategy, surging with internal force and accompanied by a strong gust, as she launched a powerful attack. Ye Cang still managed to deter her with a single finger. The intense attack ceased abruptly, and then, he followed with a left stab to the face. She lost consciousness and was defeated.

"What's this move? So impressive! This is what I want to learn... I must ask my master to teach me this move!" Zhao Xiangyu muttered to herself. She also recalled the first time she saw him by the lake, the Transformation Spirit Snake Sword technique she had exerted with all her might. Amidst countless illusions, his casual finger strike had directly hit the tip of her sword, rendering her sword unable to advance even slightly.

Qin Zhong thought silently. This move concealed an understanding of force and fulcrums. It was an innate talent. If he was willing, he could destroy the opponent's attack's fulcrum and balance point. Although his son-in-law's skills sometimes appeared disorganized, they were all within his control. This stabbing fist revealed his cleanest attack method. There was nothing but pureness—straight-line distance, maximum speed, and the shortest time to attack the opponent. This simple punch was his lethal move!

Ye Cang's gaze shifted and saw a middle school girl from the Dragon group blink her eyes. Huh!? Ye Wushuang? She acted as if she was putting in her utmost effort, defeating her opponent with a force that seemed unbelievable. Apart from the Dragon Lady, she was among the top three strongest members of the Dragon group. This girl is terrifyingly talented and very intelligent. Of course, her weakness is laziness and being broke. Fortunately, she wasn't a squanderer.  She was in the next city. Last year, in the neighboring city, we had set off to get some money. But upon seeing her, wow, both Lele and Ah Xiong had become miserable. This girl, hesitating for a long time, looked at the instant noodle cups in the trash can. I silently left. and when she saw it, she might decide who would win the match, who knows who would end up worse.

Ye Wushuang had noticed Ye Cang long ago. At this moment, seeing him looking, she gestured with a rude hand sign. Ye Cang nodded in understanding, returning a filthy gesture. Their hand signals were lightning-fast, only the two of them paid any attention...'''
  html_filename = f"VirtualWorldPeerlessWhiteEmperor/VWPWE-{chapter_number}.html"
  create_html_with_chapter(chapter_number, chapter_content, html_filename)