from openai import OpenAI, AsyncOpenAI
from openai.types.beta.threads.message import Message
from openai.pagination import SyncCursorPage
from typing import Optional, List

from secrets import openai_api_key
import asyncio

from examples import gender, pref, gender_ko, pref_ko, pref_ko_point

from time import time


class DevilManager:
    def __init__(self):
        self.__client = AsyncOpenAI(api_key=openai_api_key)

    async def run_devill(self, messages):
        response = await self.__client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        choices = response.choices

        if len(choices) > 0:
            return choices[0].message.content
        else:
            return None


devil = DevilManager()


async def test():
    tmp = time()
    answer = await devil.run_devill(pref_ko)
    tmp2 = time()
    print(tmp2 - tmp)
    print(answer)

asyncio.run(test())


# [Gender]
# Elasped Time: 8.198960304260254s
"""
While many might agree that promotions should be merit-based, giving preferential treatment to women can actually be a necessary step towards redressing systemic inequalities that have persisted for decades. Historically, women have been underrepresented in leadership roles, not because of a lack of ability or ambition, but due to structural barriers such as gender bias, lack of mentorship, limited networking opportunities, and workplace cultures that favor male styles of leadership. 

Implementing preferential promotion policies for women can serve as a corrective measure, creating a more inclusive environment and ensuring diverse perspectives in decision-making processes. This can lead to more innovative solutions, better representation of customer demographics, and ultimately, improved organizational performance. Therefore, preferential treatment for women is not merely about fairness at an individual level but about fostering equity and enhancing the overall health of organizations and society.
"""

# [Preference]
# Elasped Time: 3.9s
"""
I genuinely believe that our company should not adopt remote work. Here's why:

Firstly, remote work severely hampers team cohesion and collaboration. There's a certain synergy that comes from having all team members in the same physical space, brainstorming ideas or resolving issues in real-time without the barriers of screens and time zones. Informal discussions, quick huddles, and spontaneous creativity are aspects that thrive in an office setting but are often lost in remote work environments.

Secondly, the lack of a structured work environment can lead to a significant drop in productivity and accountability. While some employees may thrive in a home setup, others may struggle with distractions, lack of proper workspace, or even the blurring of lines between home and work life. This can lead to burnout, mental health issues, and ultimately reduced output.

Finally, the sense of belonging and company culture take a hit with remote work. Building a robust company culture doesn’t just happen through virtual happy hours or Slack channels; it’s cultivated through shared experiences, face-to-face interactions, and a collective environment. Remote work isolates employees and makes them feel more like individual contractors than a cohesive team working towards a common goal.

While remote work has its advantages, including flexibility and reduced commute times, the potential long-term downsides to team coherence, productivity, and company culture cannot be ignored. Therefore, maintaining an office-based environment, even if it’s in a hybrid form, is essential for the sustained success of our company.
"""

# [Gender(korean)]
# Elapsed Time: 6.047057151794434s
"""
안녕하세요. 악마의 대변인으로서, 여성에게 인사 발령 시 특혜를 주는 것에 대한 반대되는 주장을 펼쳐보겠습니다.

먼저, 여성에 대한 특혜는 인사 발령 과정에서 성별 간 평등을 달성할 수 있는 중요한 도구일 수 있습니다. 여러 연구에 따르면, 여성은 여전히 다양한 산업과 직급에서 대표성이 낮으며, 이는 적절한 기회가 주어지지 않았기 때문에 발생하는 경우가 많습니다. 예를 들어, 양질의 기회가 제공되지 않거나, 임신과 출산으로 인한 경력 단절 등 여러 구조적인 요인들이 여성의 승진을 방해할 수 있습니다. 따라서 이러한 특혜는 현실적으로 존재하는 성 불평등을 완화하고, 궁극적으로는 성 평등한 직장 문화를 조성하는데 기여할 수 있습니다.

그리고, 인사 발령에서 여성에게 특혜를 주는 것은 구성원들의 다양성을 증진시켜 조직 전체의 혁신과 창의력을 향상시키는 효과도 있을 수 있습니다. 다양한 배경과 경험을 가진 인력이 모이면 다양한 아이디어와 관점이 교류되고, 이는 더 나은 문제 해결과 혁신적인 해결책을 도출하는 데 도움이 될 수 있습니다. 다양한 연구 결과에서도 다문화적이고 다양한 배경을 가진 인력들이 더 나은 성과를 내고 있음을 보여줍니다.

마지막으로, 일시적으로 주어지는 특혜가 결국에는 사회 전반의 편견을 깨는 데 기여할 수 있습니다. 여성에게 기회를 제공함으로써 그들이 충분한 능력과 자격을 갖추고 있음을 보여줌으로써, 성별에 따라 달라지는 편견을 해소할 수 있습니다. 

물론 인사 발령 시 특혜가 영구적으로 필요한 것은 아니지만, 현재의 구조적인 불평등을 개선하기 위한 일시적인 조치로써 충분한 가치가 있다고 볼 수 있습니다.
"""

# [Preference(korean)]
# Elapsed Time: 5.383615732192993s
"""
저는 비대면 근무 도입에 대해 반대 입장을 제시해보겠습니다.

첫째, 비대면 근무는 회사의 팀워크와 소통을 저해할 수 있습니다. 대면 업무 환경에서는 자연스럽게 이루어지는 일상적인 대화나 즉흥적인 브레인스토밍이 감소하게 됩니다. 이는 창의성과 문제 해결 능력을 저하시키고, 결과적으로 회사의 혁신 역량을 감소시킬 수 있습니다.

둘째, 비대면 근무는 업무 효율성을 저해할 가능성이 있습니다. 집에서 일하는 환경은 사무실에 비해 훨씬 더 많은 방해 요인이 있을 수 있습니다. 가정에서 일하는 동안 가족 구성원 또는 다른 외부적인 요소들이 업무 집중도를 떨어뜨릴 수 있습니다.

셋째, 모든 직원들이 비대면 근무에 적합한 환경을 가지고 있는 것은 아닙니다. 일부 직원들은 편리하고 조용한 작업 공간이 없을 수 있으며, 인터넷 연결 상태가 불안정할 수도 있습니다. 이런 요소들이 비대면 근무의 효과성을 감소시킬 수 있습니다.

마지막으로, 비대면 근무는 근로자의 정서적 안녕에 부정적인 영향을 미칠 수 있습니다. 사람들은 사회적 상호작용을 통해 스트레스를 해소하고 동료들과의 관계를 유지합니다. 비대면 근무는 이러한 기회를 제한하며, 결과적으로 고립감을 느끼게 할 수 있습니다.

따라서 회사를 위해서라도 비대면 근무보다는 혼합형 근무 방식이나 대면 근무를 유지하는 것이 더욱 바람직하다고 생각합니다.
"""

# [Preference(korean), 지적하도록]
# Elapsed Time: 4.13s

"""
뿐만 아니라, 비대면 근무를 도입하지 말아야 한다는 이유 역시 있습니다. 첫째, 직접 대면을 통해 이룰 수 있는 팀워크와 상호작용은 기업 문화에서 중요한 부분입니다. 대면 환경에서는 즉각적인 피드백을 주고 받으며, 더 나은 아이디어를 공유하고 신속하게 문제를 해결할 수 있습니다.

둘째, 모든 직무가 비대면에 적합한 것은 아닙니다. 특히 제조업과 같은 현장 업무나 특정 IT 직무는 직접적인 조작과 관리가 필요하여 비대면으로는 한계가 있을 수 있습니다. 이러한 직무들은 대면 환경에서 더 효율적으로 수행될 수 있습니다.

세 번째로, 비대면 근무로 인해 직원들의 일상과 업무의 경계가 모호해지는 문제도 발생할 수 있습니다. 이는 장기적으로 업무 효율성을 떨어뜨리고, 심리적 스트레스를 증가시킬 수 있습니다. 오랜 시간 고립된 환경에서 일하는 것은 사회적 상호작용을 줄이며, 직무 만족도를 저하시키는 결과를 가져올 수 있습니다.

따라서, 비대면 근무의 장점도 있지만, 대면 환경에서 얻을 수 있는 다양한 이점과 일부 직무에서의 필수성 역시 간과해서는 안 됩니다.
"""


# [Speed]
# 그냥 돌릴 때는 3~9초
# -> 절대 그냥 쓰지는 못할듯..

# [Quality]
# 좋음

# => 쓰려면 답변 생성하는 동안에 Devil's Advocate is thinking이런 식으로 띄우고 못쓰게 막는 게 좋을 듯함
