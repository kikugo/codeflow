import streamlit as st
import time

st.set_page_config(
    page_title="CodeFlow",
    page_icon=":desktop_computer:",
    initial_sidebar_state="expanded"
)

# Function to display the typewriter effect
def typewriter_effect(text, language, delay=0.05):
    placeholder = st.empty()  # Create a placeholder for dynamic updates
    current_text = ""
    for char in text:
        current_text += char
        placeholder.code(current_text, language=language, line_numbers=True, wrap_lines=True)  # Update the placeholder
        time.sleep(delay)  # Delay for typewriter effect

# Streamlit app
with st.sidebar:
    st.title("CodeFlow")
    st.write("Transform your code into a live storytelling experience.")
    st.divider()
    st.header("Usage")
    st.write("1. Select the programming language.")
    st.write("2. Enter the code.")
    st.write("3. Click on the Effect tab to see the typewriter effect.")
    st.info("Note: You can minimize this sidebar to see the full effect.")
    st.divider()
    st.write("Made with :heart: by [Rajtilak](https://github.com/rajtilakjee/codeflow)")

# Initialize session state for tab tracking if not already initialized
if 'start_effect' not in st.session_state:
    st.session_state.start_effect = False

if 'code_text' not in st.session_state:
    st.session_state.code_text = ""

if 'language' not in st.session_state:
    st.session_state.language = ""

data, effect = st.tabs(["Data", "Effect"])

with data:
    st.session_state.language = st.selectbox(
        "Please select the programming language the code is written in:",
        ("Abap", "Abnf", "Actionscript", "Ada", "Agda", "Al", "Antlr4", "Apacheconf", 
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
        "Xojo", "Xquery", "Yaml", "Yang", "Zig", "Other"),
        index=None,
        placeholder="Select the programming language...",
    )
    if st.session_state.language:
        st.session_state.code_text = st.text_area("Enter the code below:", height=500)

with effect:
    # Set the session state flag when the Effect tab is clicked
    if effect:
        st.session_state.start_effect = True

    # Trigger the typewriter effect only if the Effect tab is active and code is provided
    if st.session_state.start_effect and st.session_state.code_text and st.session_state.language:
        time.sleep(5)  # Add a small delay to allow users to see the transition
        if st.session_state.language == "Other":
            st.session_state.language = None
        else:
            st.session_state.language = st.session_state.language.lower()
        typewriter_effect(st.session_state.code_text, language=st.session_state.language, delay=0.1)
        
