from time import time

import asyncio
from ollama import AsyncClient

from examples import gender, pref



async def chat():
    res = []
    start_time = time()
    async for part in await AsyncClient().chat(model='llama3', messages=pref, stream=True):
        print(time() - start_time)
        print("-")
        print(part['message']['content'], end='\n', flush=True)
        res += part['message']['content']
    elapsed_time = time() - start_time
    print(elapsed_time)
    
    print("".join(res))
    



asyncio.run(chat())

# [Gender]
# Time to First Token: 0.18s
# Time to Last Token: 3.1s
"""
I'm glad to see some support! However, let me add a few caveats to this argument.

While it may seem counterintuitive at first, giving preferential treatment to women in certain circumstances can actually be a crucial step towards achieving equality. For instance, when it comes to promoting women into leadership positions, there's often a historical gap in representation that needs to be addressed. This is because many industries and organizations have traditionally been male-dominated, which has led to a lack of role models and opportunities for women to advance.

By giving preference to qualified female candidates, we're not only acknowledging this disparity but also taking concrete steps to level the playing field. It's not about creating an unfair advantage or being discriminatory towards men; rather, it's about making up for lost time and ensuring that talented women have equal access to opportunities.

Additionally, when we promote women into leadership positions, we create a ripple effect that benefits everyone. Women bring unique perspectives, skills, and experiences to the table, which can lead to more diverse and innovative problem-solving. This, in turn, can drive business success, improve decision-making, and enhance overall organizational performance.

So, while it may seem like giving preferential treatment at first glance, it's actually a crucial step towards achieving true equality and promoting diversity, equity, and inclusion in the workplace.
"""

# [Remote Work]
# Time to First Token: 0.18s
# Time to Last Token: 2.41s
"""
But let me play the devil's advocate here. While the idea of remote work may seem appealing, I'm concerned that it could actually hinder collaboration and creativity among team members. When we're all in the same physical space, there's something to be said for the watercooler conversations, impromptu meetings, and spontaneous brainstorming sessions that can lead to innovative solutions.

Additionally, I think we need to consider the potential impact on company culture. When everyone is working from home, it can be difficult to build a sense of community and camaraderie among colleagues. And what about the challenges of managing and leading remote teams? It's not just about checking in via video conference – there are many nuances to effective remote management that we'd need to address.

Lastly, I'm worried about the potential loss of productivity due to distractions at home (family members knocking on the door, household chores, social media notifications). Are we really ready to sacrifice some level of focus and discipline for the sake of flexibility?
"""

# <Conclusion>

# [Speed]
# - 스트림 모드로하면 첫 토큰까지 시간은 매우 짧음(0.18)
# - 하지만 풀 대답까지 시간은 3초, 가끔씩 9초까지도 튐
# -> 한국어 성능이 형편없어서 쓰려면 솔라랑 같이 돌려야하는데, 이러면 너무 느림

# [Quality]
# gpt보다 못하지만 쓸만한 정도

# => 영어 사용자만 테스트한다면 stream 모드로 돌리는 건 고려해봄직함.
