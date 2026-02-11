import sys

def main():
    file_path = 'a-Shell/SceneDelegate.swift'
    with open(file_path, 'r') as f:
        lines = f.readlines()

    start_line = -1
    end_line = -1

    # Locate the block
    for i, line in enumerate(lines):
        if 'if (storedCommand.hasPrefix("vim -S ")) {' in line:
            start_line = i
        if 'NSLog("Could not find session file at \(sessionFile)")' in line:
            # This is inside the else block of the file check
            # We need to find the closing brace of the main if (storedCommand...)
            # It's likely a few lines down.
            pass

    # Let's extract the exact lines based on previous  output
    # sed -n '4434,4460p' a-Shell/SceneDelegate.swift showed the start.
    # We need to capture the whole block.

    # I'll rely on the text content rather than line numbers to be robust.

    target_block_start = 'if (storedCommand.hasPrefix("vim -S ")) {'

    # I will read the file and replace the whole block with the new logic.

    new_block = """                if (storedCommand.hasPrefix("vim -S ")) {
                    var sessionFile = storedCommand
                    sessionFile.removeFirst("vim -S ".count)
                    if (sessionFile.hasPrefix("~")) {
                        sessionFile.removeFirst("~".count)
                        let documentsUrl = try! FileManager().url(for: .documentDirectory,
                                                                     in: .userDomainMask,
                                                                     appropriateFor: nil,
                                                                     create: true)
                        let homeUrl = documentsUrl.deletingLastPathComponent()
                        sessionFile = homeUrl.path + sessionFile
                    }
                    if (FileManager().fileExists(atPath: sessionFile)) {
                        // We counter it by restoring TERM before starting Vim:
                        if let storedTermC = getenv("TERM") {
                            if let storedTerm = String(utf8String: storedTermC) {
                                if storedTerm == "dumb" {
                                    setenv("TERM", "xterm", 1)
                                }
                            }
                        }
                        NSLog("Restarting session with \(storedCommand)")

                        if (UserDefaults.standard.bool(forKey: "restart_vim")) {
                            /* We only restart vim commands, and only if the user asks for it.
                             Everything else is creating problems.
                             Basically, we can only restart commands if we can save their status. */
                            // The preference is set to false by default, to avoid beginners trapped in Vim
                            NSLog("sceneWillEnterForeground, Restoring command: \(storedCommand)")
                            let commandSent = storedCommand.replacingOccurrences(of: "\\", with: "\\\\").replacingOccurrences(of: "\\"", with: "\\\\"").replacingOccurrences(of: "'", with: "\\'").replacingOccurrences(of: "\n", with: "\\n")
                            let restoreCommand = "window.webkit.messageHandlers.aShell.postMessage('shell:' + '\(commandSent)');\nwindow.commandRunning = '\(commandSent)';\n"
                            currentCommand = commandSent
                            NSLog("Calling command: \(restoreCommand)")
                            self.webView?.evaluateJavaScript(restoreCommand) { (result, error) in
                                // if let error = error { print(error) }
                                // if let result = result { print(result) }
                            }
                        }
                    } else {
                         NSLog("Could not find session file at \(sessionFile)")
                    }
                }"""

    # Note: escaping in the python string for replaceOccurrences is tricky.
    # original: .replacingOccurrences(of: "\", with: "\\")
    # python string: .replacingOccurrences(of: "\\", with: "\\\\")

    # Let's try to just locate the lines and swap them programmatically to avoid hardcoding the inner logic if possible,
    # but the inner logic is interleaved.

    # Constructing the exact original block to replace is risky if I get whitespace wrong.
    # Let's read the file content, find the range, and replace it.

    content = "".join(lines)

    # Search for the start
    start_idx = content.find('if (storedCommand.hasPrefix("vim -S ")) {')
    if start_idx == -1:
        print("Could not find start of block")
        sys.exit(1)

    # Find the matching closing brace.
    brace_count = 0
    end_idx = -1
    found_start = False

    for i in range(start_idx, len(content)):
        if content[i] == '{':
            brace_count += 1
            found_start = True
        elif content[i] == '}':
            brace_count -= 1
            if found_start and brace_count == 0:
                end_idx = i + 1
                break

    if end_idx == -1:
        print("Could not find end of block")
        sys.exit(1)

    original_block = content[start_idx:end_idx]

    # Now we have the original block. We can parse it or just replace it if we are confident.
    # Given the complexity, I'll rewrite the new block carefully matching indentation.

    # I need to be careful with the escaping in .
    # Original:
    # let commandSent = storedCommand.replacingOccurrences(of: "\", with: "\\").replacingOccurrences(of: "\"", with: "\\"").replacingOccurrences(of: "'", with: "\'").replacingOccurrences(of: "\n", with: "\n")

    # New block construction:
    new_block_lines = [
        '                if (storedCommand.hasPrefix("vim -S ")) {',
        '                    // Safety check: is the vim session file still there?',
        '                    // I could have been removed by the system, or by the user.',
        '                    var sessionFile = storedCommand',
        '                    sessionFile.removeFirst("vim -S ".count)',
        '                    if (sessionFile.hasPrefix("~")) {',
        '                        sessionFile.removeFirst("~".count)',
        '                        let documentsUrl = try! FileManager().url(for: .documentDirectory,',
        '                                                                     in: .userDomainMask,',
        '                                                                     appropriateFor: nil,',
        '                                                                     create: true)',
        '                        let homeUrl = documentsUrl.deletingLastPathComponent()',
        '                        sessionFile = homeUrl.path + sessionFile',
        '                    }',
        '                    if (FileManager().fileExists(atPath: sessionFile)) {',
        '                        // We counter it by restoring TERM before starting Vim:',
        '                        if let storedTermC = getenv("TERM") {',
        '                            if let storedTerm = String(utf8String: storedTermC) {',
        '                                if storedTerm == "dumb" {',
        '                                    setenv("TERM", "xterm", 1)',
        '                                }',
        '                            }',
        '                        }',
        '                        NSLog("Restarting session with \(storedCommand)")',
        '                        if (UserDefaults.standard.bool(forKey: "restart_vim")) {',
        '                            /* We only restart vim commands, and only if the user asks for it.',
        '                             Everything else is creating problems.',
        '                             Basically, we can only restart commands if we can save their status. */',
        '                            // The preference is set to false by default, to avoid beginners trapped in Vim',
        '                            NSLog("sceneWillEnterForeground, Restoring command: \(storedCommand)")',
        '                            let commandSent = storedCommand.replacingOccurrences(of: "\\", with: "\\\\").replacingOccurrences(of: "\\"", with: "\\\\"").replacingOccurrences(of: "\'", with: "\\\'").replacingOccurrences(of: "\n", with: "\\n")',
        '                            let restoreCommand = "window.webkit.messageHandlers.aShell.postMessage(\'shell:\' + \'\(commandSent)\');\nwindow.commandRunning = \'\(commandSent)\';\n"',
        '                            currentCommand = commandSent',
        '                            NSLog("Calling command: \(restoreCommand)")',
        '                            self.webView?.evaluateJavaScript(restoreCommand) { (result, error) in',
        '                                // if let error = error { print(error) }',
        '                                // if let result = result { print(result) }',
        '                            }',
        '                        }',
        '                    } else {',
        '                        NSLog("Could not find session file at \(sessionFile)")',
        '                    }',
        '                }'
    ]

    new_block_str = "\n".join(new_block_lines)

    new_content = content[:start_idx] + new_block_str + content[end_idx:]

    with open(file_path, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    main()
