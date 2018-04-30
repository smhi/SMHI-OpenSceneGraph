#include <osgDB/Registry>

USE_SERIALIZER_WRAPPER(osgShadow_DebugShadowMap)
USE_SERIALIZER_WRAPPER(osgShadow_LightSpacePerspectiveShadowMapCB)
USE_SERIALIZER_WRAPPER(osgShadow_LightSpacePerspectiveShadowMapDB)
USE_SERIALIZER_WRAPPER(osgShadow_LightSpacePerspectiveShadowMapVB)
USE_SERIALIZER_WRAPPER(osgShadow_MinimalCullBoundsShadowMap)
USE_SERIALIZER_WRAPPER(osgShadow_MinimalDrawBoundsShadowMap)
USE_SERIALIZER_WRAPPER(osgShadow_MinimalShadowMap)
USE_SERIALIZER_WRAPPER(osgShadow_ParallelSplitShadowMap)
USE_SERIALIZER_WRAPPER(osgShadow_ShadowedScene)
USE_SERIALIZER_WRAPPER(osgShadow_ShadowMap)
USE_SERIALIZER_WRAPPER(osgShadow_ShadowTechnique)
USE_SERIALIZER_WRAPPER(osgShadow_ShadowTexture)
USE_SERIALIZER_WRAPPER(osgShadow_ShadowVolume)
USE_SERIALIZER_WRAPPER(osgShadow_SoftShadowMap)
USE_SERIALIZER_WRAPPER(osgShadow_StandardShadowMap)
USE_SERIALIZER_WRAPPER(osgShadow_ViewDependentShadowTechnique)

extern "C" void wrapper_serializer_library_osgShadow(void) {}

