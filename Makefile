# --- Prompt History targets ---
PHR_DIR := docs/prompts
ADR_DIR := docs/adr

## Create a new prompt file
## Usage: make prompt-new SLUG=chat-endpoint STAGE=architect
prompt-new:
	@python3 scripts/prompt_new.py --dir $(PHR_DIR) --slug $(SLUG) --stage $(STAGE)

## Rebuild prompt index (docs/prompts/index.md)
prompt-index:
	@python3 scripts/prompt_index.py --dir $(PHR_DIR)

## Validate staged changes reference a prompt (run manually if no hooks)
prompt-guard:
	@python3 scripts/prompt_guard.py
