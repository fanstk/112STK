# GLB/GLTF Track Support

You can now use custom 3D tracks in GLB or GLTF format!

## How to Add a Custom Track

1. **Create your track model** in Blender, Maya, or any 3D software
2. **Export as .glb or .gltf** format
3. **Place the file** in the `/racetracks/` folder
4. **The track will automatically appear** in the track selection menu

## Mesh Collider

- The system automatically generates a mesh collider from your GLB model
- This means the exact shape of your 3D model becomes the collision boundary
- Cars will collide with the actual geometry of your track

## Recommended Track Design

For best results:
- Create a closed loop track
- Keep walls on both sides of the track path
- Ensure the track is roughly centered at origin (0, 0, 0)
- Use simple geometry for better collision performance

## Notes

- Checkpoints are auto-generated based on the model's bounding box
- For precise checkpoint placement, consider using the traditional `.track` file format
- GLB tracks work alongside existing `.track` files
