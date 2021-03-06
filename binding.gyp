{
  "targets": [
    {
      "target_name": "<(module_name)",
      "sources": [ "./src/gdi.cc" ],
      "libraries": [ "Gdiplus.lib", "Shlwapi.lib", "Shcore.lib"],
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
  # "targets": [
  #   {
  #     "target_name": "gdi",
  #     "sources": [ "./src/gdi.cc" ],
  #      "libraries": [ "Gdiplus.lib", "Shlwapi.lib" ]
  #   }
  # ]
}