import torch
from diffusers import StableDiffusionPipeline


dish = ['Roasted Potato and Carrot Medley', 'Potato and Carrot Soup']
model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

# インスタンス化とcudaに転送
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)

for i, dish in enumerate(dish):
    # print(dish)
    prompt = "a photo of an " + dish
    # 多分画像生成してるところ
    image = pipe(prompt).images[0]  
        
    image.save(f"{i}.png")
    print(type(image))