from src.utils.listener import Listener
from src.utils.speaker import Speaker
from src.core.processor import CommandProcessor
from src.config import EXIT_COMMANDS, WAKE_WORD
import sys

def main():
    listener = Listener()
    speaker = Speaker()
    processor = CommandProcessor(listener)

    speaker.speak("System online. How can I help you?")

    while True:
        try:
            command = listener.listen()
            
            if command:
                if any(exit_cmd in command for exit_cmd in EXIT_COMMANDS):
                    speaker.speak("Goodbye!")
                    sys.exit()
                
                # Optional: Check for wake word if strictly required, 
                # currently processing all detected speech for smoother interaction
                # if WAKE_WORD in command: ...
                
                processor.process(command)
        
        except KeyboardInterrupt:
            speaker.speak("System stopping.")
            sys.exit()

if __name__ == "__main__":
    main()
