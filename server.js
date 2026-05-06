require('dotenv').config();
const express = require('express');
const { spawn, execSync } = require('child_process');

const app = express();
const PORT = process.env.PORT || 3000;

// Dummy route to satisfy health checks
app.get('/', (req, res) => {
    res.send('CineMatch Bot is running!');
});

app.listen(PORT, () => {
    console.log(`Dummy web server listening on port ${PORT}`);
    
    // Configure OpenClaw automatically before starting
    try {
        console.log('Setting up OpenClaw configuration...');
        execSync('openclaw config set agents.defaults.workspace .', { stdio: 'inherit' });
        
        // Ensure free LLM models are selected
        execSync('openclaw models set "openrouter/meta-llama/llama-3.3-70b-instruct:free"', { stdio: 'inherit' });
        
        // Add multiple fallbacks to survive free tier rate limits
        const fallbacks = [
            'openrouter/nousresearch/hermes-3-llama-3.1-405b:free',
            'openrouter/google/gemma-4-31b-it:free',
            'openrouter/qwen/qwen3-next-80b-a3b-instruct:free',
            'openrouter/meta-llama/llama-3.2-3b-instruct:free',
            'openrouter/openai/gpt-oss-120b:free'
        ];
        
        for (const model of fallbacks) {
            try {
                execSync(`openclaw models fallbacks add "${model}"`, { stdio: 'inherit' });
            } catch (e) {
                // Ignore if it's already added or fails
            }
        }
        
        // Connect Telegram bot dynamically
        if (process.env.TELEGRAM_BOT_TOKEN) {
            console.log('Configuring Telegram channel...');
            execSync(`openclaw channels add --channel telegram --token "${process.env.TELEGRAM_BOT_TOKEN}" --name "CineMatch Bot"`, { stdio: 'inherit' });
        } else {
            console.warn('WARNING: TELEGRAM_BOT_TOKEN is not set in environment variables.');
        }

        // Disable pairing to make the bot public for everyone
        execSync('openclaw config set gateway.auth.mode token', { stdio: 'inherit' });
    } catch (error) {
        console.error('Failed to configure OpenClaw:', error.message);
    }

    // Start OpenClaw gateway in foreground
    console.log('Starting OpenClaw gateway...');
    const openclaw = spawn('openclaw', ['gateway', 'run'], {
        stdio: 'inherit',
        shell: true
    });

    openclaw.on('close', (code) => {
        console.log(`OpenClaw process exited with code ${code}`);
    });
});
