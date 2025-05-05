import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
apiKey = os.getenv('OPENAI_API_KEY')
orgId = os.getenv('OPENAI_ORG_ID')
projectId = os.getenv('OPENAI_PROJECT_ID')

if not apiKey or not orgId or not projectId:
    raise ValueError("API key, Organization ID, and Project ID must be set in environment variables.")

# Initialize OpenAI
client = OpenAI(
    api_key=apiKey,
    organization=orgId,
    project=projectId
)
monthly_horoscope ="""Aries, your May 2025 forecast shows an exciting month ahead with several planets in your sign, including Venus, Mercury, Saturn, and Neptune. This planetary lineup means you'll be exceptionally busy! Saturn's arrival in your sign brings a strong sense of determination. As Saturn enters your first house, you're essentially getting a fresh start while carrying all the wisdom you've gathered over recent years.
Your money situation improves this month thanks to the Sun moving through your financial sector. The Full Moon on May 12 points to news about your finances or your partner's money matters. Your natural energy and strength are returning in full force after a period of reflection.
Your personal relationships might go through some interesting changes this month. The Moon's helpful angle with Mars suggests you'll bring lots of excitement and passion to your interactions with others. However, be careful of possible misunderstandings as Venus forms a tense angle with the Moon. Make sure your communication is clear, and use your natural charm to smooth over any rough spots that might come up. Spending quality time with friends and family will bring you emotional satisfaction and happiness.
For your health this month, focus on finding a balance between staying active and getting enough rest. With Chiron in your sign, old injuries or health issues might reappear, so pay attention to what your body is telling you. It's a good time to start new routines that mix physical activity with practices that calm your mind. Watch for signs of stress from daily pressures and give yourself time to recharge. Drinking enough water and eating a balanced diet will support your overall well-being.
In your work life, you might find yourself at a turning point where important decisions need to be made. With both Mars and Mercury in key positions, try using your creativity and sharp thinking to stand out from the crowd. Working with others might test your patience due to different opinions, but your natural leadership skills will help you through these situations. Stay flexible and open to other viewpoints to find success in your professional efforts.
Your emotional life could be quite intense this month. The Moon's interaction with various planets might heighten your sensitivity, encouraging you to explore your feelings more deeply. See this emotional ride as a chance for personal growth. You might find comfort in artistic activities or through talks with people who truly understand you. Remember, it's okay to show vulnerability, but stay true to yourself.
Travel opportunities look favorable with Saturn and Neptune aligned in your sign. Consider going to places that allow for quiet reflection while also letting you explore new cultural experiences. Even short local trips can bring unique insights about your path in life. Be open to spontaneous plans, but make sure to take necessary health and safety precautions during your travels this month.
Red and orange are your lucky colors for May, with 5, 9, and 18 as your lucky numbers. The letters A and M might bring you good fortune. If you're single, connecting with nature could help you feel more spiritually balanced. For couples, sharing thoughts about health goals and personal growth can strengthen your bond.
For the past few months, your creative process has been shifting due to new ideas, dreams, and impulses. May invites you to start fresh and create new spaces for your self-expression. Which old patterns are you ready to leave behind? As inspiration quietly builds, a new phase of vision and direction begins to take shape by the end of the month.
Life's challenges help fine-tune us to match what the universe has in store. As you move through May, your bold Aries spirit combined with Saturn's discipline creates a powerful mix of energy and structure. Use this unique combination to set intentions that align with your true self.
Your financial outlook is improving, your personal determination is strong, and your creative vision is clarifying. By month's end, you'll likely feel more centered in your purpose and ready to move forward with renewed confidence and direction."""

prompt = f"""
You are an astrology assistant. Extract specific and concise insights for the following categories from the given monthly horoscope content:

- personal life
- profession
- health
- emotions
- travel
- luck
- general_prediction (optional but helpful for any content not directly fitting in the above)

Use clear, paragraph-style natural language for each category. Avoid copying full paragraphs—summarize only the relevant parts. Return the response as a structured JSON with keys: love, travel, career, health, emotions, general_prediction.

Monthly Horoscope Content:
\"\"\"
{monthly_horoscope}
\"\"\"
"""

# Call OpenAI
try:
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    result = completion.choices[0].message.content
    print(result)
except Exception as e:
    error_message = str(e)
    if "insufficient_quota" in error_message:
        print(f"You have exceeded your current quota. Please check your plan and billing details.\nError: {error_message}")
    else:
        print(f"An error occurred: {e}")