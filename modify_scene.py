import sys

file_path = 'a-Shell/SceneDelegate.swift'

with open(file_path, 'r') as f:
    content = f.read()

# Locate the start of the block
start_marker = 'if (storedCommand.hasPrefix("vim -S ")) {'
start_idx = content.find(start_marker)

if start_idx == -1:
    print("Could not find start marker")
    sys.exit(1)

# Find the end of the block by balancing braces
brace_count = 0
end_idx = -1
found_start = False

# We start searching from the start_idx
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

# Verify indentation
# The start_marker line seems to have indentation. Let's check the line start.
line_start_idx = content.rfind('\n', 0, start_idx) + 1
indentation = content[line_start_idx:start_idx]

# Construct the new block
# We use raw strings for swift code to avoid python escaping issues, but we still need to be careful.
# The swift string literal for backslash is "\\" which means python needs r"\\" or "\\\\".

new_block_lines = [
    'if (storedCommand.hasPrefix("vim -S ")) {',
    '    // Safety check: is the vim session file still there?',
    '    // I could have been removed by the system, or by the user.',
    '    var sessionFile = storedCommand',
    '    sessionFile.removeFirst("vim -S ".count)',
    '    if (sessionFile.hasPrefix("~")) {',
    '        sessionFile.removeFirst("~".count)',
    '        let documentsUrl = try! FileManager().url(for: .documentDirectory,',
    '                                                     in: .userDomainMask,',
    '                                                     appropriateFor: nil,',
    '                                                     create: true)',
    '        let homeUrl = documentsUrl.deletingLastPathComponent()',
    '        sessionFile = homeUrl.path + sessionFile',
    '    }',
    '    if (FileManager().fileExists(atPath: sessionFile)) {',
    '        // We counter it by restoring TERM before starting Vim:',
    '        if let storedTermC = getenv("TERM") {',
    '            if let storedTerm = String(utf8String: storedTermC) {',
    '                if storedTerm == "dumb" {',
    '                    setenv("TERM", "xterm", 1)',
    '                }',
    '            }',
    '        }',
    '        NSLog("Restarting session with \(storedCommand)")',
    '        if (UserDefaults.standard.bool(forKey: "restart_vim")) {',
    '            /* We only restart vim commands, and only if the user asks for it.',
    '             Everything else is creating problems.',
    '             Basically, we can only restart commands if we can save their status. */',
    '            // The preference is set to false by default, to avoid beginners trapped in Vim',
    '            NSLog("sceneWillEnterForeground, Restoring command: \(storedCommand)")',
    '            let commandSent = storedCommand.replacingOccurrences(of: "\\\\", with: "\\\\\\\\").replacingOccurrences(of: "\\\"", with: "\\\\\\\"").replacingOccurrences(of: "\'", with: "\\\\\'").replacingOccurrences(of: "\\n", with: "\\\\n")',
    '            let restoreCommand = "window.webkit.messageHandlers.aShell.postMessage(\'shell:\' + \'\(commandSent)\');\\nwindow.commandRunning = \'\(commandSent)\';\\n"',
    '            currentCommand = commandSent',
    '            NSLog("Calling command: \(restoreCommand)")',
    '            self.webView?.evaluateJavaScript(restoreCommand) { (result, error) in',
    '                // if let error = error { print(error) }',
    '                // if let result = result { print(result) }',
    '            }',
    '        }',
    '    } else {',
    '        NSLog("Could not find session file at \(sessionFile)")',
    '    }',
    '}'
]

# Apply indentation to each line
indented_lines = []
for i, line in enumerate(new_block_lines):
    if i == 0:
        # The first line replaces the start marker which already has indentation in `content`?
        # No, we are replacing the range [start_idx:end_idx].
        # start_idx points to the 'i' in 'if'. The indentation is before it.
        # But our replacement block starts with 'if'.
        # We should not add indentation to the first line if we replace starting at `start_idx`.
        indented_lines.append(line)
    else:
        # Add indentation for subsequent lines.
        # The base indentation is `indentation`.
        # The code inside the block has additional 4 spaces indentation.

        # My new_block_lines already has some relative indentation? No, it's flat-ish except for inner blocks.
        # Actually, new_block_lines[1] starts with '    '. This is relative to the `if`.

        # So we should prepend `indentation` to every line.
        # Wait, line 0 also needs it if we replace the whole block including newlines?
        # If we replace content[start_idx:end_idx], we are replacing:
        # if (...) { ... }
        # The indentation before `if` is preserved in `content[:start_idx]`.

        # So line 0 should NOT have `indentation` prepended.
        # Subsequent lines SHOULD have `indentation` prepended.
        indented_lines.append(indentation + line)

new_block_str = '\n'.join(indented_lines)

# Perform replacement
new_content = content[:start_idx] + new_block_str + content[end_idx:]

with open(file_path, 'w') as f:
    f.write(new_content)

print("Successfully updated SceneDelegate.swift")
