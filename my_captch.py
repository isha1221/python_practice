# from captcha.image import ImageCaptcha
# import random
# import string

# # Function to generate random CAPTCHA text
# def generate_captcha_text(length=6):
#     characters = string.ascii_letters + string.digits
#     return ''.join(random.choices(characters, k=length))

# # Function to generate a CAPTCHA image
# def generate_captcha_image(text, output_path):
#     # Create an ImageCaptcha instance
#     captcha = ImageCaptcha(width=280, height=90)
#     # Generate the CAPTCHA image
#     image = captcha.generate_image(text)
#     # Save the image to the specified path
#     image.save(output_path)
#     print(f"CAPTCHA saved at: {output_path}")

# if __name__ == "__main__":
#     # Generate random CAPTCHA text
#     captcha_text = generate_captcha_text()
#     print(f"Generated CAPTCHA text: {captcha_text}")
#     # Generate and save CAPTCHA image
#     generate_captcha_image(captcha_text, "captcha.png")
from captcha.image import ImageCaptcha
from PIL import ImageDraw
import random
import string

# Function to generate random CAPTCHA text
def generate_captcha_text(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

# Function to generate random alphanumeric filename
def generate_filename(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length)) + ".png"

# Function to add noise (random lines) to the image
def add_noise(image):
    draw = ImageDraw.Draw(image)
    width, height = image.size

    # Add random lines for noise
    for _ in range(5):  # Number of noise lines
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill="black", width=2)

    return image

# Function to generate a CAPTCHA image
def generate_captcha_image(text, output_path):
    # Create an ImageCaptcha instance
    captcha = ImageCaptcha(width=280, height=90)
    # Generate the CAPTCHA image
    image = captcha.generate_image(text)
    # Add noise to the image
    image = add_noise(image)
    # Save the image to the specified path
    image.save(output_path)
    print(f"CAPTCHA saved at: {output_path}")

if __name__ == "__main__":
    # Generate random CAPTCHA text
    captcha_text = generate_captcha_text()
    print(f"Generated CAPTCHA text: {captcha_text}")
    # Generate a random filename
    captcha_filename = generate_filename()
    print(f"Generated CAPTCHA filename: {captcha_filename}")
    # Generate and save CAPTCHA image
    generate_captcha_image(captcha_text, captcha_filename)
