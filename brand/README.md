# SuperDoc Brand

This directory is the single source of truth for SuperDoc's brand identity, design tokens, and visual guidelines.

## Structure

```
brand/
  tokens/
    primitive/          Raw color, typography, and spacing values
      colors.tokens.json
      typography.tokens.json
      spacing.tokens.json
    semantic/           Role-based mappings for light and dark themes
      theme-light.tokens.json
      theme-dark.tokens.json
  brand-guidelines.md   Voice, tone, positioning, and content patterns
  visual-identity.md    Logo usage, color meanings, and visual do's/don'ts
  assets/
    logos/               Logo files (SVG, PNG)
```

## Token Format

Tokens follow the [W3C Design Tokens (DTCG) 2025.10 specification](https://www.designtokens.org/tr/drafts/format/). Every token includes a `$description` field explaining when and why to use it — this makes the tokens AI-readable.

## How to Use

**For AI tools** (Claude, Cursor, Copilot): These files are referenced in CLAUDE.md and can be loaded as context. The `$description` fields on tokens provide usage guidance without needing separate documentation.

**For development**: Primitive tokens define the palette; semantic tokens map those to UI roles. Always use semantic tokens in component code — never hardcode hex values.

**For marketing/content**: See `brand-guidelines.md` for voice, tone, and writing patterns.
