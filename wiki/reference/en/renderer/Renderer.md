---
tags:
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Class "Renderer"

## Functions

<div class="rgon-only" markdown="1">

### LoadImage () {: aria-label='Functions' }
#### [Image](Image.md) LoadImage ( string filePath ) {: .copyable aria-label='Functions' }     [ ](#){: .rgonorplus .tooltip .badge }

___

### Pipeline () {: aria-label='Functions' }
#### [Pipeline](Pipeline.md) Pipeline ( ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ProjectionMatrix () {: aria-label='Functions' }
#### [GLMat4](GLSLValue.md) ProjectionMatrix ( ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }

___

### RenderSet () {: aria-label='Functions' }
#### void RenderSet ( ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }

___

### Shader () {: aria-label='Functions' }
#### [Shader](Shader.md) Shader ( string vertexShader, string fragmentShader, [VertexDescriptor](VertexDescriptor.md) vertexDescriptor ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }

___

### StartTransformation () {: aria-label='Functions' }
#### [Transformer](Transformer.md) StartTransformation ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### Vec2 () {: aria-label='Functions' }
#### [GLVec2](GLSLValue.md) Vec2 ( float x = 0, float y = 0 ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }

___

### Vec3 () {: aria-label='Functions' }
#### [GLVec3](GLSLValue.md) Vec3 ( float x = 0 float y = 0, float z = 0 ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }

___

### Vec4 () {: aria-label='Functions' }
#### [GLVec4](GLSLValue.md) Vec4 ( float x = 0 float y = 0, float z = 0, float w = 0 ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }

___

### VertexDescriptor () {: aria-label='Functions' }
#### [VertexDescriptor](VertexDescriptor.md) VertexDescriptor ( ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CreateImage () {: aria-label='Functions' }
#### [Image](Image.md) CreateImage ( integer width, integer height, string name ) {: .copyable aria-label='Functions' }     [ ](#){: .rgonplus .tooltip .badge }

___

### RenderToImage () {: aria-label='Functions' }
#### void RenderToImage ( [Image](Image.md) image, function renderFunction ) {: .copyable aria-label='Functions' }     [ ](#){: .rgonplus .tooltip .badge }

Sets the specified `Image` as the current render target and executes `renderFunction`.

All rendering operations must be performed inside `renderFunction`, as the previous render target is restored immediately after the function returns.

Only images created using [CreateImage](#createimage)() or surfaces created by the game may be used as render targets.

`renderFunction` may take a [SurfaceRenderController](SurfaceRenderController.md) as it's first parameter, allowing access to additional render operations for the active render target.

???- example "Example Code"

    ```lua

    local exampleSurface = Renderer.CreateImage(128, 128, "Example Surface")

    local function UpdateSurfaceContents(renders)
        Renderer.RenderToImage(exampleSurface, function(controller)
            controller:Clear()
            for _, render in ipairs(renders) do
                local sprite = render[1]
                local position = render[2]
                sprite:Render(position)
            end
        end)
    end
    ```

___

### GetShaderByType () {: aria-label='Functions' }
#### [Shader](Shader.md) GetShaderByType ( [ShaderType](../enums/ShaderType.md) shaderType ) {: .copyable aria-label='Functions' }     [ ](#){: .rgonplus .tooltip .badge }

Returns one of the in-game shaders.

___

### LoadShader () {: aria-label='Functions' }
#### [Shader](Shader.md) LoadShader ( string filePath, table vertexDescriptor ) {: .copyable aria-label='Functions' }     [ ](#){: .rgonplus .tooltip .badge }

`filePath` should be specified without a file extension, and it must be relative to the `resources/` directory.

Both a `.vs` and a `.fs` must exist in the specified location.

???- info "VertexDescriptor"
    VertexDescriptor is an array of tables, with each entry being a pair of `[string, VertexAttributeFormat]`,
    with string being the attribute name.

    The attribute name must be the exact same as the one used in the shader.

???- example "Example Code"
    This code shows how color offset gold would need to be loaded if it were a custom shader.

    ```lua
        local fmt = Renderer.VertexAttributeFormat

        local vertexDesc = {
            {"Position", fmt.POSITION},
            {"Color", fmt.COLOR},
            {"TexCoord", fmt.TEX_COORD},
            {"ColorizeIn", fmt.VEC4},
            {"ColorOffsetIn", fmt.VEC3},
            {"TextureSize", fmt.VEC2},
            {"PixelationAmount", fmt.FLOAT},
            {"ClipPlane", fmt.VEC3},
        }

        local goldShader = Renderer.LoadShader("shaders/coloroffset_gold", vertexDesc)
    ```

___

### GetPixelationAmount () {: aria-label='Functions' }
#### number GetPixelationAmount ( ) {: .copyable aria-label='Functions' }     [ ](#){: .rgonplus .tooltip .badge }

___

### GetClipPaneNormal () {: aria-label='Functions' }
#### [Vector](../Vector.md) GetClipPaneNormal ( ) {: .copyable aria-label='Functions' }     [ ](#){: .rgonplus .tooltip .badge }

___

### GetClipPaneThreshold () {: aria-label='Functions' }
#### number GetClipPaneThreshold ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>
