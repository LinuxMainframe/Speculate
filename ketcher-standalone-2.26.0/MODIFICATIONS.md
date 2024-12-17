# Modifications to Ketcher Standalone v2.26.0

This document details modifications made to the original Ketcher Standalone library for use in this project.

## Modified Files
### `index.html`
- **Description**: A polyfill was added to ensure compatibility with Qt's WebView system, which uses an older JavaScript engine. This resolves issues related to the absence of the `Object.hasOwn` function in such environments.
- **Code Addition**:
  ```html
  <script>
      if (!Object.hasOwn) {
          Object.hasOwn = function(obj, prop) {
              return Object.prototype.hasOwnProperty.call(obj, prop);
          };
      }
  </script>
