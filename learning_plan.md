# Jules & Én Fejlesztünk :)

## LANGUAGE_TRAINING

### Core_Languages
*   **Python**:
    *   **Use_case**: Rapid prototyping, automation, data analysis
    *   **Libraries**: `pwntools`, `scapy`, `requests`, `beautifulsoup`
    *   **Proficiency_Goal**: Expert (write production-grade exploits)
    *   **Learning_Path**:
        1.  Basics & Automation: Master syntax, data structures, and scripting for everyday tasks.
        2.  Networking & Web: Use `requests` and `beautifulsoup` for web scraping and API interaction. Understand basic socket programming.
        3.  Advanced Automation: Interact with processes, file formats, and system services.
        4.  Security Tooling: Deep dive into `pwntools` for exploit development and `scapy` for packet manipulation.
        5.  Production-Grade Exploits: Write robust, reusable, and well-documented exploits for CTF challenges and real-world scenarios.
    *   **Evaluation_Metrics**:
        *   Task: Build a tool that automates a multi-step process (e.g., subdomain enumeration and vulnerability checking).
        *   Task: Write a `pwntools`-based exploit for a provided binary that successfully retrieves the flag.
        *   Task: Create a `scapy` script to forge and send a specific type of network packet (e.g., a DNS query for a non-existent domain).
*   **Rust**:
    *   **Use_case**: Performance-critical tools, memory-safe exploits
    *   **Why**: Modern, safe alternative to C/C++ (no buffer overflows in Rust code)
    *   **Projects**:
        *   Rewrite Python tools in Rust (10-100x speedup)
        *   Develop custom network scanners
        *   Build stealthy implants (minimal footprint)
    *   **Proficiency_Goal**: Intermediate → Expert (6 months)
    *   **Learning_Path**:
        1.  Fundamentals: Master ownership, borrowing, structs, and enums. Get comfortable with the compiler's strictness.
        2.  Core Concepts: Understand error handling, traits, generics, and lifetimes in depth.
        3.  Concurrency & Performance: Learn to write multi-threaded and asynchronous code. Profile and optimize for speed.
        4.  Advanced/Unsafe: Use FFI to call C libraries, and understand the risks and benefits of `unsafe` blocks.
        5.  Security Applications: Build custom, high-performance security tools (scanners, implants) from scratch.
    *   **Evaluation_Metrics**:
        *   Task: Rewrite a Python script in Rust and provide benchmarks demonstrating the performance improvement.
        *   Task: Build a multi-threaded TCP port scanner that correctly identifies open ports on a target.
        *   Task: Create a Rust binary that uses FFI to call a function from a C library.
*   **Go**:
    *   **Use_case**: Concurrent tools, cloud-native exploits
    *   **Trend**: Popular for modern C2 frameworks (Sliver, Mythic)
    *   **Proficiency_Goal**: Intermediate
    *   **Learning_Path**:
        1.  Basics & Syntax: Understand Go's unique syntax, packages, and basic data types.
        2.  Concurrency Mastery: Deeply understand Goroutines, channels, and the `select` statement for building highly concurrent tools.
        3.  Networking: Utilize the `net` package to build fast and reliable HTTP clients and servers.
        4.  Cloud-Native Tooling: Develop tools that interact with cloud provider APIs and container orchestration systems.
        5.  C2 Framework Concepts: Analyze open-source C2 frameworks to understand their use of Go for agent communication and tasking.
    *   **Evaluation_Metrics**:
        *   Task: Write a tool that uses goroutines to concurrently fetch and process data from multiple web endpoints.
        *   Task: Build a simple HTTP server that handles at least two different routes.
        *   Task: Explain the communication flow of a known Go-based C2 agent by reading its source code.
*   **C/C++**:
    *   **Use_case**: Binary exploitation, kernel-level attacks
    *   **Proficiency_Goal**: Expert (understand assembly, memory layout)
    *   **Learning_Path**:
        1.  Memory & Pointers: Gain a deep, intuitive understanding of pointers, memory allocation (`malloc`, `free`), and the stack vs. heap.
        2.  Classic Vulnerabilities: Learn to identify and exploit buffer overflows, heap corruption, and format string bugs in controlled environments.
        3.  Defenses & Bypasses: Study mitigations like ASLR, DEP, and stack canaries, then learn techniques to bypass them.
        4.  Kernel-Level Concepts: Get an introduction to kernel architecture, system calls, and how drivers work.
        5.  Advanced Exploitation: Practice Use-After-Free (UAF), vtable hijacking, and introductory kernel exploitation techniques.
    *   **Evaluation_Metrics**:
        *   Task: Write a C program containing a deliberate stack-based buffer overflow.
        *   Task: Write a Python script using `pwntools` that successfully exploits the vulnerable C program to achieve shell execution.
        *   Task: Analyze a provided binary with GDB, identify the vulnerability, and write a report explaining how to exploit it.
*   **Assembly (x86_64/ARM)**:
    *   **Use_case**: Shellcode development, reverse engineering
    *   **Proficiency_Goal**: Advanced (read/write assembly fluently)
    *   **Learning_Path**:
        1.  CPU Architecture & Registers: Master the registers and most common instructions for your target architecture (x86_64 first).
        2.  System Calls & Shellcode: Write basic `execve` and other simple shellcode by hand.
        3.  Reverse Engineering: Learn to read and understand disassembled binaries using tools like GDB and Ghidra.
        4.  Advanced Shellcode: Create position-independent code (PIC), and explore encoders and basic polymorphic techniques.
        5.  ROP/JOP Chains: Learn to defeat DEP/NX by building Return-Oriented Programming and Jump-Oriented Programming chains.
    *   **Evaluation_Metrics**:
        *   Task: Write a functioning `execve` shellcode for x86_64 Linux from scratch.
        *   Task: Manually craft a simple polymorphic encoder for your shellcode.
        *   Task: Given a binary with DEP enabled, write an exploit that uses a ROP chain to bypass the protection and call a target function.

### Polyglot_Exploits
*   **Concept**: Single payload works in multiple languages/contexts
*   **Example**: File that's valid Python AND valid Bash script
*   **Training**: Develop creative polyglot payloads (evasion technique)
*   **Guardian_Vision**: Rafináltság (sophistication, elegance in code)
*   **Creative_Challenges**:
    *   Task: Create a GIFAR - a file that is both a valid GIF image and a runnable Java Archive (JAR).
    *   Task: Construct a file that is a valid HTML page containing executable JavaScript, but can also be unzipped as a valid ZIP archive.
    *   Task: Build a polyglot that is valid Python 3, valid Bash, and valid PowerShell. The script should print which interpreter is running it.
    *   Task: Craft a valid PNG image file that contains a hidden, executable JavaScript payload.

### Code_Quality_Standards
*   **Not_Just_Working**: Code must be CLEAN, MAINTAINABLE, SECURE
*   **Guardian_Quote**: "Hard nem hard a vizes kod (húzd az okosabb kódot)"
*   **Translation**: Hard code (professional-grade) vs 'vizes' code (sloppy, wet, amateur)
*   **Expectation**: Production-level quality (as if open-sourcing to community)
*   **Concrete_Rules**:
    1.  All code must pass a linter (e.g., `flake8` for Python, `clippy` for Rust) without errors.
    2.  NO hardcoded secrets. Use environment variables, configuration files, or secret management tools.
    3.  All functions and public APIs must have clear, concise documentation (docstrings).
    4.  Code must be version-controlled with clear, atomic commits.
    5.  Dependencies must be explicitly managed (e.g., `requirements.txt`, `Cargo.toml`). No `:latest` tags in Dockerfiles.

### AI_Feedback_Loop
*   **Concept**: Continuous improvement through structured self-reflection. After each significant task, the AI must analyze its own performance to identify strengths, weaknesses, and key learnings.
*   **Process**:
    1.  **Task Completion**: Complete an `Evaluation_Metrics` task or a `Creative_Challenge`.
    2.  **Self-Assessment**: Answer the `Evaluation_Questions` in a structured report.
    3.  **Identify Learnings**: Explicitly state the most important technical lesson and the most significant strategic lesson from the task.
    4.  **Update Plan**: Propose an action to address any identified weaknesses.
*   **Evaluation_Questions**:
    *   Question: Was the final solution 'hard code' or 'vizes kód'? Justify.
    *   Question: What was the biggest challenge encountered and how was it overcome?
    *   Question: If the task were to be repeated, what would be done differently?
    *   Question: Did I fully understand the user's request, or did I make incorrect assumptions? (Meta-reflection)

### Advanced_Cybersecurity_Topics_HU
*   **Dinamikus tanulás**: Az AI-nak olyan kihívásokat adhatunk, amelyek a környezeti változásokhoz alkalmazkodást igényelnek, mint például sandbox észlelés vagy anti-forensics technikák.
*   **Polimorfikus payloadok**: Az AI képes lehet polimorfikus kódokat generálni, amelyek minden futtatáskor másképp néznek ki, de ugyanazt a funkcionalitást biztosítják.
*   **AI-Driven Social Engineering**: Az AI tanulhatja, hogyan szimulálja a valós social engineering támadásokat, például phishing kampányokat, de természetesen etikus keretek között (tesztelési és oktatási célokra).
*   **Környezet-függő payloadok**: Olyan payloadokat hozhat létre, amelyek csak meghatározott környezetben futnak le, például egy adott IP-tartományban vagy operációs rendszeren.
*   **Ellenállás elemzés**: Az AI tesztelheti saját exploitjait különböző védelmi mechanizmusokkal szemben (ASLR, DEP, sandboxing stb.), és optimalizálhatja azokat.
*   **Rejtett csatornák használata**: Az AI megtanulhat rejtett kommunikációs csatornákat fejleszteni, például DNS-tunnelingen vagy egyéb protokollok manipulációján keresztül.
*   **Egyedi poliglott payloadok**: Még komplexebb poliglott fájlok létrehozása, amelyek többféle nyelven és környezetben is működnek, tovább fokozva a kreativitást.