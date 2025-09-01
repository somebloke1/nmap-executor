#!/usr/bin/env python3
"""
Governance File Parser

Parses the governance_unparsed.md file and extracts individual documents
into separate files based on markdown headers and '---' delimiters.
"""

import os
import re
from pathlib import Path
from typing import List, Tuple, Optional

def parse_governance_file(input_file: str, output_dir: str = ".") -> List[str]:
    """
    Parse governance file and extract documents to separate files.
    
    Args:
        input_file: Path to the governance_unparsed.md file
        output_dir: Directory to create output files in
        
    Returns:
        List of created file paths
    """
    
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    created_files = []
    current_filename = None
    current_content = []
    in_document = False
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line_num, line in enumerate(lines, 1):
        line = line.rstrip('\n')  # Remove trailing newline for processing
        
        # Check if this is a filename header (starts with "# " and looks like a filename)
        if line.startswith('# ') and is_filename_header(line):
            # If we were already processing a document, save it first
            if current_filename and current_content:
                save_document(current_filename, current_content, output_dir)
                created_files.append(current_filename)
            
            # Start new document
            current_filename = line[2:].strip()  # Remove "# " prefix
            current_content = [line + '\n']  # Include the header line in content
            in_document = True
            print(f"Found document header: {current_filename} (line {line_num})")
            
        # Check if this is a section delimiter
        elif line == '---' and in_document:
            # End of current document
            if current_filename and current_content:
                save_document(current_filename, current_content, output_dir)
                created_files.append(current_filename)
                print(f"Completed document: {current_filename}")
            
            # Reset for next document
            current_filename = None
            current_content = []
            in_document = False
            
        # Collect content lines
        elif in_document and current_filename:
            # Add the original line with newline preserved
            current_content.append(line + '\n')
    
    # Handle the last document if file doesn't end with '---'
    if current_filename and current_content:
        save_document(current_filename, current_content, output_dir)
        created_files.append(current_filename)
        print(f"Completed final document: {current_filename}")
    
    return created_files

def is_filename_header(line: str) -> bool:
    """
    Determine if a line starting with '# ' is a filename header.
    
    Args:
        line: The line to check
        
    Returns:
        True if this appears to be a filename header
    """
    # Remove the '# ' prefix
    potential_filename = line[2:].strip()
    
    # Known valid filenames from our governance file
    valid_filenames = {
        'CLAUDE.md',
        'notation_guide.md', 
        'glyph_system.md',
        'orchestrator_identity.md',
        'orchestrator_delegation_patterns.md',
        'agent_task_matching.md',
        'agent_selection_for_task.md',
        'external_lm_consultation.md',
        'git_workflow.md',
        'project_management.md',
        'memory_practices.md',
        'directory_structure.md',
        'tool_abstract.md',
        'zen_mcp_server.md',
        'context7.md',
        'manifest.yml',
        'governance_loading.md'
    }
    
    # Direct match with known filenames
    if potential_filename in valid_filenames:
        return True
    
    # Fallback: check if it looks like a filename
    # Should have an extension and not contain parentheses or long descriptive text
    if ('.' in potential_filename and 
        '(' not in potential_filename and 
        ')' not in potential_filename and
        len(potential_filename) < 50 and
        not ' ' in potential_filename):
        return True
    
    return False

def save_document(filename: str, content: List[str], output_dir: str) -> None:
    """
    Save document content to a file.
    
    Args:
        filename: Name of the file to create
        content: List of content lines (with newlines)
        output_dir: Directory to create the file in
    """
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Handle potential subdirectories in filename
    full_path = os.path.join(output_dir, filename)
    file_dir = os.path.dirname(full_path)
    if file_dir and file_dir != output_dir:
        os.makedirs(file_dir, exist_ok=True)
    
    # Write content to file
    with open(full_path, 'w', encoding='utf-8') as f:
        if content:
            # Join all content and strip any trailing whitespace/newlines
            full_content = ''.join(content).rstrip()
            
            # Write the content with exactly one newline at the end
            f.write(full_content + '\n')
        else:
            # Empty content, just write a newline
            f.write('\n')

def main():
    """Main function to run the parser."""
    
    input_file = "/home/dgk/projects/nmap-executor/_user-docs/governance_unparsed.md"
    output_dir = "/home/dgk/projects/nmap-executor"
    
    print(f"Parsing governance file: {input_file}")
    print(f"Output directory: {output_dir}")
    print("-" * 50)
    
    try:
        created_files = parse_governance_file(input_file, output_dir)
        
        print("-" * 50)
        print(f"Successfully created {len(created_files)} files:")
        for filename in created_files:
            full_path = os.path.join(output_dir, filename)
            file_size = os.path.getsize(full_path)
            print(f"  - {filename} ({file_size} bytes)")
        
        print("\nParsing completed successfully!")
        
    except Exception as e:
        print(f"Error during parsing: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())