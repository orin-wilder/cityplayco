# Tabletop AR demo

Public route: `/ar/`. Standalone static page; no backend or signup.

The original brass key is approximately 18 cm long, stored in metres in a 115 KB GLB. Regenerate it with `python tools/build-ar-key.py`. Model-viewer 4.1.0 is pinned on jsDelivr. iOS Quick Look generates its USDZ from the GLB automatically; Android uses WebXR or Scene Viewer when supported. Unsupported devices retain the interactive 3D preview. HTTPS is required for deployed AR.

Validation: glTF validator reports zero errors and warnings; JavaScript syntax checked; local HTTP route and assets checked. Physical AR placement has not been verified on a real device. Before presenting, open the live page in Safari on an AR-capable iPhone and Chrome on an AR-capable Android, launch AR, place the key on a well-lit table, and return to the page. Also check the preview on a desktop.
