import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LLMs.llm import gpt4oWriter

from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Load the plan prompt template
with open(os.path.join(os.path.dirname(__file__), 'prompts', 'final_polish.txt'), 'r') as file:
    plan_template = file.read()

# Create a PromptTemplate
final_polish_prompt = ChatPromptTemplate([
        ('user', plan_template)
    ])


final_polish_chain = final_polish_prompt | gpt4oWriter | StrOutputParser()


## For testing
if __name__ == "__main__":
    # Test the plan_chain
    test_instruction = (
        "Write a 1500 word comprehensive review of the Altra King MT 2 with casual humanlike style, using transitional phrases, and avoidance of unnatural sentence structure while explaining in details extensively and comprehensively. Remember, you're not trying to sell the shoe, you're trying to bring the facts.\n"
        "The review should have 5 major sections: Introduction, Fit, Feel, Durability, and Conclusion.\n"
        "Introduction - Should be short containing 5-6 sentences, each on separate lines teasing some of the key features of the model, and enticing the reader to keep reading.\n"
        "Fit - A section of around 500 words with multiple paragraphs each focusing on different aspects of the shoe fit. Ensure you cover the suggested sizing (for example true to size, or 1/2 size up or down), the width in different areas of the shoe, and depth in different areas of the shoe. Each paragraph should be 2-3 sentences, and the first sentence of each paragraph should be bolded to allow the section to be skimmable by the reader.\n"
        "Feel - A section of around 500 words with multiple paragraphs each focusing on a different aspect of the feel of the shoe. This could be flexibility, stiffness, grip, stack height etc. Each paragraph should be 2-3 sentences, and the first sentence of each paragraph should be bolded to allow the section to be skimmable by the reader.\n"
        "Durability - A section of around 500 words with multiple paragraphs each focusing on a different aspect of the durability of the shoe. Focus on the outsole, midsole if it has one, and the upper construction of the shoe. Each paragraph should be 2-3 sentences, and the first sentence of each paragraph should be bolded to allow the section to be skimmable by the reader.\n"
        "Conclusion - Wrap up the review suggesting some final thoughts and what other shoes a user should consider.")

    content = """The Altra King MT 2 stands out with its specialized Vibram outsole and robust construction, designed spmecifically for tackling rugged terrains and providing exceptional grip in challenging conditions.

Whether you're navigating alpine trails or rocky paths, this shoe excels with its remarkable grip and comfort. Its performance in muddy conditions is unmatched, making it a reliable choice for those seeking stability and confidence on challenging terrains.

Trail runners and outdoor enthusiasts looking for a dependable shoe to conquer challenging environments will find the Altra King MT 2 an ideal companion. Dive into the following sections for more insights.

**When it comes to sizing, the Altra King MT 2 generally fits true to size, which is a relief for those who often find themselves between sizes.** However, some users with wider feet might consider going half a size up to ensure a more comfortable fit, especially during longer runs when feet tend to swell. Proper sizing is crucial as it directly impacts the shoe's performance and comfort, allowing for a snug fit that prevents unnecessary movement within the shoe. This ensures that the runner can fully benefit from the shoe's design, maintaining stability and reducing the risk of blisters or discomfort.

**The width of the Altra King MT 2 is designed to accommodate a variety of foot shapes, offering a generous toe box that allows for natural toe splay.** This feature is particularly beneficial for trail runners who require extra stability and comfort on uneven terrains. The wider forefoot not only enhances balance but also reduces the likelihood of pressure points, which can be a common issue in narrower shoes. For those with broader feet, this design ensures that the shoe remains comfortable over long distances, providing a secure fit that supports the foot's natural movement without compromising on performance.

**The depth of the Altra King MT 2 plays a significant role in its overall fit and comfort, particularly in the toe box and heel areas.** The toe box is not only wide but also deep, allowing ample room for toe movement and reducing the risk of cramping during long runs. This depth is crucial for maintaining comfort, especially on descents where toes might otherwise be pushed forward. Meanwhile, the heel depth ensures a snug fit, preventing slippage and enhancing stability on uneven terrains. Together, these features contribute to a secure and comfortable experience, allowing runners to focus on the trail ahead.

**The fit of the Altra King MT 2 significantly enhances performance by providing a secure and comfortable experience, especially in challenging terrains.** The combination of a true-to-size fit, generous width, and ample depth ensures that the shoe adapts well to the natural shape of the foot, minimizing movement and maximizing stability. This tailored fit is particularly advantageous on rugged trails, where a secure footing is essential to navigate obstacles and maintain balance. By reducing the risk of blisters and discomfort, the Altra King MT 2 allows runners to focus on their performance, confidently tackling even the most demanding environments.

**In summary, the overall fit of the Altra King MT 2 is a standout feature that significantly contributes to its comfort and performance on the trail.** The shoe's true-to-size fit, combined with its accommodating width and depth, ensures a personalized feel that supports natural foot movement. For those seeking the best fit, it's advisable to try the shoe on with the socks you plan to wear during runs, and consider sizing up if you have wider feet or anticipate swelling during longer distances. This attention to fit details allows runners to fully leverage the shoe's design, enhancing their trail running experience.

**The flexibility of the Altra King MT 2 strikes a harmonious balance between offering ground feel and ensuring protection, making it a versatile choice for varied terrains.** This shoe's design allows for a natural foot movement, which is crucial for adapting to the unpredictable surfaces encountered on trails. The midsole provides just enough give to feel connected to the ground, enhancing agility and responsiveness without sacrificing the protective features needed for rocky or uneven paths. This balance is particularly beneficial for trail runners who need to quickly adjust their footing while maintaining stability. By offering a flexible yet protective experience, the Altra King MT 2 empowers runners to confidently tackle diverse environments, from soft forest trails to rugged mountain paths, without compromising on performance or safety.

**The stiffness of the Altra King MT 2 plays a pivotal role in providing stability and support, especially when navigating rocky and uneven terrains.** This shoe's construction incorporates a firm midsole that offers a solid platform, crucial for maintaining balance and preventing foot fatigue during long runs. The stiffness ensures that the foot remains well-supported, reducing the risk of twisting or rolling on unpredictable surfaces. While some might find the rigidity a bit limiting in terms of flexibility, it ultimately enhances the runner's confidence by delivering a secure and stable ride. This characteristic is particularly advantageous for those tackling technical trails, where a firm and supportive shoe can make all the difference in maintaining a steady pace and avoiding potential injuries.

**The grip of the Altra King MT 2 is one of its most impressive features, thanks to the specialized Vibram outsole that excels in both muddy and rocky conditions.** This outsole is designed with a full hook pattern that provides exceptional traction, allowing runners to maintain their footing even on slippery or uneven surfaces. The effectiveness of this grip is particularly noticeable in challenging environments, where maintaining stability is crucial for safety. By offering reliable traction, the Altra King MT 2 enhances the runner's confidence, enabling them to tackle trails with assurance and focus on their performance rather than worrying about potential slips or falls. This robust grip makes the shoe an ideal choice for those who frequently encounter unpredictable terrains.

**The stack height of the Altra King MT 2 is thoughtfully designed to provide a balanced blend of cushioning and ground feel, making it suitable for a variety of trail running environments.** With a moderate stack height, this shoe offers enough cushioning to absorb impact on hard surfaces, reducing strain on the joints during long runs. At the same time, it maintains a low enough profile to ensure a responsive connection with the ground, which is essential for navigating technical trails with precision. This balance allows runners to enjoy the comfort needed for endurance while still feeling agile and in control on uneven terrains. Whether tackling steep ascents or fast descents, the Altra King MT 2's stack height supports a versatile and adaptable trail running experience.

**The durability of the Altra King MT 2's outsole is a testament to its robust construction, primarily due to the high-quality Vibram material used.** This specialized outsole is engineered to withstand the rigors of diverse terrains, from rocky paths to muddy trails, without showing significant signs of wear and tear. The Vibram material not only provides exceptional grip but also enhances the shoe's longevity, making it a reliable choice for trail runners who frequently tackle challenging environments. By maintaining its structural integrity over time, the outsole ensures that the Altra King MT 2 remains a dependable companion for countless adventures, offering consistent performance and protection even after extensive use. This durability is a key factor in the shoe's appeal, promising long-lasting value for outdoor enthusiasts.

**The midsole construction of the Altra King MT 2 is crafted with precision, utilizing a dual-layer EVA foam that offers both cushioning and support.** This material is known for its ability to absorb shock, which is crucial for reducing impact on joints during long runs on hard surfaces. Over time, the EVA foam maintains its resilience, ensuring that the shoe continues to provide a comfortable ride even after extensive use. This durability is complemented by the shoe's ability to retain its supportive structure, preventing the midsole from compressing excessively and losing its effectiveness. As a result, the Altra King MT 2 delivers consistent performance, allowing trail runners to rely on its cushioning and support for numerous adventures, enhancing both comfort and longevity.

**The upper construction of the Altra King MT 2 is meticulously designed to endure the rigors of harsh trail conditions, thanks to its durable materials and reinforced stitching.** The upper is crafted from a robust mesh that balances breathability with protection, allowing for adequate airflow while shielding the foot from debris and abrasions. The strategic placement of reinforced stitching enhances the shoe's structural integrity, ensuring that it holds up well against the wear and tear of rugged terrains. This thoughtful construction not only contributes to the shoe's longevity but also provides a secure fit that adapts to the foot's movements. By maintaining its form and function over time, the Altra King MT 2's upper ensures that trail runners can confidently tackle challenging environments without compromising on comfort or durability.

**The overall durability of the Altra King MT 2 is a testament to its thoughtfully engineered components, each contributing to the shoe's long-lasting performance.** The Vibram outsole stands out with its exceptional resistance to wear, providing reliable traction across diverse terrains while maintaining its structural integrity. Complementing this is the dual-layer EVA foam midsole, which offers enduring cushioning and support, ensuring comfort over extended use without succumbing to compression. Meanwhile, the robust upper construction, with its durable mesh and reinforced stitching, withstands the challenges of rugged trails, offering both protection and breathability. Together, these elements create a cohesive design that not only enhances the shoe's longevity but also ensures consistent performance, making the Altra King MT 2 a dependable choice for trail enthusiasts.

**The Altra King MT 2 excels with its exceptional grip, robust durability, and adaptability to challenging terrains, making it a standout choice for trail runners and outdoor enthusiasts.** Its Vibram outsole ensures reliable traction, while the durable construction withstands the rigors of rugged environments. These features collectively provide a secure and comfortable experience, allowing adventurers to confidently tackle diverse trails. The shoe's thoughtful design and performance capabilities make it a trusted companion for those seeking reliability and endurance in their footwear.

While the Altra King MT 2 excels in many areas, there is room for improvement in enhancing its flexibility to cater to those who prefer a more adaptable feel. Additionally, addressing minor fit issues could broaden its appeal, offering a more customized experience for a wider range of foot shapes.

For those seeking alternatives to the Altra King MT 2, the Altra Superior offers increased flexibility and a lighter build, making it ideal for drier, less rugged terrains. Meanwhile, the Mont Blanc provides a different comfort experience, with enhanced cushioning for those prioritizing a softer ride. These options cater to varying preferences, ensuring that trail runners can find a shoe that aligns with their specific needs and the conditions they frequently encounter.

Total word count: 1797
"""

    # Invoke the plan_chain
    result = final_polish_chain.invoke({"instructions": test_instruction, "content": content})
    
    # Print the result
    print("Generated Writing Plan:")
    print(result)


