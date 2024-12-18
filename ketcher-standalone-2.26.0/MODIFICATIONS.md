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
  ```
- **Formatting Changes**:  
  Code was reformatted to de-minimize the code for better reading and adaptation for connections between PyQt5's WebEngineView and the JS Ketcher App via QWebChannel  
  - *JSBeautifier was used on .css and .js files*
  ```python
  import jsbeautifier
  import sys
  
  def beautify(input_file, output_file):
      # Read and beautify the input file
      with open(input_file, 'r') as f:
          content = f.read()
      beautified_content = jsbeautifier.beautify(content)
  
      # Save the beautified code to the output file
      with open(output_file, 'w') as f:
          f.write(beautified_content)
  
  if __name__ == "__main__":
      #This check is specific to my usage, and jsbeautifier does not require an output file designation
      if len(sys.argv) != 3:
          print("Usage: python beautify.py <input_file> <output_file>")
      else:
          beautify(sys.argv[1], sys.argv[2])
  ```
  You can find jsbeautifier in the following github repo: [jsbeautifier](https://github.com/beautifier/js-beautify)
