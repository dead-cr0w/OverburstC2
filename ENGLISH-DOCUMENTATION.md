# OverburstC2 - Comprehensive English Documentation

## Project Overview

OverburstC2 is an enhanced version of SentinelaNet, a Command and Control (C&C) server written in Python. This version improves upon the base SentinelaNet with better code organization, enhanced security features, and modular architecture.

### Key Improvements Over SentinelaNet
- **Modular Architecture**: Separated concerns with dedicated modules for bot management, attack handling, session management, and command processing
- **Enhanced Security**: Input validation, rate limiting, and secure bot authentication
- **Database Integration**: User management backed by database system
- **Session Management**: Proper session handling with activity tracking
- **Comprehensive Logging**: Detailed logs for all operations
- **Rate Limiting**: Protection against brute-force login attempts

---

## Installation

### Requirements
```
colorama==0.4.6
bcrypt==4.1.2
```

### Setup Instructions
```bash
git clone https://github.com/dead-cr0w/OverburstC2.git
cd OverburstC2
pip install -r requirements.txt
python main.py
```

---

## Available Commands

### Admin Commands

| Command | Description |
|---------|-------------|
| `!user` | Add / List / Remove users |
| `!blacklist` | Add / List / Remove blacklisted targets |

### CNC (Command and Control) Commands

| Command | Description |
|---------|-------------|
| `help` | Shows list of available commands |
| `botnet` | Displays available botnet attack methods |
| `bots` | Shows all connected bots with architecture information |
| `stop` | Stops all floods in progress |
| `clear` | Clears the console screen |
| `exit` | Disconnects from the C&C server |

---

## Attack Methods

### Available Payload Methods

| Method | Description |
|--------|-------------|
| `.UDP` | Sends varying size UDP packets to overwhelm the target |
| `.TCP` | Continuously sends TCP packets to exhaust connections |
| `.SYN` | Sends SYN requests to flood pending TCP handshakes |
| `.MIX` | Alternates between TCP and UDP to bypass protections |
| `.VSE` | Sends Valve Source Engine protocol floods |
| `.FIVEM` | Specialized payload designed for FiveM servers |
| `.OVHUDP` | UDP floods with random payloads targeting specific ports |
| `.OVHTCP` | Randomized byte sequences and terminators to bypass WAFs |
| `.DISCORD` | Specialized UDP packet targeting Discord services |

### Attack Usage Format
```
[METHOD] [TARGET_IP] [PORT] [DURATION_SECONDS]
```

Example:
```
.UDP 192.168.1.1 80 60
```

---

## Technical Architecture

### Core Components

#### 1. SentinelaServer (main.py)
The main server class that orchestrates all functionality:
- Connection handling
- Client and bot management
- Session management
- Attack orchestration
- Title bar updates with real-time statistics

#### 2. BotManager (src/utils/bot_manager.py)
Manages all connected bots:
- Bot registration and tracking
- Architecture-based organization
- Ping/keepalive mechanism
- Bot removal and cleanup

#### 3. AttackManager (src/utils/attack_manager.py)
Handles attack execution and management:
- Attack validation
- Target blacklist checking
- Rate limiting per user
- Attack scheduling and cleanup

#### 4. SessionManager (src/utils/session_manager.py)
Manages user sessions:
- Session creation and tracking
- Activity monitoring
- Session expiration cleanup
- Secure session tokens

#### 5. CommandHandler (src/utils/command_handler.py)
Processes all user commands:
- Command parsing and validation
- Admin command execution
- Attack command routing
- User-specific command handling

---

## Database System

### User Management
Users are stored in a database with the following information:
- Username
- Password (bcrypt hashed)
- Creation date
- Last login information
- User role/privileges

### Blacklist Management
- Stores blacklisted target IPs
- Prevents attacks on protected targets
- Persistent storage across server restarts

---

## Network Implementation

### Connection Security
- **Bot Authentication**: Bots authenticate using a shared secret
- **Input Validation**: All inputs are validated before processing
- **Rate Limiting**: Protects against brute-force attacks
- **Socket Timeouts**: Prevents hanging connections

### Data Flow
1. Client connects to server on configured port
2. Username and password authentication
3. Session token creation upon successful login
4. Command processing loop
5. Real-time title bar updates with server statistics

---

## Configuration

### Server Configuration (config.json)
```json
{
  "server": {
    "host": "0.0.0.0",
    "port": 1337,
    "name": "SentinelaC2"
  },
  "global_limits": {
    "max_attacks": 30,
    "threads": 5
  },
  "bot_secret": "BASE64_ENCODED_SECRET"
}
```

---

## Updates and Features

### Recent Fixes
- ✅ Fixed: Some attacks were not being launched
- ✅ Fixed: SyntaxError with f-string formatting in main.py
- ✅ Some methods have been optimized for better performance
- ✅ Bot code has been reorganized for clarity
- ✅ STOP command functionality improved

### Upcoming Features
- [ ] Additional attack methods (Coming Soon)
- [ ] Enhanced statistics and analytics
- [ ] Improved bot management interface

---

## Bot Architecture Support

OverburstC2 recognizes and categorizes bots by architecture:
- `i386` - 32-bit Intel/AMD processors
- `mips` - MIPS architecture
- `mips64` - 64-bit MIPS architecture
- `x86_64` - 64-bit Intel/AMD processors
- `armv7l` - 32-bit ARM processors
- `armv8l` - 32-bit ARM version 8
- `aarch64` - 64-bit ARM processors
- `ppc64le` - 64-bit PowerPC little-endian
- `unknown` - Unidentified architectures

---

## Security Considerations

### Best Practices
1. Change default credentials immediately
2. Use strong, unique passwords
3. Enable input validation in configuration
4. Monitor logs regularly for suspicious activity
5. Keep Python and dependencies updated
6. Use firewall rules to restrict C&C access
7. Implement proper network isolation

### Rate Limiting
- Maximum 5 login attempts per IP address per 5-minute window
- Automatic temporary lockout after threshold exceeded
- Prevents brute-force credential attacks

### Logging
- All user actions are logged with timestamps
- Failed login attempts are recorded
- Bot connections and disconnections are tracked
- All attacks are logged with associated user information

---

## ⚠️ Legal Notice

This project is strictly intended for **educational and research purposes only**.  
Misuse of this software may be **illegal** and lead to **criminal penalties**.  
Always use cybersecurity knowledge to **defend systems**, never to attack them.

---

## Author Information

- **Project Creator**: CirqueiraDev (Base SentinelaNet)
- **OverburstC2 Enhancements**: dead-cr0w
- **Discord**: Cirqueira
- **Instagram**: @sirkeirax
