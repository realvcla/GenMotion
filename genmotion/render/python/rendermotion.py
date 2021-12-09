import numpy as np
import imageio
import os
import torch
from tqdm import tqdm
from genmotion.render.python.renderer import get_renderer
import genmotion.render.python.utils as geometry

def get_rotation(theta=np.pi/3):
    axis = torch.tensor([0, 1, 0], dtype=torch.float)
    axisangle = theta*axis
    matrix = geometry.axis_angle_to_matrix(axisangle)
    return matrix.numpy()


def render_video(meshes, key, action, renderer, savepath, background, cam=(0.75, 0.75, 0, 0.10), color=[0.11, 0.53, 0.8]):
    writer = imageio.get_writer(savepath, fps=30)
    # center the first frame
    meshes = meshes - meshes[0].mean(axis=0)
    # matrix = get_rotation(theta=np.pi/4)
    # meshes = meshes[45:]
    # meshes = np.einsum("ij,lki->lkj", matrix, meshes)
    imgs = []
    for mesh in tqdm(meshes, desc=f"Visualize {key}, action {action}"):
        img = renderer.render(background, mesh, cam, color=color)
        imgs.append(img)
        # show(img)

    imgs = np.array(imgs)
    masks = ~(imgs/255. > 0.96).all(-1)

    coords = np.argwhere(masks.sum(axis=0))
    y1, x1 = coords.min(axis=0)
    y2, x2 = coords.max(axis=0)

    for cimg in imgs[:, y1:y2, x1:x2]:
        writer.append_data(cimg)
    writer.close()


def render(data: np.array, save_folder: str):

    if data.shape[0] == 3:
        visualization, generation, reconstruction = data
        data = {"visualization": visualization,
                  "generation": generation,
                  "reconstruction": reconstruction}
    else:
        # output = {f"generation_{key}": output[key] for key in range(2)} #  len(output))}
        # output = {f"generation_{key}": output[key] for key in range(len(output))}
        data = {f"generation_{key}": data[key] for key in range(len(data))}

    width = 1024
    height = 1024

    background = np.zeros((height, width, 3))
    renderer = get_renderer(width, height)

    # if duration mode, put back durations
    if data["generation_3"].shape[-1] == 100:
        data["generation_0"] = data["generation_0"][:, :, :, :40]
        data["generation_1"] = data["generation_1"][:, :, :, :60]
        data["generation_2"] = data["generation_2"][:, :, :, :80]
        data["generation_3"] = data["generation_3"][:, :, :, :100]
    elif data["generation_3"].shape[-1] == 160:
        print("160 mode")
        data["generation_0"] = data["generation_0"][:, :, :, :100]
        data["generation_1"] = data["generation_1"][:, :, :, :120]
        data["generation_2"] = data["generation_2"][:, :, :, :140]
        data["generation_3"] = data["generation_3"][:, :, :, :160]

    # if str(action) == str(1) and str(key) == "generation_4":
    for key in data:
        vidmeshes = data[key]
        for action in range(len(vidmeshes)):
            meshes = vidmeshes[action].transpose(2, 0, 1)
            path = os.path.join(save_folder, "action{}_{}.mp4".format(action, key))
            render_video(meshes, key, action, renderer, path, background)