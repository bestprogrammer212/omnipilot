"""Tool and Agent Registry for OmniPilot"""
from dataclasses import dataclass
from typing import Optional, List, Dict

@dataclass
class Agent:
    name: str
    description: str
    keywords: List[str]
    tool: str
    model: str
    division: str

@dataclass
class Tool:
    name: str
    executable: str
    description: str
    requires_ollama: bool
    default_model: Optional[str] = None
    supports_agents: bool = False

# Tool definitions
TOOLS: Dict[str, Tool] = {
    "opencode": Tool(
        name="OpenCode",
        executable="opencode",
        description="Coding agent with specialist roles",
        requires_ollama=True,
        default_model="qwen3:8b",
        supports_agents=True
    ),
    "hermes": Tool(
        name="Hermes Agent",
        executable="hermes",
        description="Autonomous coding agent with memory",
        requires_ollama=True,
        default_model="devstral:24b",
        supports_agents=False
    ),
    "interpreter": Tool(
        name="Open Interpreter",
        executable="interpreter",
        description="General-purpose desktop assistant",
        requires_ollama=True,
        default_model="phi4",
        supports_agents=False
    ),
    "ai3d": Tool(
        name="AI 3D Generator Pro",
        executable="AI 3D Generator Pro",
        description="Image-to-3D and text-to-3D generation",
        requires_ollama=False,
        default_model=None,
        supports_agents=False
    )
}

# ============================================================
# ENGINEERING DIVISION
# ============================================================
AGENTS: Dict[str, Agent] = {
    "frontend-developer": Agent(
        name="Frontend Developer",
        description="React/Vue/Angular, UI implementation, performance",
        keywords=["frontend", "react", "vue", "angular", "component", "ui", "ux", "typescript", "sass", "tailwind", "html", "css", "javascript", "web", "pwa", "website", "responsive"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "backend-architect": Agent(
        name="Backend Architect",
        description="API design, database architecture, scalability",
        keywords=["backend", "api", "database", "microservices", "cloud", "server", "architecture", "scalability"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "mobile-app-builder": Agent(
        name="Mobile App Builder",
        description="iOS/Android, React Native, Flutter",
        keywords=["mobile", "ios", "android", "react native", "flutter", "app"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "ai-engineer": Agent(
        name="AI Engineer",
        description="ML models, deployment, AI integration",
        keywords=["ai", "ml", "model", "llm", "neural", "training", "inference", "quantization", "fine-tune", "embedding", "vector", "ollama"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "devops-automator": Agent(
        name="DevOps Automator",
        description="CI/CD, infrastructure automation, cloud ops",
        keywords=["devops", "ci/cd", "pipeline", "infrastructure", "cloud", "deployment", "monitoring", "docker", "kubernetes"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "network-engineer": Agent(
        name="Network Engineer",
        description="Cisco IOS/IOS-XE, Juniper Junos, Palo Alto PAN-OS",
        keywords=["network", "cisco", "juniper", "palo alto", "router", "switch", "firewall", "bgp", "ospf", "acl"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "rapid-prototyper": Agent(
        name="Rapid Prototyper",
        description="Fast POC development, MVPs",
        keywords=["prototype", "mvp", "poc", "hackathon", "fast iteration"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "senior-developer": Agent(
        name="Senior Developer",
        description="Laravel/Livewire, advanced patterns",
        keywords=["laravel", "livewire", "advanced", "senior", "complex", "architecture"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "filament-optimization": Agent(
        name="Filament Optimization Specialist",
        description="Filament PHP admin UX, structural form redesign",
        keywords=["filament", "php", "admin", "form", "resource", "table"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "autonomous-optimization": Agent(
        name="Autonomous Optimization Architect",
        description="LLM routing, cost optimization, shadow testing",
        keywords=["llm routing", "cost optimization", "shadow testing", "api selection"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "embedded-firmware": Agent(
        name="Embedded Firmware Engineer",
        description="Bare-metal, RTOS, ESP32/STM32/Nordic firmware",
        keywords=["embedded", "firmware", "esp32", "stm32", "nordic", "bare-metal", "rtos", "microbit", "micro:bit", "arduino"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "incident-response-commander": Agent(
        name="Incident Response Commander",
        description="Incident management, post-mortems, on-call",
        keywords=["incident", "post-mortem", "on-call", "production", "outage"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "solidity-engineer": Agent(
        name="Solidity Smart Contract Engineer",
        description="EVM contracts, gas optimization, DeFi",
        keywords=["solidity", "smart contract", "evm", "gas", "defi", "ethereum", "blockchain"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "codebase-onboarding": Agent(
        name="Codebase Onboarding Engineer",
        description="Fast developer onboarding, read-only codebase exploration",
        keywords=["onboarding", "codebase", "exploration", "repo", "new developer"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "technical-writer": Agent(
        name="Technical Writer",
        description="Developer docs, API reference, tutorials",
        keywords=["documentation", "docs", "api reference", "tutorial", "technical writing"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "wechat-mini-program": Agent(
        name="WeChat Mini Program Developer",
        description="WeChat ecosystem, Mini Programs, payment integration",
        keywords=["wechat", "mini program", "payment", "weixin"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "code-reviewer": Agent(
        name="Code Reviewer",
        description="Constructive code review, security, maintainability",
        keywords=["review", "bug", "fix", "security", "refactor", "optimize", "test", "coverage", "vulnerability", "performance", "memory leak", "pr review"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "database-optimizer": Agent(
        name="Database Optimizer",
        description="Schema design, query optimization, indexing strategies",
        keywords=["database", "schema", "query", "optimization", "index", "postgresql", "mysql", "slow query", "migration"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "git-workflow-master": Agent(
        name="Git Workflow Master",
        description="Branching strategies, conventional commits, advanced Git",
        keywords=["git", "branch", "commit", "workflow", "history", "merge", "rebase"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "software-architect": Agent(
        name="Software Architect",
        description="System design, DDD, architectural patterns",
        keywords=["architecture", "system design", "ddd", "domain", "pattern", "trade-off"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "sre": Agent(
        name="SRE",
        description="SLOs, error budgets, observability, chaos engineering",
        keywords=["sre", "slo", "error budget", "observability", "chaos", "reliability"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "ai-data-remediation": Agent(
        name="AI Data Remediation Engineer",
        description="Self-healing pipelines, air-gapped SLMs, semantic clustering",
        keywords=["data remediation", "pipeline", "slm", "semantic", "clustering"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "data-engineer": Agent(
        name="Data Engineer",
        description="Data pipelines, lakehouse architecture, ETL/ELT",
        keywords=["data pipeline", "lakehouse", "etl", "elt", "data infrastructure", "warehouse"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "feishu-integration": Agent(
        name="Feishu Integration Developer",
        description="Feishu/Lark Open Platform, bots, workflows",
        keywords=["feishu", "lark", "bot", "workflow", "integration"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "cms-developer": Agent(
        name="CMS Developer",
        description="WordPress & Drupal themes, plugins/modules",
        keywords=["cms", "wordpress", "drupal", "theme", "plugin", "module"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "email-intelligence": Agent(
        name="Email Intelligence Engineer",
        description="Email parsing, MIME extraction, structured data for AI agents",
        keywords=["email", "mime", "parsing", "structured data"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "voice-ai": Agent(
        name="Voice AI Integration Engineer",
        description="Speech-to-text pipelines, Whisper, ASR, speaker diarization",
        keywords=["voice", "speech", "whisper", "asr", "diarization", "transcription"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "it-service-manager": Agent(
        name="IT Service Manager",
        description="ITIL 4 service management",
        keywords=["itil", "service management", "incident", "problem", "change", "sla", "cmdb"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "minimal-change": Agent(
        name="Minimal Change Engineer",
        description="Minimum-viable diffs, no scope creep",
        keywords=["minimal change", "diff", "scope", "fix only"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "orgscript-engineer": Agent(
        name="OrgScript Engineer",
        description="OrgScript grammar & AST validation",
        keywords=["orgscript", "grammar", "ast", "business logic"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "prompt-engineer": Agent(
        name="Prompt Engineer",
        description="LLM prompt design & optimization",
        keywords=["prompt", "llm prompt", "prompt design", "prompt optimization"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "multi-agent-architect": Agent(
        name="Multi-Agent Systems Architect",
        description="Multi-agent pipeline design & governance",
        keywords=["multi-agent", "agent pipeline", "topology", "governance", "agent system"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "drupal-shopping-cart": Agent(
        name="Drupal Shopping Cart Engineer",
        description="Drupal Commerce storefronts",
        keywords=["drupal commerce", "shopping cart", "catalog", "checkout", "drupal 10", "drupal 11"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),
    "wordpress-shopping-cart": Agent(
        name="WordPress Shopping Cart Engineer",
        description="WooCommerce storefronts",
        keywords=["woocommerce", "shopping cart", "catalog", "checkout", "wordpress"],
        tool="opencode", model="qwen3:8b", division="Engineering"
    ),

    # ============================================================
    # DESIGN DIVISION
    # ============================================================
    "ui-designer": Agent(
        name="UI Designer",
        description="Visual design, component libraries, design systems",
        keywords=["design", "ui", "visual", "component", "figma", "sketch", "palette", "typography", "icon", "layout", "design system"],
        tool="opencode", model="qwen3:8b", division="Design"
    ),
    "ux-researcher": Agent(
        name="UX Researcher",
        description="User testing, behavior analysis, research",
        keywords=["ux", "user testing", "behavior", "research", "usability", "interview"],
        tool="opencode", model="qwen3:8b", division="Design"
    ),
    "ux-architect": Agent(
        name="UX Architect",
        description="Technical architecture, CSS systems, implementation",
        keywords=["ux architect", "css system", "technical", "implementation"],
        tool="opencode", model="qwen3:8b", division="Design"
    ),
    "brand-guardian": Agent(
        name="Brand Guardian",
        description="Brand identity, consistency, positioning",
        keywords=["brand", "identity", "consistency", "positioning", "guideline"],
        tool="opencode", model="qwen3:8b", division="Design"
    ),
    "visual-storyteller": Agent(
        name="Visual Storyteller",
        description="Visual narratives, multimedia content",
        keywords=["visual", "storytelling", "narrative", "multimedia"],
        tool="opencode", model="qwen3:8b", division="Design"
    ),
    "whimsy-injector": Agent(
        name="Whimsy Injector",
        description="Personality, delight, playful interactions",
        keywords=["whimsy", "delight", "playful", "micro-interaction", "easter egg", "personality"],
        tool="opencode", model="qwen3:8b", division="Design"
    ),
    "image-prompt-engineer": Agent(
        name="Image Prompt Engineer",
        description="AI image generation prompts, photography",
        keywords=["image prompt", "midjourney", "dalle", "stable diffusion", "photography prompt"],
        tool="opencode", model="qwen3:8b", division="Design"
    ),
    "inclusive-visuals": Agent(
        name="Inclusive Visuals Specialist",
        description="Representation, bias mitigation, authentic imagery",
        keywords=["inclusive", "representation", "bias", "cultural", "imagery"],
        tool="opencode", model="qwen3:8b", division="Design"
    ),
    "persona-walkthrough": Agent(
        name="Persona Walkthrough Specialist",
        description="Persona-driven cognitive walkthroughs",
        keywords=["persona", "walkthrough", "cognitive", "simulation", "friction"],
        tool="opencode", model="qwen3:8b", division="Design"
    ),

    # ============================================================
    # PAID MEDIA DIVISION
    # ============================================================
    "ppc-strategist": Agent(
        name="PPC Campaign Strategist",
        description="Google/Microsoft/Amazon Ads, account architecture, bidding",
        keywords=["ppc", "google ads", "microsoft ads", "amazon ads", "bidding", "account architecture"],
        tool="opencode", model="qwen3:8b", division="Paid Media"
    ),
    "search-query-analyst": Agent(
        name="Search Query Analyst",
        description="Search term analysis, negative keywords, intent mapping",
        keywords=["search query", "negative keyword", "intent", "search term", "audit"],
        tool="opencode", model="qwen3:8b", division="Paid Media"
    ),
    "paid-media-auditor": Agent(
        name="Paid Media Auditor",
        description="200+ point account audits, competitive analysis",
        keywords=["audit", "paid media", "competitive analysis", "account takeover"],
        tool="opencode", model="qwen3:8b", division="Paid Media"
    ),
    "tracking-measurement": Agent(
        name="Tracking & Measurement Specialist",
        description="GTM, GA4, conversion tracking, CAPI",
        keywords=["gtm", "ga4", "conversion tracking", "capi", "measurement"],
        tool="opencode", model="qwen3:8b", division="Paid Media"
    ),
    "ad-creative-strategist": Agent(
        name="Ad Creative Strategist",
        description="RSA copy, Meta creative, Performance Max assets",
        keywords=["ad creative", "rsa", "meta creative", "performance max", "creative testing"],
        tool="opencode", model="qwen3:8b", division="Paid Media"
    ),
    "programmatic-buyer": Agent(
        name="Programmatic & Display Buyer",
        description="GDN, DSPs, partner media, ABM display",
        keywords=["programmatic", "gdn", "dsp", "display", "abm"],
        tool="opencode", model="qwen3:8b", division="Paid Media"
    ),
    "paid-social-strategist": Agent(
        name="Paid Social Strategist",
        description="Meta, LinkedIn, TikTok, cross-platform social",
        keywords=["paid social", "meta", "linkedin", "tiktok", "social ads"],
        tool="opencode", model="qwen3:8b", division="Paid Media"
    ),

    # ============================================================
    # SALES DIVISION
    # ============================================================
    "outbound-strategist": Agent(
        name="Outbound Strategist",
        description="Signal-based prospecting, multi-channel sequences, ICP targeting",
        keywords=["outbound", "prospecting", "sequence", "icp", "pipeline"],
        tool="opencode", model="qwen3:8b", division="Sales"
    ),
    "discovery-coach": Agent(
        name="Discovery Coach",
        description="SPIN, Gap Selling, Sandler - question design and call structure",
        keywords=["discovery", "spin", "gap selling", "sandler", "qualify", "call"],
        tool="opencode", model="qwen3:8b", division="Sales"
    ),
    "deal-strategist": Agent(
        name="Deal Strategist",
        description="MEDDPICC qualification, competitive positioning, win planning",
        keywords=["deal", "meddpicc", "competitive", "win plan", "pipeline risk"],
        tool="opencode", model="qwen3:8b", division="Sales"
    ),
    "sales-engineer": Agent(
        name="Sales Engineer",
        description="Technical demos, POC scoping, competitive battlecards",
        keywords=["sales engineer", "demo", "poc", "battlecard", "pre-sales"],
        tool="opencode", model="qwen3:8b", division="Sales"
    ),
    "proposal-strategist": Agent(
        name="Proposal Strategist",
        description="RFP response, win themes, narrative structure",
        keywords=["proposal", "rfp", "win theme", "narrative", "persuade"],
        tool="opencode", model="qwen3:8b", division="Sales"
    ),
    "pipeline-analyst": Agent(
        name="Pipeline Analyst",
        description="Forecasting, pipeline health, deal velocity, RevOps",
        keywords=["pipeline", "forecast", "velocity", "revops", "deal"],
        tool="opencode", model="qwen3:8b", division="Sales"
    ),
    "account-strategist": Agent(
        name="Account Strategist",
        description="Land-and-expand, QBRs, stakeholder mapping",
        keywords=["account", "land and expand", "qbr", "stakeholder", "nrr"],
        tool="opencode", model="qwen3:8b", division="Sales"
    ),
    "sales-coach": Agent(
        name="Sales Coach",
        description="Rep development, call coaching, pipeline review facilitation",
        keywords=["sales coach", "rep development", "call coaching", "pipeline review"],
        tool="opencode", model="qwen3:8b", division="Sales"
    ),
    "sales-outreach": Agent(
        name="Sales Outreach",
        description="Cold prospecting, multi-touch cadences, objection handling",
        keywords=["sales outreach", "cold email", "cadence", "objection", "b2b"],
        tool="opencode", model="qwen3:8b", division="Sales"
    ),
    "offer-lead-gen": Agent(
        name="Offer & Lead Gen Strategist",
        description="Offers & lead magnets",
        keywords=["offer", "lead magnet", "lead gen", "top of funnel"],
        tool="opencode", model="qwen3:8b", division="Sales"
    ),

    # ============================================================
    # MARKETING DIVISION
    # ============================================================
    "growth-hacker": Agent(
        name="Growth Hacker",
        description="Rapid user acquisition, viral loops, experiments",
        keywords=["growth", "viral", "acquisition", "experiment", "conversion", "a/b test"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "content-creator": Agent(
        name="Content Creator",
        description="Multi-platform content, editorial calendars",
        keywords=["content", "copywriting", "editorial", "calendar", "blog", "social"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "twitter-engager": Agent(
        name="Twitter Engager",
        description="Real-time engagement, thought leadership",
        keywords=["twitter", "x", "engagement", "thought leadership", "social"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "twitter-intelligence": Agent(
        name="X/Twitter Intelligence Analyst",
        description="Social listening, trend detection, account monitoring",
        keywords=["twitter intelligence", "social listening", "trend", "monitoring", "brand risk"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "tiktok-strategist": Agent(
        name="TikTok Strategist",
        description="Viral content, algorithm optimization",
        keywords=["tiktok", "viral", "algorithm", "short video", "gen z"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "instagram-curator": Agent(
        name="Instagram Curator",
        description="Visual storytelling, community building",
        keywords=["instagram", "visual", "community", "aesthetic", "story"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "reddit-community": Agent(
        name="Reddit Community Builder",
        description="Authentic engagement, value-driven content",
        keywords=["reddit", "community", "authentic", "engagement", "value"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "app-store-optimizer": Agent(
        name="App Store Optimizer",
        description="ASO, conversion optimization, discoverability",
        keywords=["aso", "app store", "conversion", "discoverability", "app marketing"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "social-media-strategist": Agent(
        name="Social Media Strategist",
        description="Cross-platform strategy, campaigns",
        keywords=["social media", "cross-platform", "campaign", "strategy"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "xiaohongshu": Agent(
        name="Xiaohongshu Specialist",
        description="Lifestyle content, trend-driven strategy",
        keywords=["xiaohongshu", "lifestyle", "trend", "gen z", "aesthetic"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "wechat-official": Agent(
        name="WeChat Official Account Manager",
        description="Subscriber engagement, content marketing",
        keywords=["wechat official", "subscriber", "content marketing", "weixin"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "zhihu-strategist": Agent(
        name="Zhihu Strategist",
        description="Thought leadership, knowledge-driven engagement",
        keywords=["zhihu", "thought leadership", "knowledge", "q&a", "lead generation"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "baidu-seo": Agent(
        name="Baidu SEO Specialist",
        description="Baidu optimization, China SEO, ICP compliance",
        keywords=["baidu", "china seo", "icp", "china search"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "bilibili": Agent(
        name="Bilibili Content Strategist",
        description="Bilibili algorithm, danmaku culture, UP growth",
        keywords=["bilibili", "danmaku", "up主", "community"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "carousel-growth": Agent(
        name="Carousel Growth Engine",
        description="TikTok/Instagram carousels, autonomous publishing",
        keywords=["carousel", "tiktok carousel", "instagram carousel", "publishing"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "linkedin-creator": Agent(
        name="LinkedIn Content Creator",
        description="Personal branding, thought leadership, professional content",
        keywords=["linkedin", "personal brand", "thought leadership", "b2b content"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "china-ecommerce": Agent(
        name="China E-Commerce Operator",
        description="Taobao, Tmall, Pinduoduo, live commerce",
        keywords=["taobao", "tmall", "pinduoduo", "live commerce", "china ecommerce"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "kuaishou": Agent(
        name="Kuaishou Strategist",
        description="Kuaishou, community, grassroots growth",
        keywords=["kuaishou", "grassroots", "community"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "seo-specialist": Agent(
        name="SEO Specialist",
        description="Technical SEO, content strategy, link building",
        keywords=["seo", "technical seo", "link building", "organic search"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "book-co-author": Agent(
        name="Book Co-Author",
        description="Thought-leadership books, ghostwriting, publishing",
        keywords=["book", "ghostwriting", "publishing", "thought leadership"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "cross-border-ecommerce": Agent(
        name="Cross-Border E-Commerce Specialist",
        description="Amazon, Shopee, Lazada, cross-border fulfillment",
        keywords=["cross-border", "amazon", "shopee", "lazada", "fulfillment"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "douyin-strategist": Agent(
        name="Douyin Strategist",
        description="Douyin platform, short-video marketing, algorithm",
        keywords=["douyin", "short video", "algorithm", "china"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "livestream-commerce": Agent(
        name="Livestream Commerce Coach",
        description="Host training, live room optimization, conversion",
        keywords=["livestream", "commerce", "host training", "conversion"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "podcast-strategist-cn": Agent(
        name="Podcast Strategist (CN)",
        description="Chinese podcast market strategy and operations",
        keywords=["podcast", "china podcast", "audio", "strategy"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "private-domain": Agent(
        name="Private Domain Operator",
        description="WeCom, private traffic, community operations",
        keywords=["private domain", "wecom", "private traffic", "community"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "short-video-editor": Agent(
        name="Short-Video Editing Coach",
        description="Post-production, editing workflows, platform specs",
        keywords=["short video", "editing", "post-production", "workflow"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "weibo-strategist": Agent(
        name="Weibo Strategist",
        description="Sina Weibo, trending topics, fan engagement",
        keywords=["weibo", "sina", "trending", "fan", "engagement"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "podcast-strategist-global": Agent(
        name="Global Podcast Strategist",
        description="Show positioning, audience growth, monetisation",
        keywords=["podcast", "show positioning", "audience growth", "monetisation", "sponsorship"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "ai-citation": Agent(
        name="AI Citation Strategist",
        description="AEO/GEO, AI recommendation visibility, citation auditing",
        keywords=["aeo", "geo", "ai citation", "chatgpt", "claude", "gemini", "perplexity"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "china-localization": Agent(
        name="China Market Localization Strategist",
        description="Full-stack China market localization, Douyin/Xiaohongshu/WeChat GTM",
        keywords=["china localization", "gtm", "china market", "localization"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "video-optimization": Agent(
        name="Video Optimization Specialist",
        description="YouTube algorithm strategy, chaptering, thumbnail concepts",
        keywords=["youtube", "video optimization", "thumbnail", "chapter", "audience retention"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "aeo-foundations": Agent(
        name="AEO Foundations Architect",
        description="AI Engine Optimization infrastructure",
        keywords=["aeo", "llms.txt", "robots.txt", "agent discovery"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "agentic-search": Agent(
        name="Agentic Search Optimizer",
        description="WebMCP & agentic task completion",
        keywords=["agentic search", "webmcp", "agent browsing", "task completion"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "email-marketing": Agent(
        name="Email Marketing Strategist",
        description="Lifecycle email & deliverability",
        keywords=["email marketing", "lifecycle", "deliverability", "crm", "automation"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "multi-platform-publisher": Agent(
        name="Multi-Platform Publisher",
        description="One-click Chinese multi-platform publishing",
        keywords=["multi-platform", "publishing", "zhihu", "xiaohongshu", "csdn", "bilibili"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),
    "pr-communications": Agent(
        name="PR & Communications Manager",
        description="PR, media relations & crisis comms",
        keywords=["pr", "communications", "media relations", "crisis", "press release"],
        tool="opencode", model="qwen3:8b", division="Marketing"
    ),

    # ============================================================
    # PRODUCT DIVISION
    # ============================================================
    "sprint-prioritizer": Agent(
        name="Sprint Prioritizer",
        description="Agile planning, feature prioritization",
        keywords=["sprint", "agile", "prioritization", "backlog", "feature"],
        tool="opencode", model="qwen3:8b", division="Product"
    ),
    "trend-researcher": Agent(
        name="Trend Researcher",
        description="Market intelligence, competitive analysis",
        keywords=["trend", "market intelligence", "competitive analysis", "opportunity"],
        tool="opencode", model="qwen3:8b", division="Product"
    ),
    "feedback-synthesizer": Agent(
        name="Feedback Synthesizer",
        description="User feedback analysis, insights extraction",
        keywords=["feedback", "user feedback", "insights", "synthesis", "analysis"],
        tool="opencode", model="qwen3:8b", division="Product"
    ),
    "behavioral-nudge": Agent(
        name="Behavioral Nudge Engine",
        description="Behavioral psychology, nudge design, engagement",
        keywords=["behavioral", "nudge", "psychology", "engagement", "motivation"],
        tool="opencode", model="qwen3:8b", division="Product"
    ),
    "product-manager": Agent(
        name="Product Manager",
        description="Full lifecycle product ownership",
        keywords=["product manager", "prd", "roadmap", "discovery", "gtm", "outcome"],
        tool="opencode", model="qwen3:8b", division="Product"
    ),

    # ============================================================
    # PROJECT MANAGEMENT DIVISION
    # ============================================================
    "studio-producer": Agent(
        name="Studio Producer",
        description="High-level orchestration, portfolio management",
        keywords=["producer", "orchestration", "portfolio", "multi-project"],
        tool="opencode", model="qwen3:8b", division="Project Management"
    ),
    "project-shepherd": Agent(
        name="Project Shepherd",
        description="Cross-functional coordination, timeline management",
        keywords=["project", "coordination", "timeline", "stakeholder", "cross-functional"],
        tool="opencode", model="qwen3:8b", division="Project Management"
    ),
    "studio-operations": Agent(
        name="Studio Operations",
        description="Day-to-day efficiency, process optimization",
        keywords=["operations", "efficiency", "process", "optimization", "productivity"],
        tool="opencode", model="qwen3:8b", division="Project Management"
    ),
    "experiment-tracker": Agent(
        name="Experiment Tracker",
        description="A/B tests, hypothesis validation",
        keywords=["experiment", "a/b test", "hypothesis", "validation"],
        tool="opencode", model="qwen3:8b", division="Project Management"
    ),
    "senior-project-manager": Agent(
        name="Senior Project Manager",
        description="Realistic scoping, task conversion",
        keywords=["project manager", "scoping", "task", "specs", "scope"],
        tool="opencode", model="qwen3:8b", division="Project Management"
    ),
    "jira-workflow": Agent(
        name="Jira Workflow Steward",
        description="Git workflow, branch strategy, traceability",
        keywords=["jira", "git workflow", "branch", "traceability", "delivery"],
        tool="opencode", model="qwen3:8b", division="Project Management"
    ),
    "meeting-notes": Agent(
        name="Meeting Notes Specialist",
        description="Structured meeting summaries",
        keywords=["meeting", "notes", "summary", "action items", "decisions"],
        tool="opencode", model="qwen3:8b", division="Project Management"
    ),

    # ============================================================
    # TESTING DIVISION
    # ============================================================
    "evidence-collector": Agent(
        name="Evidence Collector",
        description="Screenshot-based QA, visual proof",
        keywords=["evidence", "screenshot", "qa", "visual", "bug documentation"],
        tool="opencode", model="qwen3:8b", division="Testing"
    ),
    "reality-checker": Agent(
        name="Reality Checker",
        description="Evidence-based certification, quality gates",
        keywords=["reality check", "certification", "quality gate", "production ready"],
        tool="opencode", model="qwen3:8b", division="Testing"
    ),
    "test-results-analyzer": Agent(
        name="Test Results Analyzer",
        description="Test evaluation, metrics analysis",
        keywords=["test results", "metrics", "analysis", "coverage", "quality"],
        tool="opencode", model="qwen3:8b", division="Testing"
    ),
    "performance-benchmarker": Agent(
        name="Performance Benchmarker",
        description="Performance testing, optimization",
        keywords=["performance", "benchmark", "load test", "speed", "optimization"],
        tool="opencode", model="qwen3:8b", division="Testing"
    ),
    "api-tester": Agent(
        name="API Tester",
        description="API validation, integration testing",
        keywords=["api test", "integration", "endpoint", "validation"],
        tool="opencode", model="qwen3:8b", division="Testing"
    ),
    "tool-evaluator": Agent(
        name="Tool Evaluator",
        description="Technology assessment, tool selection",
        keywords=["tool", "evaluation", "assessment", "technology", "selection"],
        tool="opencode", model="qwen3:8b", division="Testing"
    ),
    "workflow-optimizer": Agent(
        name="Workflow Optimizer",
        description="Process analysis, workflow improvement",
        keywords=["workflow", "process", "optimization", "efficiency", "automation"],
        tool="opencode", model="qwen3:8b", division="Testing"
    ),
    "accessibility-auditor": Agent(
        name="Accessibility Auditor",
        description="WCAG auditing, assistive technology testing",
        keywords=["accessibility", "wcag", "screen reader", "assistive", "inclusive"],
        tool="opencode", model="qwen3:8b", division="Testing"
    ),

    # ============================================================
    # SECURITY DIVISION
    # ============================================================
    "security-architect": Agent(
        name="Security Architect",
        description="Threat modeling, secure-by-design, trust boundaries",
        keywords=["security architect", "threat model", "secure by design", "trust boundary"],
        tool="opencode", model="qwen3:8b", division="Security"
    ),
    "appsec-engineer": Agent(
        name="Application Security Engineer",
        description="SDLC security, SAST/DAST, secure code review",
        keywords=["appsec", "sdlc", "sast", "dast", "secure code", "vulnerability"],
        tool="opencode", model="qwen3:8b", division="Security"
    ),
    "penetration-tester": Agent(
        name="Penetration Tester",
        description="Authorized pentests, red team ops, exploitation",
        keywords=["pentest", "penetration", "red team", "exploitation", "security test"],
        tool="opencode", model="qwen3:8b", division="Security"
    ),
    "cloud-security": Agent(
        name="Cloud Security Architect",
        description="Zero trust, cloud-native defense-in-depth",
        keywords=["cloud security", "zero trust", "defense in depth", "cloud native"],
        tool="opencode", model="qwen3:8b", division="Security"
    ),
    "incident-responder": Agent(
        name="Incident Responder",
        description="DFIR, breach investigation, threat containment",
        keywords=["incident response", "dfir", "breach", "forensics", "containment"],
        tool="opencode", model="qwen3:8b", division="Security"
    ),
    "threat-intelligence": Agent(
        name="Threat Intelligence Analyst",
        description="Adversary tracking, campaign mapping, ATT&CK",
        keywords=["threat intelligence", "adversary", "att&ck", "campaign", "tracking"],
        tool="opencode", model="qwen3:8b", division="Security"
    ),
    "threat-detection": Agent(
        name="Threat Detection Engineer",
        description="SIEM rules, threat hunting, ATT&CK mapping",
        keywords=["threat detection", "siem", "threat hunting", "att&ck", "detection"],
        tool="opencode", model="qwen3:8b", division="Security"
    ),
    "secops-engineer": Agent(
        name="Senior SecOps Engineer",
        description="Secrets scanning, secure-by-default submissions",
        keywords=["secops", "secrets", "scanning", "secure by default"],
        tool="opencode", model="qwen3:8b", division="Security"
    ),
    "compliance-auditor": Agent(
        name="Compliance Auditor",
        description="SOC 2, ISO 27001, HIPAA, PCI-DSS",
        keywords=["compliance", "soc 2", "iso 27001", "hipaa", "pci-dss", "audit"],
        tool="opencode", model="qwen3:8b", division="Security"
    ),
    "blockchain-security": Agent(
        name="Blockchain Security Auditor",
        description="Smart contract audits, exploit analysis",
        keywords=["blockchain security", "smart contract audit", "exploit"],
        tool="opencode", model="qwen3:8b", division="Security"
    ),

    # ============================================================
    # SUPPORT DIVISION
    # ============================================================
    "support-responder": Agent(
        name="Support Responder",
        description="Customer service, issue resolution",
        keywords=["support", "customer service", "issue", "resolution", "help desk"],
        tool="opencode", model="qwen3:8b", division="Support"
    ),
    "analytics-reporter": Agent(
        name="Analytics Reporter",
        description="Data analysis, dashboards, insights",
        keywords=["analytics", "dashboard", "kpi", "business intelligence", "data visualization"],
        tool="opencode", model="qwen3:8b", division="Support"
    ),
    "finance-tracker": Agent(
        name="Finance Tracker",
        description="Financial planning, budget management",
        keywords=["finance", "budget", "cash flow", "financial planning"],
        tool="opencode", model="qwen3:8b", division="Support"
    ),
    "infrastructure-maintainer": Agent(
        name="Infrastructure Maintainer",
        description="System reliability, performance optimization",
        keywords=["infrastructure", "reliability", "performance", "monitoring", "system"],
        tool="opencode", model="qwen3:8b", division="Support"
    ),
    "legal-compliance": Agent(
        name="Legal Compliance Checker",
        description="Compliance, regulations, legal review",
        keywords=["legal", "compliance", "regulation", "risk", "review"],
        tool="opencode", model="qwen3:8b", division="Support"
    ),
    "executive-summary": Agent(
        name="Executive Summary Generator",
        description="C-suite communication, strategic summaries",
        keywords=["executive", "summary", "c-suite", "strategic", "reporting"],
        tool="opencode", model="qwen3:8b", division="Support"
    ),

    # ============================================================
    # SPATIAL COMPUTING DIVISION
    # ============================================================
    "xr-interface": Agent(
        name="XR Interface Architect",
        description="Spatial interaction design, immersive UX",
        keywords=["xr", "ar", "vr", "spatial", "immersive", "interface"],
        tool="opencode", model="qwen3:8b", division="Spatial Computing"
    ),
    "macos-spatial": Agent(
        name="macOS Spatial/Metal Engineer",
        description="Swift, Metal, high-performance 3D",
        keywords=["macos", "spatial", "metal", "swift", "3d", "vision pro"],
        tool="opencode", model="qwen3:8b", division="Spatial Computing"
    ),
    "xr-immersive": Agent(
        name="XR Immersive Developer",
        description="WebXR, browser-based AR/VR",
        keywords=["webxr", "browser", "ar", "vr", "immersive", "web"],
        tool="opencode", model="qwen3:8b", division="Spatial Computing"
    ),
    "xr-cockpit": Agent(
        name="XR Cockpit Interaction Specialist",
        description="Cockpit-based controls, immersive systems",
        keywords=["cockpit", "control", "immersive system", "xr cockpit"],
        tool="opencode", model="qwen3:8b", division="Spatial Computing"
    ),
    "visionos": Agent(
        name="visionOS Spatial Engineer",
        description="Apple Vision Pro development",
        keywords=["visionos", "vision pro", "apple", "spatial computing"],
        tool="opencode", model="qwen3:8b", division="Spatial Computing"
    ),
    "terminal-integration": Agent(
        name="Terminal Integration Specialist",
        description="Terminal integration, command-line tools",
        keywords=["terminal", "cli", "command line", "integration", "developer tool"],
        tool="opencode", model="qwen3:8b", division="Spatial Computing"
    ),

    # ============================================================
    # SPECIALIZED DIVISION
    # ============================================================
    "agents-orchestrator": Agent(
        name="Agents Orchestrator",
        description="Multi-agent coordination, workflow management",
        keywords=["orchestrator", "multi-agent", "coordination", "workflow"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "lsp-index": Agent(
        name="LSP/Index Engineer",
        description="Language Server Protocol, code intelligence",
        keywords=["lsp", "language server", "code intelligence", "semantic", "index"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "sales-data-extraction": Agent(
        name="Sales Data Extraction Agent",
        description="Excel monitoring, sales metric extraction",
        keywords=["sales data", "excel", "metric", "extraction", "mtd", "ytd"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "data-consolidation": Agent(
        name="Data Consolidation Agent",
        description="Sales data aggregation, dashboard reports",
        keywords=["data consolidation", "aggregation", "dashboard", "territory", "performance"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "report-distribution": Agent(
        name="Report Distribution Agent",
        description="Automated report delivery",
        keywords=["report", "distribution", "automated", "territory", "scheduled"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "agentic-identity": Agent(
        name="Agentic Identity & Trust Architect",
        description="Agent identity, authentication, trust verification",
        keywords=["agent identity", "authentication", "trust", "multi-agent", "authorization"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "identity-graph": Agent(
        name="Identity Graph Operator",
        description="Shared identity resolution for multi-agent systems",
        keywords=["identity graph", "entity", "deduplication", "merge", "cross-agent"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "accounts-payable": Agent(
        name="Accounts Payable Agent",
        description="Payment processing, vendor management, audit",
        keywords=["accounts payable", "payment", "vendor", "audit", "crypto", "fiat"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "cultural-intelligence": Agent(
        name="Cultural Intelligence Strategist",
        description="Global UX, representation, cultural exclusion",
        keywords=["cultural", "global ux", "representation", "cultural exclusion"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "developer-advocate": Agent(
        name="Developer Advocate",
        description="Community building, DX, developer content",
        keywords=["developer advocate", "community", "dx", "developer content"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "model-qa": Agent(
        name="Model QA Specialist",
        description="ML audits, feature analysis, interpretability",
        keywords=["model qa", "ml audit", "feature analysis", "interpretability"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "zk-steward": Agent(
        name="ZK Steward",
        description="Knowledge management, Zettelkasten, notes",
        keywords=["zettelkasten", "knowledge", "notes", "connected", "validated"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "mcp-builder": Agent(
        name="MCP Builder",
        description="Model Context Protocol servers, AI agent tooling",
        keywords=["mcp", "model context protocol", "server", "agent tooling"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "document-generator": Agent(
        name="Document Generator",
        description="PDF, PPTX, DOCX, XLSX generation from code",
        keywords=["document", "pdf", "pptx", "docx", "xlsx", "generation"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "automation-governance": Agent(
        name="Automation Governance Architect",
        description="Automation governance, n8n, workflow auditing",
        keywords=["automation governance", "n8n", "workflow", "audit"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "training-designer": Agent(
        name="Corporate Training Designer",
        description="Enterprise training, curriculum development",
        keywords=["training", "curriculum", "enterprise", "learning", "education"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "personal-growth": Agent(
        name="Personal Growth Mentor",
        description="Goal clarity, habit systems, accountability, life strategy",
        keywords=["personal growth", "goal", "habit", "accountability", "mentor"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "government-presales": Agent(
        name="Government Digital Presales Consultant",
        description="China ToG presales, digital transformation",
        keywords=["government", "presales", "tog", "digital transformation", "china"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "healthcare-compliance": Agent(
        name="Healthcare Marketing Compliance",
        description="China healthcare advertising compliance",
        keywords=["healthcare", "compliance", "china", "advertising"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "recruitment-specialist": Agent(
        name="Recruitment Specialist",
        description="Talent acquisition, recruiting operations",
        keywords=["recruitment", "talent", "hiring", "sourcing", "acquisition"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "study-abroad": Agent(
        name="Study Abroad Advisor",
        description="International education, application planning",
        keywords=["study abroad", "education", "application", "us", "uk", "canada", "australia"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "supply-chain": Agent(
        name="Supply Chain Strategist",
        description="Supply chain management, procurement strategy",
        keywords=["supply chain", "procurement", "strategy", "management"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "workflow-architect": Agent(
        name="Workflow Architect",
        description="Workflow discovery, mapping, and specification",
        keywords=["workflow", "discovery", "mapping", "specification", "path"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "salesforce-architect": Agent(
        name="Salesforce Architect",
        description="Multi-cloud Salesforce design, governor limits, integrations",
        keywords=["salesforce", "governor limit", "integration", "org strategy"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "french-consulting": Agent(
        name="French Consulting Market Navigator",
        description="ESN/SI ecosystem, portage salarial, rate positioning",
        keywords=["french consulting", "esn", "si", "portage salarial", "freelance"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "korean-business": Agent(
        name="Korean Business Navigator",
        description="Korean business culture, process, relationship mechanics",
        keywords=["korean business", "relationship", "korea"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "civil-engineer": Agent(
        name="Civil Engineer",
        description="Structural analysis, geotechnical design, global building codes",
        keywords=["civil", "structural", "geotechnical", "building code", "eurocode", "aci", "aisc"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "customer-service": Agent(
        name="Customer Service",
        description="Omnichannel support, complaint handling, retention, escalation",
        keywords=["customer service", "omnichannel", "complaint", "retention", "escalation"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "healthcare-customer-service": Agent(
        name="Healthcare Customer Service",
        description="HIPAA-aware patient support, billing, insurance, emergency routing",
        keywords=["healthcare support", "hipaa", "patient", "billing", "insurance"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "hospitality-guest": Agent(
        name="Hospitality Guest Services",
        description="Reservations, concierge, complaint recovery, loyalty, events",
        keywords=["hospitality", "concierge", "reservation", "loyalty", "hotel", "resort"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "hr-onboarding": Agent(
        name="HR Onboarding",
        description="Pre-boarding, compliance, benefits enrollment, 30-60-90 day plans",
        keywords=["hr", "onboarding", "pre-boarding", "benefits", "compliance"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "language-translator": Agent(
        name="Language Translator",
        description="Spanish to English translation, dialect awareness, cultural context",
        keywords=["translator", "spanish", "english", "translation", "dialect", "cultural"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "legal-billing": Agent(
        name="Legal Billing & Time Tracking",
        description="Time capture, billing narratives, IOLTA compliance, collections",
        keywords=["legal billing", "time tracking", "iolta", "collections", "law firm"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "legal-intake": Agent(
        name="Legal Client Intake",
        description="Prospect qualification, conflict screening, consultation scheduling",
        keywords=["legal intake", "prospect", "conflict", "consultation", "law firm"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "legal-document-review": Agent(
        name="Legal Document Review",
        description="Contract review, risk flagging, version comparison, compliance",
        keywords=["legal document", "contract", "risk", "version", "compliance"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "loan-officer": Agent(
        name="Loan Officer Assistant",
        description="Borrower intake, TRID compliance, pipeline tracking, closing coordination",
        keywords=["loan", "borrower", "trid", "mortgage", "closing", "pipeline"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "real-estate": Agent(
        name="Real Estate Buyer & Seller",
        description="Buyer/seller representation, offers, transaction coordination",
        keywords=["real estate", "buyer", "seller", "offer", "transaction", "residential"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "retail-returns": Agent(
        name="Retail Customer Returns",
        description="Return processing, fraud prevention, exchanges, vendor returns",
        keywords=["retail", "returns", "fraud", "exchange", "vendor"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "business-strategist": Agent(
        name="Business Strategist",
        description="Management-consulting strategy",
        keywords=["business strategy", "consulting", "competitive analysis", "market entry"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "change-management": Agent(
        name="Change Management Consultant",
        description="ADKAR/Kotter/Prosci change",
        keywords=["change management", "adkar", "kotter", "prosci", "transformation"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "chief-of-staff": Agent(
        name="Chief of Staff",
        description="Executive coordination",
        keywords=["chief of staff", "executive", "coordination", "process", "decision"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "customer-success": Agent(
        name="Customer Success Manager",
        description="Onboarding, health & retention",
        keywords=["customer success", "onboarding", "health", "retention", "qbr", "churn"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "grant-writer": Agent(
        name="Grant Writer",
        description="Grant proposals & funding",
        keywords=["grant", "proposal", "funding", "nonprofit", "research"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "medical-billing": Agent(
        name="Medical Billing & Coding Specialist",
        description="ICD-10/CPT/HCPCS & revenue cycle",
        keywords=["medical billing", "icd-10", "cpt", "hcpcs", "revenue cycle", "claims"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "pricing-analyst": Agent(
        name="Pricing Analyst",
        description="Pricing models & margin optimization",
        keywords=["pricing", "margin", "optimization", "competitor", "cost analysis"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "cfo": Agent(
        name="Chief Financial Officer",
        description="Capital allocation & financial strategy",
        keywords=["cfo", "capital", "financial strategy", "treasury", "fp&a", "m&a"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "esg-officer": Agent(
        name="ESG & Sustainability Officer",
        description="ESG programs & disclosure",
        keywords=["esg", "sustainability", "disclosure", "decarbonization", "reporting"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "data-privacy-officer": Agent(
        name="Data Privacy Officer",
        description="GDPR/CCPA privacy compliance",
        keywords=["privacy", "gdpr", "ccpa", "data mapping", "dpia", "consent", "breach"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "operations-manager": Agent(
        name="Operations Manager",
        description="Lean/Six Sigma operations",
        keywords=["operations", "lean", "six sigma", "process mapping", "capacity", "kpi"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "ma-integration": Agent(
        name="M&A Integration Manager",
        description="Post-merger integration",
        keywords=["m&a", "merger", "integration", "day 1", "synergy", "tsa"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "org-psychologist": Agent(
        name="Organizational Psychologist",
        description="Team dynamics & culture health",
        keywords=["organizational psychology", "team dynamics", "culture", "psychological safety", "burnout"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),
    "strategy-duel": Agent(
        name="Strategy Duel Agent",
        description="Game theory & the 36 stratagems",
        keywords=["strategy", "game theory", "stratagem", "adversarial", "simulation"],
        tool="opencode", model="qwen3:8b", division="Specialized"
    ),

    # ============================================================
    # FINANCE DIVISION
    # ============================================================
    "bookkeeper": Agent(
        name="Bookkeeper & Controller",
        description="Month-end close, reconciliation, GAAP compliance, internal controls",
        keywords=["bookkeeper", "controller", "month-end", "reconciliation", "gaap", "audit"],
        tool="opencode", model="qwen3:8b", division="Finance"
    ),
    "financial-analyst": Agent(
        name="Financial Analyst",
        description="Financial modeling, forecasting, scenario analysis, decision support",
        keywords=["financial analyst", "modeling", "forecasting", "scenario", "variance"],
        tool="opencode", model="qwen3:8b", division="Finance"
    ),
    "fpa-analyst": Agent(
        name="FP&A Analyst",
        description="Budgeting, rolling forecasts, variance analysis, business reviews",
        keywords=["fp&a", "budget", "forecast", "variance", "business review"],
        tool="opencode", model="qwen3:8b", division="Finance"
    ),
    "investment-researcher": Agent(
        name="Investment Researcher",
        description="Due diligence, portfolio analysis, asset valuation, equity research",
        keywords=["investment", "due diligence", "portfolio", "valuation", "equity research"],
        tool="opencode", model="qwen3:8b", division="Finance"
    ),
    "tax-strategist": Agent(
        name="Tax Strategist",
        description="Tax optimization, multi-jurisdictional compliance, transfer pricing",
        keywords=["tax", "optimization", "compliance", "transfer pricing", "entity structuring"],
        tool="opencode", model="qwen3:8b", division="Finance"
    ),

    # ============================================================
    # GAME DEVELOPMENT DIVISION
    # ============================================================
    # Cross-Engine
    "game-designer": Agent(
        name="Game Designer",
        description="Systems design, GDD authorship, economy balancing, gameplay loops",
        keywords=["game design", "gdd", "economy", "gameplay loop", "mechanic", "progression"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "level-designer": Agent(
        name="Level Designer",
        description="Layout theory, pacing, encounter design, environmental storytelling",
        keywords=["level", "map", "layout", "pacing", "encounter", "dungeon", "world", "terrain", "tilemap"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "technical-artist": Agent(
        name="Technical Artist",
        description="Shaders, VFX, LOD pipeline, art-to-engine optimization",
        keywords=["technical artist", "shader", "vfx", "lod", "art pipeline"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "game-audio": Agent(
        name="Game Audio Engineer",
        description="FMOD/Wwise, adaptive music, spatial audio, audio budgets",
        keywords=["game audio", "fmod", "wwise", "adaptive music", "spatial audio"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "narrative-designer": Agent(
        name="Narrative Designer",
        description="Story systems, branching dialogue, lore architecture",
        keywords=["narrative", "story", "branching dialogue", "lore", "world building"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    # Unity
    "unity-architect": Agent(
        name="Unity Architect",
        description="ScriptableObjects, data-driven modularity, DOTS/ECS",
        keywords=["unity", "scriptableobject", "dots", "ecs", "data-driven"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "unity-shader": Agent(
        name="Unity Shader Graph Artist",
        description="Shader Graph, HLSL, URP/HDRP, Renderer Features",
        keywords=["unity shader", "shader graph", "hlsl", "urp", "hdrp"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "unity-multiplayer": Agent(
        name="Unity Multiplayer Engineer",
        description="Netcode for GameObjects, Unity Relay/Lobby, server authority",
        keywords=["unity multiplayer", "netcode", "relay", "lobby", "prediction"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "unity-editor": Agent(
        name="Unity Editor Tool Developer",
        description="EditorWindows, AssetPostprocessors, PropertyDrawers, build validation",
        keywords=["unity editor", "editorwindow", "assetpostprocessor", "propertydrawer"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    # Unreal
    "unreal-systems": Agent(
        name="Unreal Systems Engineer",
        description="C++/Blueprint hybrid, GAS, Nanite constraints, memory management",
        keywords=["unreal", "blueprint", "gas", "nanite", "c++", "gameplay ability system"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "unreal-technical-artist": Agent(
        name="Unreal Technical Artist",
        description="Material Editor, Niagara, PCG, Substrate",
        keywords=["unreal", "material", "niagara", "pcg", "substrate", "vfx"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "unreal-multiplayer": Agent(
        name="Unreal Multiplayer Architect",
        description="Actor replication, GameMode/GameState hierarchy, dedicated server",
        keywords=["unreal multiplayer", "replication", "gamemode", "dedicated server"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "unreal-world-builder": Agent(
        name="Unreal World Builder",
        description="World Partition, Landscape, HLOD, LWC",
        keywords=["unreal", "world partition", "landscape", "hlod", "open world"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    # Godot
    "godot-scripter": Agent(
        name="Godot Gameplay Scripter",
        description="GDScript 2.0, signals, composition, static typing",
        keywords=["godot", "gdscript", "signal", "composition", "scene"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "godot-multiplayer": Agent(
        name="Godot Multiplayer Engineer",
        description="MultiplayerAPI, ENet/WebRTC, RPCs, authority model",
        keywords=["godot multiplayer", "multiplayerapi", "enetc", "webrtc", "rpc"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "godot-shader": Agent(
        name="Godot Shader Developer",
        description="Godot shading language, VisualShader, RenderingDevice",
        keywords=["godot shader", "visualshader", "renderingdevice", "compute"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    # Blender
    "blender-addon": Agent(
        name="Blender Addon Engineer",
        description="Blender Python (bpy), custom operators/panels, asset validators, exporters",
        keywords=["blender", "bpy", "addon", "operator", "panel", "asset", "export"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    # Roblox
    "roblox-scripter": Agent(
        name="Roblox Systems Scripter",
        description="Luau, RemoteEvents/Functions, DataStore, server-authoritative module architecture",
        keywords=["roblox", "luau", "remoteevent", "datastore", "server authoritative"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "roblox-designer": Agent(
        name="Roblox Experience Designer",
        description="Engagement loops, monetization, D1/D7 retention, onboarding flow",
        keywords=["roblox", "engagement", "monetization", "retention", "game pass"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),
    "roblox-avatar": Agent(
        name="Roblox Avatar Creator",
        description="UGC pipeline, accessory rigging, Creator Marketplace submission",
        keywords=["roblox", "ugc", "avatar", "accessory", "rigging", "marketplace"],
        tool="opencode", model="qwen3:8b", division="Game Dev"
    ),

    # ============================================================
    # ACADEMIC DIVISION
    # ============================================================
    "anthropologist": Agent(
        name="Anthropologist",
        description="Cultural systems, kinship, rituals, belief systems",
        keywords=["anthropology", "culture", "kinship", "ritual", "belief"],
        tool="opencode", model="qwen3:8b", division="Academic"
    ),
    "geographer": Agent(
        name="Geographer",
        description="Physical/human geography, climate, cartography",
        keywords=["geography", "climate", "cartography", "terrain", "settlement"],
        tool="opencode", model="qwen3:8b", division="Academic"
    ),
    "historian": Agent(
        name="Historian",
        description="Historical analysis, periodization, material culture",
        keywords=["history", "historical", "period", "material culture", "authentic"],
        tool="opencode", model="qwen3:8b", division="Academic"
    ),
    "narratologist": Agent(
        name="Narratologist",
        description="Narrative theory, story structure, character arcs",
        keywords=["narratology", "narrative theory", "story structure", "character arc"],
        tool="opencode", model="qwen3:8b", division="Academic"
    ),
    "psychologist": Agent(
        name="Psychologist",
        description="Personality theory, motivation, cognitive patterns",
        keywords=["psychology", "personality", "motivation", "cognitive", "character"],
        tool="opencode", model="qwen3:8b", division="Academic"
    ),

    # ============================================================
    # GIS DIVISION
    # ============================================================
    "gis-consultant": Agent(
        name="GIS Technical Consultant",
        description="GIS strategy, gap analysis, technology roadmaps, digital transformation",
        keywords=["gis", "strategy", "gap analysis", "roadmap", "geospatial"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),
    "gis-solution-engineer": Agent(
        name="GIS Solution Engineer",
        description="Esri + FOSS4G prototype building, PoC delivery, technical feasibility",
        keywords=["gis", "esri", "foss4g", "prototype", "poc", "feasibility"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),
    "gis-analyst": Agent(
        name="GIS Analyst",
        description="Map production, data QC, symbology, layouts, spatial queries",
        keywords=["gis analyst", "map", "symbology", "spatial query", "data qc"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),
    "spatial-data-engineer": Agent(
        name="Spatial Data Engineer",
        description="Geospatial ETL, format conversion, CRS reprojection, automated pipelines",
        keywords=["spatial data", "etl", "crs", "reprojection", "pipeline"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),
    "geoprocessing": Agent(
        name="Geoprocessing Specialist",
        description="ArcPy, Python Toolbox, Model Builder, batch automation",
        keywords=["geoprocessing", "arcpy", "python toolbox", "model builder", "automation"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),
    "gis-qa": Agent(
        name="GIS QA Engineer",
        description="Topology validation, metadata audit, CRS consistency, accuracy assessment",
        keywords=["gis qa", "topology", "metadata", "crs", "accuracy"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),
    "geoai-ml": Agent(
        name="GeoAI/ML Engineer",
        description="Feature extraction, object detection, semantic segmentation, land cover",
        keywords=["geoai", "ml", "feature extraction", "object detection", "segmentation"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),
    "bim-gis": Agent(
        name="BIM/GIS Specialist",
        description="Revit/IFC to GIS, indoor mapping, digital twin architecture",
        keywords=["bim", "gis", "revit", "ifc", "indoor", "digital twin"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),
    "3d-scene": Agent(
        name="3D & Scene Developer",
        description="Cesium, ArcGIS Scene Viewer, 3D Tiles, point clouds, terrain visualization",
        keywords=["3d scene", "cesium", "3d tiles", "point cloud", "terrain"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),
    "spatial-data-scientist": Agent(
        name="Spatial Data Scientist",
        description="Spatial statistics, clustering, regression, interpolation, point pattern",
        keywords=["spatial", "statistics", "clustering", "regression", "interpolation"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),
    "drone-mapping": Agent(
        name="Drone/Reality Mapping",
        description="Photogrammetry, orthomosaic, DTM/DSM, point cloud classification, 3D mesh",
        keywords=["drone", "photogrammetry", "orthomosaic", "dtm", "dsm", "point cloud"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),
    "web-gis": Agent(
        name="Web GIS Developer",
        description="MapLibre GL JS, ArcGIS JS API, Leaflet, real-time dashboards, REST APIs",
        keywords=["web gis", "maplibre", "arcgis js", "leaflet", "dashboard"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),
    "cartography": Agent(
        name="Cartography Designer",
        description="Color theory, typography, basemap design, visual hierarchy, print and web",
        keywords=["cartography", "color theory", "typography", "basemap", "visual hierarchy"],
        tool="opencode", model="qwen3:8b", division="GIS"
    ),

}

# Keyword-to-tool mapping for quick classification
KEYWORD_TOOLS: Dict[str, str] = {
    # OpenCode agents
    "refactor": "opencode",
    "test": "opencode",
    "microbit": "opencode",
    "micro:bit": "opencode",
    "arduino": "opencode",
    "esp32": "opencode",
    "spiel": "opencode",
    "game": "opencode",
    "html": "opencode",
    "pwa": "opencode",
    "website": "opencode",
    "3d printing": "opencode",
    "elegoo": "opencode",
    "neptune": "opencode",
    "ai model": "opencode",
    "ollama": "opencode",
    "frontend": "opencode",
    "testing": "opencode",
    "level": "opencode",
    "ui design": "opencode",
    "backend": "opencode",
    "api": "opencode",
    "database": "opencode",
    "devops": "opencode",
    "ci/cd": "opencode",
    "network": "opencode",
    "prototype": "opencode",
    "laravel": "opencode",
    "embedded": "opencode",
    "firmware": "opencode",
    "solidity": "opencode",
    "codebase": "opencode",
    "documentation": "opencode",
    "wechat": "opencode",
    "review": "opencode",
    "git": "opencode",
    "architecture": "opencode",
    "sre": "opencode",
    "data pipeline": "opencode",
    "cms": "opencode",
    "wordpress": "opencode",
    "drupal": "opencode",
    "email": "opencode",
    "voice": "opencode",
    "itil": "opencode",
    "prompt": "opencode",
    "multi-agent": "opencode",
    "design": "opencode",
    "ux": "opencode",
    "brand": "opencode",
    "visual": "opencode",
    "whimsy": "opencode",
    "image prompt": "opencode",
    "inclusive": "opencode",
    "persona": "opencode",
    "ppc": "opencode",
    "google ads": "opencode",
    "search query": "opencode",
    "paid media": "opencode",
    "gtm": "opencode",
    "ga4": "opencode",
    "ad creative": "opencode",
    "programmatic": "opencode",
    "paid social": "opencode",
    "outbound": "opencode",
    "discovery": "opencode",
    "deal": "opencode",
    "sales engineer": "opencode",
    "proposal": "opencode",
    "pipeline": "opencode",
    "account": "opencode",
    "sales coach": "opencode",
    "sales outreach": "opencode",
    "offer": "opencode",
    "growth": "opencode",
    "content": "opencode",
    "twitter": "opencode",
    "tiktok": "opencode",
    "instagram": "opencode",
    "reddit": "opencode",
    "aso": "opencode",
    "social media": "opencode",
    "xiaohongshu": "opencode",
    "zhihu": "opencode",
    "baidu": "opencode",
    "bilibili": "opencode",
    "carousel": "opencode",
    "linkedin": "opencode",
    "taobao": "opencode",
    "seo": "opencode",
    "book": "opencode",
    "cross-border": "opencode",
    "douyin": "opencode",
    "livestream": "opencode",
    "podcast": "opencode",
    "private domain": "opencode",
    "weibo": "opencode",
    "aeo": "opencode",
    "agentic": "opencode",
    "email marketing": "opencode",
    "pr": "opencode",
    "sprint": "opencode",
    "agile": "opencode",
    "trend": "opencode",
    "feedback": "opencode",
    "behavioral": "opencode",
    "product manager": "opencode",
    "producer": "opencode",
    "project": "opencode",
    "operations": "opencode",
    "experiment": "opencode",
    "jira": "opencode",
    "meeting": "opencode",
    "evidence": "opencode",
    "reality check": "opencode",
    "test results": "opencode",
    "performance": "opencode",
    "api test": "opencode",
    "tool evaluation": "opencode",
    "workflow": "opencode",
    "accessibility": "opencode",
    "security": "opencode",
    "pentest": "opencode",
    "cloud security": "opencode",
    "incident response": "opencode",
    "threat": "opencode",
    "compliance": "opencode",
    "blockchain": "opencode",
    "support": "opencode",
    "analytics": "opencode",
    "finance": "opencode",
    "infrastructure": "opencode",
    "legal": "opencode",
    "executive": "opencode",
    "xr": "opencode",
    "ar": "opencode",
    "vr": "opencode",
    "webxr": "opencode",
    "visionos": "opencode",
    "terminal": "opencode",
    "orchestrator": "opencode",
    "lsp": "opencode",
    "sales data": "opencode",
    "data consolidation": "opencode",
    "report": "opencode",
    "agent identity": "opencode",
    "identity graph": "opencode",
    "accounts payable": "opencode",
    "cultural": "opencode",
    "developer advocate": "opencode",
    "model qa": "opencode",
    "zettelkasten": "opencode",
    "mcp": "opencode",
    "document": "opencode",
    "automation governance": "opencode",
    "training": "opencode",
    "personal growth": "opencode",
    "government": "opencode",
    "healthcare": "opencode",
    "recruitment": "opencode",
    "study abroad": "opencode",
    "supply chain": "opencode",
    "salesforce": "opencode",
    "civil": "opencode",
    "customer service": "opencode",
    "hospitality": "opencode",
    "hr": "opencode",
    "translator": "opencode",
    "legal billing": "opencode",
    "legal intake": "opencode",
    "legal document": "opencode",
    "loan": "opencode",
    "real estate": "opencode",
    "retail": "opencode",
    "business strategy": "opencode",
    "change management": "opencode",
    "chief of staff": "opencode",
    "customer success": "opencode",
    "grant": "opencode",
    "medical billing": "opencode",
    "pricing": "opencode",
    "cfo": "opencode",
    "esg": "opencode",
    "privacy": "opencode",
    "gdpr": "opencode",
    "m&a": "opencode",
    "organizational psychology": "opencode",
    "strategy duel": "opencode",
    "bookkeeper": "opencode",
    "financial analyst": "opencode",
    "fp&a": "opencode",
    "investment": "opencode",
    "tax": "opencode",
    "game design": "opencode",
    "unity": "opencode",
    "unreal": "opencode",
    "godot": "opencode",
    "blender": "opencode",
    "roblox": "opencode",
    "anthropology": "opencode",
    "geography": "opencode",
    "history": "opencode",
    "narratology": "opencode",
    "psychology": "opencode",
    "gis": "opencode",
    "geospatial": "opencode",
    "spatial data": "opencode",
    "cartography": "opencode",
    "drone": "opencode",
    "photogrammetry": "opencode",
    "bim": "opencode",
    "3d scene": "opencode",

    # Hermes (large projects)
    "plan project": "hermes",
    "project plan": "hermes",
    "architecture": "hermes",
    "large refactoring": "hermes",
    "large refactor": "hermes",
    "system design": "hermes",

    # Open Interpreter
    "create file": "interpreter",
    "open browser": "interpreter",
    "desktop": "interpreter",
    "read pdf": "interpreter",
    "automation": "interpreter",
    "script": "interpreter",
    "command": "interpreter",

    # AI 3D Generator Pro
    "3d modell": "ai3d",
    "3d model": "ai3d",
    "image to 3d": "ai3d",
    "stl": "ai3d",
    "print": "ai3d",
    "mesh": "ai3d",
    "generate 3d": "ai3d",
    "blender": "ai3d",
    "cad": "ai3d"
}

def get_agent_for_prompt(prompt: str) -> Optional[Agent]:
    """Find best agent based on prompt keywords"""
    prompt_lower = prompt.lower()

    best_agent = None
    best_score = 0

    for agent_id, agent in AGENTS.items():
        score = 0
        for keyword in agent.keywords:
            if keyword in prompt_lower:
                score += 1
                # Exact match gets higher score
                if keyword == prompt_lower.strip():
                    score += 5

        if score > best_score:
            best_score = score
            best_agent = agent

    return best_agent

def get_tool_for_prompt(prompt: str) -> str:
    """Quick keyword-based tool detection"""
    prompt_lower = prompt.lower()

    for keyword, tool in KEYWORD_TOOLS.items():
        if keyword in prompt_lower:
            return tool

    # Default to opencode for coding-related prompts
    coding_keywords = ["code", "program", "function", "class", "bug", "error", "fix", "implement", "write"]
    if any(kw in prompt_lower for kw in coding_keywords):
        return "opencode"

    return "interpreter"  # Default fallback
