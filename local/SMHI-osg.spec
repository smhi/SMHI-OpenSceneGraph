%define appname SMHI-OpenSceneGraph
%define name SMHI-OpenSceneGraph
%define version 3.6.3
%define release 1.0
%define vendor	smhi.se

Summary: Systemd unit file for %{appname}
Name: %{appname}
Version: %{version}
Release: %{release}
License: SMHI
Group: Utilities
URL: http://www.smhi.se/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Systemd unit file for %{appname}

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
cd $RPM_BUILD_ROOT/usr
tar xvzf $RPM_SOURCE_DIR/SMHI-OpenSceneGraph.tar.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post

%preun

%files
%defattr(-,root,root,-)
/usr/bin/osg2cpp
   /usr/bin/osganalysis
   /usr/bin/osgarchive
   /usr/bin/osgconv
   /usr/bin/osgfilecache
   /usr/bin/osgshaderpipeline
   /usr/bin/osgversion
   /usr/bin/osgviewer
   /usr/bin/osgvolume
   /usr/bin/present3D
   /usr/include/OpenThreads/Affinity
   /usr/include/OpenThreads/Atomic
   /usr/include/OpenThreads/Barrier
   /usr/include/OpenThreads/Block
   /usr/include/OpenThreads/Condition
   /usr/include/OpenThreads/Config
   /usr/include/OpenThreads/Exports
   /usr/include/OpenThreads/Mutex
   /usr/include/OpenThreads/ReadWriteMutex
   /usr/include/OpenThreads/ReentrantMutex
   /usr/include/OpenThreads/ScopedLock
   /usr/include/OpenThreads/Thread
   /usr/include/OpenThreads/Version
   /usr/include/osg/AlphaFunc
   /usr/include/osg/AnimationPath
   /usr/include/osg/ApplicationUsage
   /usr/include/osg/ArgumentParser
   /usr/include/osg/Array
   /usr/include/osg/AttributeDispatchers
   /usr/include/osg/AudioStream
   /usr/include/osg/AutoTransform
   /usr/include/osg/Billboard
   /usr/include/osg/BindImageTexture
   /usr/include/osg/BlendColor
   /usr/include/osg/BlendEquation
   /usr/include/osg/BlendEquationi
   /usr/include/osg/BlendFunc
   /usr/include/osg/BlendFunci
   /usr/include/osg/BoundingBox
   /usr/include/osg/BoundingSphere
   /usr/include/osg/BoundsChecking
   /usr/include/osg/BufferIndexBinding
   /usr/include/osg/BufferObject
   /usr/include/osg/BufferTemplate
   /usr/include/osg/Callback
   /usr/include/osg/Camera
   /usr/include/osg/CameraView
   /usr/include/osg/Capability
   /usr/include/osg/ClampColor
   /usr/include/osg/ClearNode
   /usr/include/osg/ClipControl
   /usr/include/osg/ClipNode
   /usr/include/osg/ClipPlane
   /usr/include/osg/ClusterCullingCallback
   /usr/include/osg/CollectOccludersVisitor
   /usr/include/osg/ColorMask
   /usr/include/osg/ColorMaski
   /usr/include/osg/ColorMatrix
   /usr/include/osg/ComputeBoundsVisitor
   /usr/include/osg/Config
   /usr/include/osg/ContextData
   /usr/include/osg/ConvexPlanarOccluder
   /usr/include/osg/ConvexPlanarPolygon
   /usr/include/osg/CoordinateSystemNode
   /usr/include/osg/CopyOp
   /usr/include/osg/CullFace
   /usr/include/osg/CullSettings
   /usr/include/osg/CullStack
   /usr/include/osg/CullingSet
   /usr/include/osg/DeleteHandler
   /usr/include/osg/Depth
   /usr/include/osg/DepthRangeIndexed
   /usr/include/osg/DispatchCompute
   /usr/include/osg/DisplaySettings
   /usr/include/osg/DrawPixels
   /usr/include/osg/Drawable
   /usr/include/osg/Endian
   /usr/include/osg/Export
   /usr/include/osg/Fog
   /usr/include/osg/FragmentProgram
   /usr/include/osg/FrameBufferObject
   /usr/include/osg/FrameStamp
   /usr/include/osg/FrontFace
   /usr/include/osg/GL
   /usr/include/osg/GL2Extensions
   /usr/include/osg/GLDefines
   /usr/include/osg/GLExtensions
   /usr/include/osg/GLObjects
   /usr/include/osg/GLU
   /usr/include/osg/Geode
   /usr/include/osg/Geometry
   /usr/include/osg/GraphicsContext
   /usr/include/osg/GraphicsCostEstimator
   /usr/include/osg/GraphicsThread
   /usr/include/osg/Group
   /usr/include/osg/Hint
   /usr/include/osg/Identifier
   /usr/include/osg/Image
   /usr/include/osg/ImageSequence
   /usr/include/osg/ImageStream
   /usr/include/osg/ImageUtils
   /usr/include/osg/KdTree
   /usr/include/osg/LOD
   /usr/include/osg/Light
   /usr/include/osg/LightModel
   /usr/include/osg/LightSource
   /usr/include/osg/LineSegment
   /usr/include/osg/LineStipple
   /usr/include/osg/LineWidth
   /usr/include/osg/LogicOp
   /usr/include/osg/Material
   /usr/include/osg/Math
   /usr/include/osg/Matrix
   /usr/include/osg/MatrixTransform
   /usr/include/osg/Matrixd
   /usr/include/osg/Matrixf
   /usr/include/osg/MixinVector
   /usr/include/osg/Multisample
   /usr/include/osg/Node
   /usr/include/osg/NodeCallback
   /usr/include/osg/NodeTrackerCallback
   /usr/include/osg/NodeVisitor
   /usr/include/osg/Notify
   /usr/include/osg/Object
   /usr/include/osg/Observer
   /usr/include/osg/ObserverNodePath
   /usr/include/osg/OccluderNode
   /usr/include/osg/OcclusionQueryNode
   /usr/include/osg/OperationThread
   /usr/include/osg/PagedLOD
   /usr/include/osg/PatchParameter
   /usr/include/osg/Plane
   /usr/include/osg/Point
   /usr/include/osg/PointSprite
   /usr/include/osg/PolygonMode
   /usr/include/osg/PolygonOffset
   /usr/include/osg/PolygonStipple
   /usr/include/osg/Polytope
   /usr/include/osg/PositionAttitudeTransform
   /usr/include/osg/PrimitiveRestartIndex
   /usr/include/osg/PrimitiveSet
   /usr/include/osg/PrimitiveSetIndirect
   /usr/include/osg/Program
   /usr/include/osg/Projection
   /usr/include/osg/ProxyNode
   /usr/include/osg/Quat
   /usr/include/osg/Referenced
   /usr/include/osg/RenderInfo
   /usr/include/osg/SampleMaski
   /usr/include/osg/Sampler
   /usr/include/osg/Scissor
   /usr/include/osg/ScissorIndexed
   /usr/include/osg/ScriptEngine
   /usr/include/osg/Sequence
   /usr/include/osg/ShadeModel
   /usr/include/osg/Shader
   /usr/include/osg/ShaderAttribute
   /usr/include/osg/ShaderComposer
   /usr/include/osg/ShadowVolumeOccluder
   /usr/include/osg/Shape
   /usr/include/osg/ShapeDrawable
   /usr/include/osg/State
   /usr/include/osg/StateAttribute
   /usr/include/osg/StateAttributeCallback
   /usr/include/osg/StateSet
   /usr/include/osg/Stats
   /usr/include/osg/Stencil
   /usr/include/osg/StencilTwoSided
   /usr/include/osg/Switch
   /usr/include/osg/TemplatePrimitiveFunctor
   /usr/include/osg/TemplatePrimitiveIndexFunctor
   /usr/include/osg/TexEnv
   /usr/include/osg/TexEnvCombine
   /usr/include/osg/TexEnvFilter
   /usr/include/osg/TexGen
   /usr/include/osg/TexGenNode
   /usr/include/osg/TexMat
   /usr/include/osg/Texture
   /usr/include/osg/Texture1D
   /usr/include/osg/Texture2D
   /usr/include/osg/Texture2DArray
   /usr/include/osg/Texture2DMultisample
   /usr/include/osg/Texture3D
   /usr/include/osg/TextureBuffer
   /usr/include/osg/TextureCubeMap
   /usr/include/osg/TextureRectangle
   /usr/include/osg/Timer
   /usr/include/osg/TransferFunction
   /usr/include/osg/Transform
   /usr/include/osg/TriangleFunctor
   /usr/include/osg/TriangleIndexFunctor
   /usr/include/osg/TriangleLinePointIndexFunctor
   /usr/include/osg/Types
   /usr/include/osg/Uniform
   /usr/include/osg/UserDataContainer
   /usr/include/osg/ValueMap
   /usr/include/osg/ValueObject
   /usr/include/osg/ValueStack
   /usr/include/osg/Vec2
   /usr/include/osg/Vec2b
   /usr/include/osg/Vec2d
   /usr/include/osg/Vec2f
   /usr/include/osg/Vec2i
   /usr/include/osg/Vec2s
   /usr/include/osg/Vec2ub
   /usr/include/osg/Vec2ui
   /usr/include/osg/Vec2us
   /usr/include/osg/Vec3
   /usr/include/osg/Vec3b
   /usr/include/osg/Vec3d
   /usr/include/osg/Vec3f
   /usr/include/osg/Vec3i
   /usr/include/osg/Vec3s
   /usr/include/osg/Vec3ub
   /usr/include/osg/Vec3ui
   /usr/include/osg/Vec3us
   /usr/include/osg/Vec4
   /usr/include/osg/Vec4b
   /usr/include/osg/Vec4d
   /usr/include/osg/Vec4f
   /usr/include/osg/Vec4i
   /usr/include/osg/Vec4s
   /usr/include/osg/Vec4ub
   /usr/include/osg/Vec4ui
   /usr/include/osg/Vec4us
   /usr/include/osg/Version
   /usr/include/osg/VertexArrayState
   /usr/include/osg/VertexAttribDivisor
   /usr/include/osg/VertexProgram
   /usr/include/osg/View
   /usr/include/osg/Viewport
   /usr/include/osg/ViewportIndexed
   /usr/include/osg/buffered_value
   /usr/include/osg/fast_back_stack
   /usr/include/osg/io_utils
   /usr/include/osg/observer_ptr
   /usr/include/osg/os_utils
   /usr/include/osg/ref_ptr
   /usr/include/osgAnimation/Action
   /usr/include/osgAnimation/ActionAnimation
   /usr/include/osgAnimation/ActionBlendIn
   /usr/include/osgAnimation/ActionBlendOut
   /usr/include/osgAnimation/ActionCallback
   /usr/include/osgAnimation/ActionStripAnimation
   /usr/include/osgAnimation/ActionVisitor
   /usr/include/osgAnimation/Animation
   /usr/include/osgAnimation/AnimationManagerBase
   /usr/include/osgAnimation/AnimationUpdateCallback
   /usr/include/osgAnimation/BasicAnimationManager
   /usr/include/osgAnimation/Bone
   /usr/include/osgAnimation/BoneMapVisitor
   /usr/include/osgAnimation/Channel
   /usr/include/osgAnimation/CubicBezier
   /usr/include/osgAnimation/EaseMotion
   /usr/include/osgAnimation/Export
   /usr/include/osgAnimation/FrameAction
   /usr/include/osgAnimation/Interpolator
   /usr/include/osgAnimation/Keyframe
   /usr/include/osgAnimation/LinkVisitor
   /usr/include/osgAnimation/MorphGeometry
   /usr/include/osgAnimation/MorphTransformHardware
   /usr/include/osgAnimation/MorphTransformSoftware
   /usr/include/osgAnimation/RigGeometry
   /usr/include/osgAnimation/RigTransform
   /usr/include/osgAnimation/RigTransformHardware
   /usr/include/osgAnimation/RigTransformSoftware
   /usr/include/osgAnimation/Sampler
   /usr/include/osgAnimation/Skeleton
   /usr/include/osgAnimation/StackedMatrixElement
   /usr/include/osgAnimation/StackedQuaternionElement
   /usr/include/osgAnimation/StackedRotateAxisElement
   /usr/include/osgAnimation/StackedScaleElement
   /usr/include/osgAnimation/StackedTransform
   /usr/include/osgAnimation/StackedTransformElement
   /usr/include/osgAnimation/StackedTranslateElement
   /usr/include/osgAnimation/StatsHandler
   /usr/include/osgAnimation/StatsVisitor
   /usr/include/osgAnimation/Target
   /usr/include/osgAnimation/Timeline
   /usr/include/osgAnimation/TimelineAnimationManager
   /usr/include/osgAnimation/UpdateBone
   /usr/include/osgAnimation/UpdateMaterial
   /usr/include/osgAnimation/UpdateMatrixTransform
   /usr/include/osgAnimation/UpdateUniform
   /usr/include/osgAnimation/Vec3Packed
   /usr/include/osgAnimation/VertexInfluence
   /usr/include/osgDB/Archive
   /usr/include/osgDB/AuthenticationMap
   /usr/include/osgDB/Callbacks
   /usr/include/osgDB/ClassInterface
   /usr/include/osgDB/ConvertBase64
   /usr/include/osgDB/ConvertUTF
   /usr/include/osgDB/DataTypes
   /usr/include/osgDB/DatabasePager
   /usr/include/osgDB/DatabaseRevisions
   /usr/include/osgDB/DotOsgWrapper
   /usr/include/osgDB/DynamicLibrary
   /usr/include/osgDB/Export
   /usr/include/osgDB/ExternalFileWriter
   /usr/include/osgDB/FileCache
   /usr/include/osgDB/FileNameUtils
   /usr/include/osgDB/FileUtils
   /usr/include/osgDB/ImageOptions
   /usr/include/osgDB/ImagePager
   /usr/include/osgDB/ImageProcessor
   /usr/include/osgDB/Input
   /usr/include/osgDB/InputStream
   /usr/include/osgDB/ObjectCache
   /usr/include/osgDB/ObjectWrapper
   /usr/include/osgDB/Options
   /usr/include/osgDB/Output
   /usr/include/osgDB/OutputStream
   /usr/include/osgDB/ParameterOutput
   /usr/include/osgDB/PluginQuery
   /usr/include/osgDB/ReadFile
   /usr/include/osgDB/ReaderWriter
   /usr/include/osgDB/Registry
   /usr/include/osgDB/Serializer
   /usr/include/osgDB/SharedStateManager
   /usr/include/osgDB/StreamOperator
   /usr/include/osgDB/Version
   /usr/include/osgDB/WriteFile
   /usr/include/osgDB/XmlParser
   /usr/include/osgDB/fstream
   /usr/include/osgFX/AnisotropicLighting
   /usr/include/osgFX/BumpMapping
   /usr/include/osgFX/Cartoon
   /usr/include/osgFX/Effect
   /usr/include/osgFX/Export
   /usr/include/osgFX/MultiTextureControl
   /usr/include/osgFX/Outline
   /usr/include/osgFX/Registry
   /usr/include/osgFX/Scribe
   /usr/include/osgFX/SpecularHighlights
   /usr/include/osgFX/Technique
   /usr/include/osgFX/Validator
   /usr/include/osgFX/Version
   /usr/include/osgGA/AnimationPathManipulator
   /usr/include/osgGA/CameraManipulator
   /usr/include/osgGA/CameraViewSwitchManipulator
   /usr/include/osgGA/Device
   /usr/include/osgGA/DriveManipulator
   /usr/include/osgGA/Event
   /usr/include/osgGA/EventHandler
   /usr/include/osgGA/EventQueue
   /usr/include/osgGA/EventVisitor
   /usr/include/osgGA/Export
   /usr/include/osgGA/FirstPersonManipulator
   /usr/include/osgGA/FlightManipulator
   /usr/include/osgGA/GUIActionAdapter
   /usr/include/osgGA/GUIEventAdapter
   /usr/include/osgGA/GUIEventHandler
   /usr/include/osgGA/KeySwitchMatrixManipulator
   /usr/include/osgGA/MultiTouchTrackballManipulator
   /usr/include/osgGA/NodeTrackerManipulator
   /usr/include/osgGA/OrbitManipulator
   /usr/include/osgGA/SphericalManipulator
   /usr/include/osgGA/StandardManipulator
   /usr/include/osgGA/StateSetManipulator
   /usr/include/osgGA/TerrainManipulator
   /usr/include/osgGA/TrackballManipulator
   /usr/include/osgGA/UFOManipulator
   /usr/include/osgGA/Version
   /usr/include/osgGA/Widget
   /usr/include/osgManipulator/AntiSquish
   /usr/include/osgManipulator/Command
   /usr/include/osgManipulator/CommandManager
   /usr/include/osgManipulator/Constraint
   /usr/include/osgManipulator/Dragger
   /usr/include/osgManipulator/Export
   /usr/include/osgManipulator/Projector
   /usr/include/osgManipulator/RotateCylinderDragger
   /usr/include/osgManipulator/RotateSphereDragger
   /usr/include/osgManipulator/Scale1DDragger
   /usr/include/osgManipulator/Scale2DDragger
   /usr/include/osgManipulator/ScaleAxisDragger
   /usr/include/osgManipulator/Selection
   /usr/include/osgManipulator/TabBoxDragger
   /usr/include/osgManipulator/TabBoxTrackballDragger
   /usr/include/osgManipulator/TabPlaneDragger
   /usr/include/osgManipulator/TabPlaneTrackballDragger
   /usr/include/osgManipulator/TrackballDragger
   /usr/include/osgManipulator/Translate1DDragger
   /usr/include/osgManipulator/Translate2DDragger
   /usr/include/osgManipulator/TranslateAxisDragger
   /usr/include/osgManipulator/TranslatePlaneDragger
   /usr/include/osgManipulator/Version
   /usr/include/osgParticle/AccelOperator
   /usr/include/osgParticle/AngularAccelOperator
   /usr/include/osgParticle/AngularDampingOperator
   /usr/include/osgParticle/BounceOperator
   /usr/include/osgParticle/BoxPlacer
   /usr/include/osgParticle/CenteredPlacer
   /usr/include/osgParticle/CompositePlacer
   /usr/include/osgParticle/ConnectedParticleSystem
   /usr/include/osgParticle/ConstantRateCounter
   /usr/include/osgParticle/Counter
   /usr/include/osgParticle/DampingOperator
   /usr/include/osgParticle/DomainOperator
   /usr/include/osgParticle/Emitter
   /usr/include/osgParticle/ExplosionDebrisEffect
   /usr/include/osgParticle/ExplosionEffect
   /usr/include/osgParticle/ExplosionOperator
   /usr/include/osgParticle/Export
   /usr/include/osgParticle/FireEffect
   /usr/include/osgParticle/FluidFrictionOperator
   /usr/include/osgParticle/FluidProgram
   /usr/include/osgParticle/ForceOperator
   /usr/include/osgParticle/Interpolator
   /usr/include/osgParticle/LinearInterpolator
   /usr/include/osgParticle/ModularEmitter
   /usr/include/osgParticle/ModularProgram
   /usr/include/osgParticle/MultiSegmentPlacer
   /usr/include/osgParticle/Operator
   /usr/include/osgParticle/OrbitOperator
   /usr/include/osgParticle/Particle
   /usr/include/osgParticle/ParticleEffect
   /usr/include/osgParticle/ParticleProcessor
   /usr/include/osgParticle/ParticleSystem
   /usr/include/osgParticle/ParticleSystemUpdater
   /usr/include/osgParticle/Placer
   /usr/include/osgParticle/PointPlacer
   /usr/include/osgParticle/PrecipitationEffect
   /usr/include/osgParticle/Program
   /usr/include/osgParticle/RadialShooter
   /usr/include/osgParticle/RandomRateCounter
   /usr/include/osgParticle/SectorPlacer
   /usr/include/osgParticle/SegmentPlacer
   /usr/include/osgParticle/Shooter
   /usr/include/osgParticle/SinkOperator
   /usr/include/osgParticle/SmokeEffect
   /usr/include/osgParticle/SmokeTrailEffect
   /usr/include/osgParticle/VariableRateCounter
   /usr/include/osgParticle/Version
   /usr/include/osgParticle/range
   /usr/include/osgPresentation/AnimationMaterial
   /usr/include/osgPresentation/CompileSlideCallback
   /usr/include/osgPresentation/Cursor
   /usr/include/osgPresentation/Export
   /usr/include/osgPresentation/KeyEventHandler
   /usr/include/osgPresentation/PickEventHandler
   /usr/include/osgPresentation/PropertyManager
   /usr/include/osgPresentation/SlideEventHandler
   /usr/include/osgPresentation/SlideShowConstructor
   /usr/include/osgPresentation/Timeout
   /usr/include/osgShadow/ConvexPolyhedron
   /usr/include/osgShadow/DebugShadowMap
   /usr/include/osgShadow/Export
   /usr/include/osgShadow/LightSpacePerspectiveShadowMap
   /usr/include/osgShadow/MinimalCullBoundsShadowMap
   /usr/include/osgShadow/MinimalDrawBoundsShadowMap
   /usr/include/osgShadow/MinimalShadowMap
   /usr/include/osgShadow/ParallelSplitShadowMap
   /usr/include/osgShadow/ProjectionShadowMap
   /usr/include/osgShadow/ShadowMap
   /usr/include/osgShadow/ShadowSettings
   /usr/include/osgShadow/ShadowTechnique
   /usr/include/osgShadow/ShadowTexture
   /usr/include/osgShadow/ShadowedScene
   /usr/include/osgShadow/SoftShadowMap
   /usr/include/osgShadow/StandardShadowMap
   /usr/include/osgShadow/Version
   /usr/include/osgShadow/ViewDependentShadowMap
   /usr/include/osgShadow/ViewDependentShadowTechnique
   /usr/include/osgSim/BlinkSequence
   /usr/include/osgSim/ColorRange
   /usr/include/osgSim/DOFTransform
   /usr/include/osgSim/ElevationSlice
   /usr/include/osgSim/Export
   /usr/include/osgSim/GeographicLocation
   /usr/include/osgSim/HeightAboveTerrain
   /usr/include/osgSim/Impostor
   /usr/include/osgSim/ImpostorSprite
   /usr/include/osgSim/InsertImpostorsVisitor
   /usr/include/osgSim/LightPoint
   /usr/include/osgSim/LightPointNode
   /usr/include/osgSim/LightPointSystem
   /usr/include/osgSim/LineOfSight
   /usr/include/osgSim/MultiSwitch
   /usr/include/osgSim/ObjectRecordData
   /usr/include/osgSim/OverlayNode
   /usr/include/osgSim/ScalarBar
   /usr/include/osgSim/ScalarsToColors
   /usr/include/osgSim/Sector
   /usr/include/osgSim/ShapeAttribute
   /usr/include/osgSim/SphereSegment
   /usr/include/osgSim/Version
   /usr/include/osgSim/VisibilityGroup
   /usr/include/osgTerrain/DisplacementMappingTechnique
   /usr/include/osgTerrain/Export
   /usr/include/osgTerrain/GeometryPool
   /usr/include/osgTerrain/GeometryTechnique
   /usr/include/osgTerrain/Layer
   /usr/include/osgTerrain/Locator
   /usr/include/osgTerrain/Terrain
   /usr/include/osgTerrain/TerrainTechnique
   /usr/include/osgTerrain/TerrainTile
   /usr/include/osgTerrain/ValidDataOperator
   /usr/include/osgTerrain/Version
   /usr/include/osgText/Export
   /usr/include/osgText/FadeText
   /usr/include/osgText/Font
   /usr/include/osgText/Font3D
   /usr/include/osgText/Glyph
   /usr/include/osgText/KerningType
   /usr/include/osgText/String
   /usr/include/osgText/Style
   /usr/include/osgText/Text
   /usr/include/osgText/Text3D
   /usr/include/osgText/TextBase
   /usr/include/osgText/Version
   /usr/include/osgUI/AlignmentSettings
   /usr/include/osgUI/Callbacks
   /usr/include/osgUI/ColorPalette
   /usr/include/osgUI/ComboBox
   /usr/include/osgUI/Dialog
   /usr/include/osgUI/Export
   /usr/include/osgUI/FrameSettings
   /usr/include/osgUI/Label
   /usr/include/osgUI/LineEdit
   /usr/include/osgUI/Popup
   /usr/include/osgUI/PushButton
   /usr/include/osgUI/Style
   /usr/include/osgUI/TabWidget
   /usr/include/osgUI/TextSettings
   /usr/include/osgUI/Validator
   /usr/include/osgUI/Widget
   /usr/include/osgUtil/ConvertVec
   /usr/include/osgUtil/CubeMapGenerator
   /usr/include/osgUtil/CullVisitor
   /usr/include/osgUtil/DelaunayTriangulator
   /usr/include/osgUtil/DisplayRequirementsVisitor
   /usr/include/osgUtil/DrawElementTypeSimplifier
   /usr/include/osgUtil/EdgeCollector
   /usr/include/osgUtil/Export
   /usr/include/osgUtil/GLObjectsVisitor
   /usr/include/osgUtil/HalfWayMapGenerator
   /usr/include/osgUtil/HighlightMapGenerator
   /usr/include/osgUtil/IncrementalCompileOperation
   /usr/include/osgUtil/IntersectVisitor
   /usr/include/osgUtil/IntersectionVisitor
   /usr/include/osgUtil/LineSegmentIntersector
   /usr/include/osgUtil/MeshOptimizers
   /usr/include/osgUtil/OperationArrayFunctor
   /usr/include/osgUtil/Optimizer
   /usr/include/osgUtil/PerlinNoise
   /usr/include/osgUtil/PlaneIntersector
   /usr/include/osgUtil/PolytopeIntersector
   /usr/include/osgUtil/PositionalStateContainer
   /usr/include/osgUtil/PrintVisitor
   /usr/include/osgUtil/RayIntersector
   /usr/include/osgUtil/ReflectionMapGenerator
   /usr/include/osgUtil/RenderBin
   /usr/include/osgUtil/RenderLeaf
   /usr/include/osgUtil/RenderStage
   /usr/include/osgUtil/ReversePrimitiveFunctor
   /usr/include/osgUtil/SceneGraphBuilder
   /usr/include/osgUtil/SceneView
   /usr/include/osgUtil/ShaderGen
   /usr/include/osgUtil/Simplifier
   /usr/include/osgUtil/SmoothingVisitor
   /usr/include/osgUtil/StateGraph
   /usr/include/osgUtil/Statistics
   /usr/include/osgUtil/TangentSpaceGenerator
   /usr/include/osgUtil/Tessellator
   /usr/include/osgUtil/TransformAttributeFunctor
   /usr/include/osgUtil/TransformCallback
   /usr/include/osgUtil/TriStripVisitor
   /usr/include/osgUtil/UpdateVisitor
   /usr/include/osgUtil/Version
   /usr/include/osgViewer/CompositeViewer
   /usr/include/osgViewer/Export
   /usr/include/osgViewer/GraphicsWindow
   /usr/include/osgViewer/Keystone
   /usr/include/osgViewer/Renderer
   /usr/include/osgViewer/Scene
   /usr/include/osgViewer/Version
   /usr/include/osgViewer/View
   /usr/include/osgViewer/Viewer
   /usr/include/osgViewer/ViewerBase
   /usr/include/osgViewer/ViewerEventHandlers
   /usr/include/osgViewer/api/X11/GraphicsHandleX11
   /usr/include/osgViewer/api/X11/GraphicsWindowX11
   /usr/include/osgViewer/api/X11/PixelBufferX11
   /usr/include/osgViewer/config/AcrossAllScreens
   /usr/include/osgViewer/config/PanoramicSphericalDisplay
   /usr/include/osgViewer/config/SingleScreen
   /usr/include/osgViewer/config/SingleWindow
   /usr/include/osgViewer/config/SphericalDisplay
   /usr/include/osgViewer/config/WoWVxDisplay
   /usr/include/osgVolume/Export
   /usr/include/osgVolume/FixedFunctionTechnique
   /usr/include/osgVolume/Layer
   /usr/include/osgVolume/Locator
   /usr/include/osgVolume/MultipassTechnique
   /usr/include/osgVolume/Property
   /usr/include/osgVolume/RayTracedTechnique
   /usr/include/osgVolume/Version
   /usr/include/osgVolume/Volume
   /usr/include/osgVolume/VolumeScene
   /usr/include/osgVolume/VolumeSettings
   /usr/include/osgVolume/VolumeTechnique
   /usr/include/osgVolume/VolumeTile
   /usr/include/osgWidget/Box
   /usr/include/osgWidget/Browser
   /usr/include/osgWidget/Canvas
   /usr/include/osgWidget/EventInterface
   /usr/include/osgWidget/Export
   /usr/include/osgWidget/Frame
   /usr/include/osgWidget/Input
   /usr/include/osgWidget/Label
   /usr/include/osgWidget/Lua
   /usr/include/osgWidget/PdfReader
   /usr/include/osgWidget/Python
   /usr/include/osgWidget/ScriptEngine
   /usr/include/osgWidget/StyleInterface
   /usr/include/osgWidget/StyleManager
   /usr/include/osgWidget/Table
   /usr/include/osgWidget/Types
   /usr/include/osgWidget/UIObjectParent
   /usr/include/osgWidget/Util
   /usr/include/osgWidget/Version
   /usr/include/osgWidget/ViewerEventHandlers
   /usr/include/osgWidget/VncClient
   /usr/include/osgWidget/Widget
   /usr/include/osgWidget/Window
   /usr/include/osgWidget/WindowManager
   /usr/lib64/libOpenThreads.so
   /usr/lib64/libOpenThreads.so.21
   /usr/lib64/libOpenThreads.so.3.3.1
   /usr/lib64/libosg.so
   /usr/lib64/libosg.so.158
   /usr/lib64/libosg.so.3.6.3
   /usr/lib64/libosgAnimation.so
   /usr/lib64/libosgAnimation.so.158
   /usr/lib64/libosgAnimation.so.3.6.3
   /usr/lib64/libosgDB.so
   /usr/lib64/libosgDB.so.158
   /usr/lib64/libosgDB.so.3.6.3
   /usr/lib64/libosgFX.so
   /usr/lib64/libosgFX.so.158
   /usr/lib64/libosgFX.so.3.6.3
   /usr/lib64/libosgGA.so
   /usr/lib64/libosgGA.so.158
   /usr/lib64/libosgGA.so.3.6.3
   /usr/lib64/libosgManipulator.so
   /usr/lib64/libosgManipulator.so.158
   /usr/lib64/libosgManipulator.so.3.6.3
   /usr/lib64/libosgParticle.so
   /usr/lib64/libosgParticle.so.158
   /usr/lib64/libosgParticle.so.3.6.3
   /usr/lib64/libosgPresentation.so
   /usr/lib64/libosgPresentation.so.158
   /usr/lib64/libosgPresentation.so.3.6.3
   /usr/lib64/libosgShadow.so
   /usr/lib64/libosgShadow.so.158
   /usr/lib64/libosgShadow.so.3.6.3
   /usr/lib64/libosgSim.so
   /usr/lib64/libosgSim.so.158
   /usr/lib64/libosgSim.so.3.6.3
   /usr/lib64/libosgTerrain.so
   /usr/lib64/libosgTerrain.so.158
   /usr/lib64/libosgTerrain.so.3.6.3
   /usr/lib64/libosgText.so
   /usr/lib64/libosgText.so.158
   /usr/lib64/libosgText.so.3.6.3
   /usr/lib64/libosgUI.so
   /usr/lib64/libosgUI.so.158
   /usr/lib64/libosgUI.so.3.6.3
   /usr/lib64/libosgUtil.so
   /usr/lib64/libosgUtil.so.158
   /usr/lib64/libosgUtil.so.3.6.3
   /usr/lib64/libosgViewer.so
   /usr/lib64/libosgViewer.so.158
   /usr/lib64/libosgViewer.so.3.6.3
   /usr/lib64/libosgVolume.so
   /usr/lib64/libosgVolume.so.158
   /usr/lib64/libosgVolume.so.3.6.3
   /usr/lib64/libosgWidget.so
   /usr/lib64/libosgWidget.so.158
   /usr/lib64/libosgWidget.so.3.6.3
   /usr/lib64/osgPlugins-3.6.3/osgdb_3dc.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_3ds.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_ac.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_bmp.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_bsp.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_bvh.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_cfg.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_curl.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_dae.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_dds.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_deprecated_osg.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_deprecated_osganimation.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_deprecated_osgfx.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_deprecated_osgparticle.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_deprecated_osgshadow.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_deprecated_osgsim.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_deprecated_osgterrain.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_deprecated_osgtext.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_deprecated_osgviewer.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_deprecated_osgvolume.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_deprecated_osgwidget.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_dot.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_dxf.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_ffmpeg.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_freetype.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_gdal.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_gif.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_gles.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_glsl.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_gz.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_hdr.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_ive.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_jp2.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_jpeg.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_ktx.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_las.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_logo.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_lua.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_lwo.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_lws.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_md2.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_mdl.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_normals.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_obj.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_ogr.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_openflight.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_osc.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_osg.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_osga.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_osgjs.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_osgshadow.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_osgterrain.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_osgtgz.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_osgviewer.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_p3d.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_pic.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_ply.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_png.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_pnm.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_pov.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_pvr.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_revisions.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_rgb.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_rot.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_scale.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osg.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osganimation.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osgfx.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osgga.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osgmanipulator.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osgparticle.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osgshadow.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osgsim.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osgterrain.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osgtext.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osgui.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osgutil.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osgviewer.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_serializers_osgvolume.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_shp.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_stl.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_tf.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_tga.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_tgz.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_tiff.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_trans.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_trk.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_txf.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_txp.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_vtf.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_x.so
   /usr/lib64/osgPlugins-3.6.3/osgdb_zip.so
   /usr/lib64/pkgconfig/openscenegraph-osg.pc
   /usr/lib64/pkgconfig/openscenegraph-osgAnimation.pc
   /usr/lib64/pkgconfig/openscenegraph-osgDB.pc
   /usr/lib64/pkgconfig/openscenegraph-osgFX.pc
   /usr/lib64/pkgconfig/openscenegraph-osgGA.pc
   /usr/lib64/pkgconfig/openscenegraph-osgManipulator.pc
   /usr/lib64/pkgconfig/openscenegraph-osgParticle.pc
   /usr/lib64/pkgconfig/openscenegraph-osgShadow.pc
   /usr/lib64/pkgconfig/openscenegraph-osgSim.pc
   /usr/lib64/pkgconfig/openscenegraph-osgTerrain.pc
   /usr/lib64/pkgconfig/openscenegraph-osgText.pc
   /usr/lib64/pkgconfig/openscenegraph-osgUtil.pc
   /usr/lib64/pkgconfig/openscenegraph-osgViewer.pc
   /usr/lib64/pkgconfig/openscenegraph-osgVolume.pc
   /usr/lib64/pkgconfig/openscenegraph-osgWidget.pc
   /usr/lib64/pkgconfig/openscenegraph.pc
   /usr/lib64/pkgconfig/openthreads.pc
   /usr/share/OpenSceneGraph/bin/osgSSBO
   /usr/share/OpenSceneGraph/bin/osganalysis
   /usr/share/OpenSceneGraph/bin/osganimate
   /usr/share/OpenSceneGraph/bin/osganimationeasemotion
   /usr/share/OpenSceneGraph/bin/osganimationhardware
   /usr/share/OpenSceneGraph/bin/osganimationmakepath
   /usr/share/OpenSceneGraph/bin/osganimationmorph
   /usr/share/OpenSceneGraph/bin/osganimationnode
   /usr/share/OpenSceneGraph/bin/osganimationskinning
   /usr/share/OpenSceneGraph/bin/osganimationsolid
   /usr/share/OpenSceneGraph/bin/osganimationtimeline
   /usr/share/OpenSceneGraph/bin/osganimationviewer
   /usr/share/OpenSceneGraph/bin/osgatomiccounter
   /usr/share/OpenSceneGraph/bin/osgautocapture
   /usr/share/OpenSceneGraph/bin/osgautotransform
   /usr/share/OpenSceneGraph/bin/osgbillboard
   /usr/share/OpenSceneGraph/bin/osgbindlesstext
   /usr/share/OpenSceneGraph/bin/osgblenddrawbuffers
   /usr/share/OpenSceneGraph/bin/osgblendequation
   /usr/share/OpenSceneGraph/bin/osgcallback
   /usr/share/OpenSceneGraph/bin/osgcamera
   /usr/share/OpenSceneGraph/bin/osgcatch
   /usr/share/OpenSceneGraph/bin/osgclip
   /usr/share/OpenSceneGraph/bin/osgcluster
   /usr/share/OpenSceneGraph/bin/osgcompositeviewer
   /usr/share/OpenSceneGraph/bin/osgcomputeshaders
   /usr/share/OpenSceneGraph/bin/osgcopy
   /usr/share/OpenSceneGraph/bin/osgcubemap
   /usr/share/OpenSceneGraph/bin/osgdatabaserevisions
   /usr/share/OpenSceneGraph/bin/osgdeferred
   /usr/share/OpenSceneGraph/bin/osgdepthpartition
   /usr/share/OpenSceneGraph/bin/osgdepthpeeling
   /usr/share/OpenSceneGraph/bin/osgdistortion
   /usr/share/OpenSceneGraph/bin/osgdrawinstanced
   /usr/share/OpenSceneGraph/bin/osgfadetext
   /usr/share/OpenSceneGraph/bin/osgfont
   /usr/share/OpenSceneGraph/bin/osgforest
   /usr/share/OpenSceneGraph/bin/osgfpdepth
   /usr/share/OpenSceneGraph/bin/osgfxbrowser
   /usr/share/OpenSceneGraph/bin/osggameoflife
   /usr/share/OpenSceneGraph/bin/osggeometry
   /usr/share/OpenSceneGraph/bin/osggeometryshaders
   /usr/share/OpenSceneGraph/bin/osggpucull
   /usr/share/OpenSceneGraph/bin/osggpx
   /usr/share/OpenSceneGraph/bin/osggraphicscost
   /usr/share/OpenSceneGraph/bin/osghangglide
   /usr/share/OpenSceneGraph/bin/osghud
   /usr/share/OpenSceneGraph/bin/osgimagesequence
   /usr/share/OpenSceneGraph/bin/osgimpostor
   /usr/share/OpenSceneGraph/bin/osgintersection
   /usr/share/OpenSceneGraph/bin/osgkdtree
   /usr/share/OpenSceneGraph/bin/osgkeyboard
   /usr/share/OpenSceneGraph/bin/osgkeyboardmouse
   /usr/share/OpenSceneGraph/bin/osgkeystone
   /usr/share/OpenSceneGraph/bin/osglauncher
   /usr/share/OpenSceneGraph/bin/osglight
   /usr/share/OpenSceneGraph/bin/osglightpoint
   /usr/share/OpenSceneGraph/bin/osglogicop
   /usr/share/OpenSceneGraph/bin/osglogo
   /usr/share/OpenSceneGraph/bin/osgmanipulator
   /usr/share/OpenSceneGraph/bin/osgmemorytest
   /usr/share/OpenSceneGraph/bin/osgmotionblur
   /usr/share/OpenSceneGraph/bin/osgmovie
   /usr/share/OpenSceneGraph/bin/osgmultiplemovies
   /usr/share/OpenSceneGraph/bin/osgmultiplerendertargets
   /usr/share/OpenSceneGraph/bin/osgmultitexture
   /usr/share/OpenSceneGraph/bin/osgmultitexturecontrol
   /usr/share/OpenSceneGraph/bin/osgmultitouch
   /usr/share/OpenSceneGraph/bin/osgmultiviewpaging
   /usr/share/OpenSceneGraph/bin/osgobjectcache
   /usr/share/OpenSceneGraph/bin/osgoccluder
   /usr/share/OpenSceneGraph/bin/osgocclusionquery
   /usr/share/OpenSceneGraph/bin/osgoit
   /usr/share/OpenSceneGraph/bin/osgoscdevice
   /usr/share/OpenSceneGraph/bin/osgoutline
   /usr/share/OpenSceneGraph/bin/osgpackeddepthstencil
   /usr/share/OpenSceneGraph/bin/osgpagedlod
   /usr/share/OpenSceneGraph/bin/osgparametric
   /usr/share/OpenSceneGraph/bin/osgparticle
   /usr/share/OpenSceneGraph/bin/osgparticleeffects
   /usr/share/OpenSceneGraph/bin/osgparticleshader
   /usr/share/OpenSceneGraph/bin/osgpdf
   /usr/share/OpenSceneGraph/bin/osgphotoalbum
   /usr/share/OpenSceneGraph/bin/osgpick
   /usr/share/OpenSceneGraph/bin/osgplanets
   /usr/share/OpenSceneGraph/bin/osgpoints
   /usr/share/OpenSceneGraph/bin/osgpointsprite
   /usr/share/OpenSceneGraph/bin/osgposter
   /usr/share/OpenSceneGraph/bin/osgprecipitation
   /usr/share/OpenSceneGraph/bin/osgprerender
   /usr/share/OpenSceneGraph/bin/osgprerendercubemap
   /usr/share/OpenSceneGraph/bin/osgreflect
   /usr/share/OpenSceneGraph/bin/osgrobot
   /usr/share/OpenSceneGraph/bin/osgsampler
   /usr/share/OpenSceneGraph/bin/osgscalarbar
   /usr/share/OpenSceneGraph/bin/osgscreencapture
   /usr/share/OpenSceneGraph/bin/osgscribe
   /usr/share/OpenSceneGraph/bin/osgsequence
   /usr/share/OpenSceneGraph/bin/osgshadercomposition
   /usr/share/OpenSceneGraph/bin/osgshadergen
   /usr/share/OpenSceneGraph/bin/osgshadermultiviewport
   /usr/share/OpenSceneGraph/bin/osgshaders
   /usr/share/OpenSceneGraph/bin/osgshaderterrain
   /usr/share/OpenSceneGraph/bin/osgshadow
   /usr/share/OpenSceneGraph/bin/osgshape
   /usr/share/OpenSceneGraph/bin/osgsharedarray
   /usr/share/OpenSceneGraph/bin/osgsidebyside
   /usr/share/OpenSceneGraph/bin/osgsimpleMDI
   /usr/share/OpenSceneGraph/bin/osgsimplegl3
   /usr/share/OpenSceneGraph/bin/osgsimpleshaders
   /usr/share/OpenSceneGraph/bin/osgsimplifier
   /usr/share/OpenSceneGraph/bin/osgsimulation
   /usr/share/OpenSceneGraph/bin/osgslice
   /usr/share/OpenSceneGraph/bin/osgspacewarp
   /usr/share/OpenSceneGraph/bin/osgspheresegment
   /usr/share/OpenSceneGraph/bin/osgspotlight
   /usr/share/OpenSceneGraph/bin/osgstereoimage
   /usr/share/OpenSceneGraph/bin/osgstereomatch
   /usr/share/OpenSceneGraph/bin/osgteapot
   /usr/share/OpenSceneGraph/bin/osgterrain
   /usr/share/OpenSceneGraph/bin/osgtessellate
   /usr/share/OpenSceneGraph/bin/osgtessellationshaders
   /usr/share/OpenSceneGraph/bin/osgtext
   /usr/share/OpenSceneGraph/bin/osgtext3D
   /usr/share/OpenSceneGraph/bin/osgtexture1D
   /usr/share/OpenSceneGraph/bin/osgtexture2D
   /usr/share/OpenSceneGraph/bin/osgtexture2DArray
   /usr/share/OpenSceneGraph/bin/osgtexture3D
   /usr/share/OpenSceneGraph/bin/osgtexturecompression
   /usr/share/OpenSceneGraph/bin/osgtexturerectangle
   /usr/share/OpenSceneGraph/bin/osgthirdpersonview
   /usr/share/OpenSceneGraph/bin/osgthreadedterrain
   /usr/share/OpenSceneGraph/bin/osgtransferfunction
   /usr/share/OpenSceneGraph/bin/osgtransformfeedback
   /usr/share/OpenSceneGraph/bin/osguniformbuffer
   /usr/share/OpenSceneGraph/bin/osgunittests
   /usr/share/OpenSceneGraph/bin/osguserdata
   /usr/share/OpenSceneGraph/bin/osguserstats
   /usr/share/OpenSceneGraph/bin/osgvertexattributes
   /usr/share/OpenSceneGraph/bin/osgvertexprogram
   /usr/share/OpenSceneGraph/bin/osgvirtualprogram
   /usr/share/OpenSceneGraph/bin/osgvolume
   /usr/share/OpenSceneGraph/bin/osgwidgetaddremove
   /usr/share/OpenSceneGraph/bin/osgwidgetbox
   /usr/share/OpenSceneGraph/bin/osgwidgetcanvas
   /usr/share/OpenSceneGraph/bin/osgwidgetframe
   /usr/share/OpenSceneGraph/bin/osgwidgetinput
   /usr/share/OpenSceneGraph/bin/osgwidgetlabel
   /usr/share/OpenSceneGraph/bin/osgwidgetmenu
   /usr/share/OpenSceneGraph/bin/osgwidgetmessagebox
   /usr/share/OpenSceneGraph/bin/osgwidgetnotebook
   /usr/share/OpenSceneGraph/bin/osgwidgetperformance
   /usr/share/OpenSceneGraph/bin/osgwidgetscrolled
   /usr/share/OpenSceneGraph/bin/osgwidgetshader
   /usr/share/OpenSceneGraph/bin/osgwidgetstyled
   /usr/share/OpenSceneGraph/bin/osgwidgettable
   /usr/share/OpenSceneGraph/bin/osgwidgetwindow
   /usr/share/OpenSceneGraph/bin/osgwindows


%changelog
* Tue Jun 25 2019 Yngve Einarsson <Yngve.Einarsson@smhi.se>
- Update to official release 3.6.3 
* Fri Apr 13 2018 Yngve Einarsson <Yngve.Einarsson@smhi.se>
- Update to official release 3.6.0 
* Mon Mar 26 2018 Yngve Einarsson <Yngve.Einarsson@smhi.se>
- Update to version 3.7.0 
* Thu Apr 6 2017 Yngve Einarsson <Yngve.Einarsson@smhi.se>
- Initial build.
- Include files added.
- Update from master
