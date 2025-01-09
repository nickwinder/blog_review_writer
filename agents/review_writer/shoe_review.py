shoe_name = "Altra FWD Via"
post_name = shoe_name.replace(" ", "_")

input_prompt = ("Write a 1500 word comprehensive review of the " + shoe_name + "with casual humanlike style, using transitional phrases, and avoidance of unnatural sentence structure while explaining in details extensively and comprehensively.\n"
                    "The review should have 5 major sections: Introduction, Fit, Feel, Durability, and Conclusion.\n"
                    "Introduction - Should be short containing 5-6 sentences, each on separate lines teasing some of the key features of the model, and enticing the reader to keep reading.\n"
                    "Fit - A section of around 500 words with multiple paragraphs each focusing on different aspects of the shoe fit. Ensure you cover the suggested sizing (for example true to size, or 1/2 size up or down), the width in different areas of the shoe, and depth in different areas of the shoe. Each paragraph should be 2-3 sentences, and the first sentence of each paragraph should be bolded to allow the section to be skimmable by the reader.\n"
                    "Feel - A section of around 500 words with multiple paragraphs each focusing on a different aspect of the feel of the shoe. This could be flexibility, stiffness, grip, stack height etc. Each paragraph should be 2-3 sentences, and the first sentence of each paragraph should be bolded to allow the section to be skimmable by the reader.\n"
                    "Durability - A section of around 500 words with multiple paragraphs each focusing on a different aspect of the durability of the shoe. Focus on the outsole, midsole if it has one, and the upper construction of the shoe. Each paragraph should be 2-3 sentences, and the first sentence of each paragraph should be bolded to allow the section to be skimmable by the reader.\n"
                    "Conclusion - Wrap up the review suggesting some final thoughts and what other shoes a user should consider.")

research = """
## My Opinions on Altra FWD

**Specifications:**
- Forefoot Height: 33 millimeters
- Heel Height: 37 millimeters
- Drop: 4 millimeters (high stack height for a running shoe)

The Altra FWD Via is a newer model from Altra that includes a drop, which is something I don’t typically prefer. 

#### Fit

- **Toe Box:** 
  - Similar to the Olympus Vier or Olympus trail models.
  - The upper features a thinner, tightly woven mesh with some structure around the toe box.
  - The depth of the toe box is average; it’s neither too high nor too low. 
  - I did not touch the top of the toe box when flexing my toes, which was comfortable.

- **Midfoot:**
  - Moderately wide, reminiscent of the Olympus model.
  - The side walls of the midsole foam extend up around the sides of the feet, which can restrict wider or flatter feet but offers a moderate width compared to other Altra models like the narrower Rivera and Escalante.
  - Stats indicate that its width is similar to the Olympus 6, likely very close to this model as well.

- **Heel:**
  - Quite structured but can bend when pressure is applied.
  - The side walls come up high around the heel area, creating a bucket-like fit that enhances stability.
  - Some discomfort is noticeable due to the sensation of lumps and bumps from the footbed's molding.

- **Insole:** 
  - Approximately 5 millimeters in height. 
  - Can be swapped out for additional depth if needed.

- **Lacing System:**
  - Needed to use a lace lock, as the heel lock was not perfect. The lace lock helped secure the midfoot effectively.

#### Midsole

- The new midsole foam, called **Ego Flow**, is softer and lighter.
- Despite the high stack height, the shoe weighs only 264 grams, which is light for its size.
- The foam is squishy underfoot but remains stable due to the wider base and structural elements around the sides.
- A noticeable heel bevel helps promote a softer landing and reduces the slap upon impact.
- Walking felt uncomfortable due to some backward rolling; however, running didn't pose any issues since I typically land more towards the forefoot rather than the heel.
- There is some ramp up of the midsole and a tiny bit of toe spring, primarily focused towards the forefoot, enhancing a rocking motion during movement.

#### Outsole

- Features some exposed foam but primarily comprises rubber from the forefoot forward, resembling the rubber on other Altra models.
- Durability seems adequate, though performance may vary in wet conditions.
- Rubber extends along both sides of the heel and the outer foot, with exposed foam mainly found in the cracks of the rubber and under the arch.

#### Durability Considerations

- The midsole's durability is a question mark given the new foam's softness. 
- I worry it may wear down more quickly if highly structured, which is critical for individuals who require a structured shoe.
- The rubber outsole should hold up well, and I expect the upper will remain intact since it doesn't slide around excessively, minimizing cornering issues.
- Eyelets are reinforced, although some lace loops could be more traditionally designed.

#### Comfort & Feel

- The tongue is short, padded, and semi-gusseted, preventing it from sliding around.
- A small bungee loop at the back aids in putting the shoe on.

**Overall Experience:**
- The 4mm drop was noticeable, pushing me forward into a rolling motion towards the front of the foot.
- Picking up the pace felt strange despite the lightness, likely due to the lack of ground feel; the squishy underfoot sensation affected stability when accelerating.
- While the shoe offered good security and lateral stability, I prefer a lower drop or stack height for faster paces. 

In summary, while secure and stable, the Altra FWD Via may not be ideal for everyone, especially if you value ground feel and a lower drop for speed work. It has its strengths in comfort and fit but comes with certain constraints due to its structure and midsole properties.

## My opinions on 4mm drop shoes 
- A 4mm drop isn't a significant difference in the context of running shoes. Minor variations in manufacturing can lead to a drop of 1-2 millimeters even in zero-drop shoes.
- Some shoes may even have a negative drop, which is worth noting.
- For heavy heel strikers, as the foam wears out over time, the heel will often compress more quickly than the forefoot. This wear can result in a progressively lower drop throughout the shoe's lifespan.
- While 4mm may not seem substantial, it is noticeable, particularly when trying the shoe on for the first time. However, it's not a major concern overall
- In the context of the Altra lineup, the presence of a drop allows runners transitioning from shoes with a higher drop (such as Hoka or Nike) to adapt more comfortably. The drop helps lessen the load on both the foot and calves while still maintaining the wider toe box, which is beneficial for foot health.
- The intended use for this type of shoe is that athletes might start with a shoe like this and gradually transition to a zero-drop model and a less structured shoe over time.

## My opinions on structured shoes
As mentioned, the shoe features high side walls and a structured footbed that creates a cup-like sensation around the heel, extending slightly into the arch with minimal arch support. 
I personally don't view this structure as beneficial. While it may be useful for someone transitioning from a shoe that offers similar support, especially if they are moving towards a zero-drop shoe or need a wider toe box for improved foot health, it should only be a temporary solution during the transition. 
In the long term, once foot and ankle health have improved sufficiently, there are limited uses for this kind of structure. Therefore, I am not entirely convinced about the design’s effectiveness.
"""
