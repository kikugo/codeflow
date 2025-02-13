import streamlit as st
import time
import os  # NEW: Import the os module

# --- Constants ---
DEFAULT_DELAY = 0.05
SUPPORTED_LANGUAGES = ("Abap", "Abnf", "Actionscript", "Ada", "Agda", "Al", "Antlr4", "Apacheconf",
        "Apex", "Apl", "Applescript", "Aql", "Arduino", "Arff", "Asciidoc", "Asm6502",
        "Asmatmel", "Aspnet", "Autohotkey", "Autoit", "Avisynth", "AvroIdl (Avro-Idl)",
        "Bash", "Basic", "Batch", "Bbcode", "Bicep", "Birb", "Bison", "Bnf",
        "Brainfuck", "Brightscript", "Bro", "Bsl", "C", "Cfscript", "Chaiscript",
        "Cil", "Clike", "Clojure", "Cmake", "Cobol", "Coffeescript", "Concurnas",
        "Coq", "Cpp", "Crystal", "Csharp", "Cshtml", "Csp", "CssExtras (Css-Extras)",
        "Css", "Csv", "Cypher", "D", "Dart", "Dataweave", "Dax", "Dhall", "Diff",
        "Django", "DnsZoneFile (Dns-Zone-File)", "Docker", "Dot", "Ebnf",
        "Editorconfig", "Eiffel", "Ejs", "Elixir", "Elm", "Erb", "Erlang", "Etlua",
        "ExcelFormula (Excel-Formula)", "Factor", "Falselang (False)",
        "FirestoreSecurityRules (Firestore-Security-Rules)", "Flow", "Fortran",
        "Fsharp", "Ftl", "Gap", "Gcode", "Gdscript", "Gedcom", "Gherkin", "Git",
        "Glsl", "Gml", "Gn", "GoModule (Go-Module)", "Go", "Graphql", "Groovy",
        "Haml", "Handlebars", "Haskell", "Haxe", "Hcl", "Hlsl", "Hoon", "Hpkp",
        "Hsts", "Http", "Ichigojam", "Icon", "IcuMessageFormat (Icu-Message-Format)",
        "Idris", "Iecst", "Ignore", "Inform7", "Ini", "Io", "J", "Java", "Javadoc",
        "Javadoclike", "Javascript", "Javastacktrace", "Jexl", "Jolie", "Jq",
        "JsExtras (Js-Extras)", "JsTemplates (Js-Templates)", "Jsdoc", "Json",
        "Json5", "Jsonp", "Jsstacktrace", "Jsx", "Julia", "Keepalived", "Keyman",
        "Kotlin", "Kumir", "Kusto", "Latex", "Latte", "Less", "Lilypond", "Liquid",
        "Lisp", "Livescript", "Llvm", "Log", "Lolcode", "Lua", "Magma", "Makefile",
        "Markdown", "MarkupTemplating (Markup-Templating)", "Markup", "Matlab",
        "Maxscript", "Mel", "Mermaid", "Mizar", "Mongodb", "Monkey", "Moonscript",
        "N1ql", "N4js", "Nand2tetrisHdl (Nand2tetris-Hdl)", "Naniscript", "Nasm",
        "Neon", "Nevod", "Nginx", "Nim", "Nix", "Nsis", "Objectivec", "Ocaml",
        "Opencl", "Openqasm", "Oz", "Parigp", "Parser", "Pascal", "Pascaligo",
        "Pcaxis", "Peoplecode", "Perl", "PhpExtras (Php-Extras)", "Php", "Phpdoc",
        "Plsql", "Powerquery", "Powershell", "Processing", "Prolog", "Promql",
        "Properties", "Protobuf", "Psl", "Pug", "Puppet", "Pure", "Purebasic",
        "Purescript", "Python", "Q", "Qml", "Qore", "Qsharp", "R", "Racket",
        "Reason", "Regex", "Rego", "Renpy", "Rest", "Rip", "Roboconf",
        "Robotframework", "Ruby", "Rust", "Sas", "Sass", "Scala", "Scheme", "Scss",
        "ShellSession (Shell-Session)", "Smali", "Smalltalk", "Smarty", "Sml",
        "Solidity", "SolutionFile (Solution-File)", "Soy", "Sparql", "SplunkSpl (Splunk-Spl)",
        "Sqf", "Sql", "Squirrel", "Stan", "Stylus", "Swift", "Systemd", "T4Cs (T4-Cs)",
        "T4Templating (T4-Templating)", "T4Vb (T4-Vb)", "Tap", "Tcl", "Textile",
        "Toml", "Tremor", "Tsx", "Tt2", "Turtle", "Twig", "Typescript", "Typoscript",
        "Unrealscript", "Uorazor", "Uri", "V", "Vala", "Vbnet", "Velocity", "Verilog",
        "Vhdl", "Vim", "VisualBasic (Visual-Basic)", "Warpscript", "Wasm",
        "WebIdl (Web-Idl)", "Wiki", "Wolfram", "Wren", "Xeora", "XmlDoc (Xml-Doc)",
        "Xojo", "Xquery", "Yaml", "Yang", "Zig", "Other")

st.set_page_config(
    page_title="CodeFlow",
    page_icon=":desktop_computer:",
    initial_sidebar_state="expanded"
)

# Function to display the typewriter effect
def typewriter_effect(text, language, delay=DEFAULT_DELAY, line_numbers=True):
    placeholder = st.empty()
    current_text = ""
    for char in text:
        current_text += char
        placeholder.code(current_text, language=language, line_numbers=line_numbers, wrap_lines=True)
        time.sleep(delay)

# NEW: Utility function to get file extension
def get_file_extension(filename: str) -> str:
    """Extracts the file extension from a filename (e.g., 'app.py' -> 'py')."""
    return os.path.splitext(filename)[1][1:].lower()

# Streamlit app
with st.sidebar:
    st.title("CodeFlow")
    st.write("Transform your code into a live storytelling experience.")
    st.divider()
    st.header("Usage")
    st.write("1. Select language and options.")
    st.write("2. Enter code or upload a file.")
    st.write("3. Click 'Effect' to view.")
    st.info("Note: Minimize sidebar for full effect.")
    st.divider()
    st.write("Made with :heart: by [Rajtilak](https://github.com/rajtilakjee/codeflow)")

# Initialize session state
if 'start_effect' not in st.session_state:
    st.session_state.start_effect = False
if 'code_text' not in st.session_state:
    st.session_state.code_text = ""
if 'language' not in st.session_state:
    st.session_state.language = ""
if 'delay' not in st.session_state:
    st.session_state.delay = DEFAULT_DELAY
if 'line_numbers' not in st.session_state:
    st.session_state.line_numbers = True

data, effect = st.tabs(["Data", "Effect"])

with data:
    st.session_state.language = st.selectbox("Programming Language", SUPPORTED_LANGUAGES, index=None, placeholder="Select a language...")
    st.session_state.delay = st.slider("Typing Speed (Delay)", 0.01, 0.5, DEFAULT_DELAY, 0.01)
    st.session_state.line_numbers = st.checkbox("Show Line Numbers", value=True)

    # NEW: File uploader
    uploaded_file = st.file_uploader("Upload Code File", type=None)  # Allow any file type

    if uploaded_file is not None:
        try:
            # Read the file content
            file_content = uploaded_file.read().decode("utf-8")  # Decode for text files
            st.session_state.code_text = file_content

            # Attempt to auto-detect language from file extension
            detected_language = get_file_extension(uploaded_file.name)
            if detected_language in map(str.lower, SUPPORTED_LANGUAGES):
                # Find the index of the detected language (case-insensitive)
                try:
                    lang_index = [lang.lower() for lang in SUPPORTED_LANGUAGES].index(detected_language)
                    st.session_state.language = SUPPORTED_LANGUAGES[lang_index]  # Set to correct case
                    st.success(f"Detected language: {st.session_state.language}")
                except ValueError:
                    st.warning(f"Detected extension '{detected_language}', but could not set language.")

        except UnicodeDecodeError:
            st.error("Could not decode the uploaded file. Please ensure it's a text file.")
            st.session_state.code_text = ""  # Prevent errors later
        except Exception as e:
            st.error(f"Error processing file: {e}")
            st.session_state.code_text = ""

    # Text area *always* shown, but only populated if no upload error
    if st.session_state.language:
        st.session_state.code_text = st.text_area("Enter/Edit Code:", value=st.session_state.code_text, height=300)
with effect:
    if effect:
        st.session_state.start_effect = True

    if st.session_state.start_effect and st.session_state.code_text and st.session_state.language:
        time.sleep(5)
        if st.session_state.language == "Other":
            st.session_state.language = None
        else:
            st.session_state.language = st.session_state.language.lower()
        typewriter_effect(st.session_state.code_text, language=st.session_state.language, delay=st.session_state.delay, line_numbers=st.session_state.line_numbers)