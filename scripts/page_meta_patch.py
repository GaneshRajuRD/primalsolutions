import os
import re

root = os.path.join(os.getcwd(), 'pages')

meta_map = {
    'index.vue': {
        'title': 'Primal Solutions | Industrial Consulting for Automotive & Manufacturing',
        'description': 'Primal Solutions delivers consulting, operational excellence, and digital manufacturing services to automotive, FMCG and industrial clients.',
        'keywords': 'industrial consulting, operational excellence, digital factory, lean transformation, automotive consulting, supply chain optimization'
    },
    'about-us.vue': {
        'title': 'About Us | Primal Solutions',
        'description': 'Learn how Primal Solutions supports industrial transformation, lean manufacturing, and business strategy for manufacturing organizations.',
        'keywords': 'about primal solutions, industrial consulting, lean transformation, business strategy, manufacturing consultancy'
    },
    'contact-us.vue': {
        'title': 'Contact Us | Primal Solutions',
        'description': 'Reach out to Primal Solutions for industrial consulting, operational excellence, and manufacturing transformation support.',
        'keywords': 'contact primal solutions, industrial consulting contact, manufacturing consulting inquiry'
    },
    'sectors.vue': {
        'title': 'Sectors | Primal Solutions',
        'description': 'Explore the sectors Primal Solutions serves, including automotive, FMCG, electronics, medical equipment and industrial manufacturing.',
        'keywords': 'manufacturing sectors, automotive sector consulting, fmcg consulting, electronics production consulting'
    },
    'resources.vue': {
        'title': 'Resources | Primal Solutions',
        'description': 'View blogs, case studies and resources focused on manufacturing transformation, operational excellence, and strategic growth.',
        'keywords': 'manufacturing resources, operational excellence case studies, manufacturing blogs, industrial insights'
    },
    'careers.vue': {
        'title': 'Careers | Primal Solutions',
        'description': 'Discover career opportunities at Primal Solutions in industrial consulting, operations, strategy, and manufacturing transformation.',
        'keywords': 'careers primal solutions, industrial consulting jobs, manufacturing consulting careers'
    },
    'privacy-policy.vue': {
        'title': 'Privacy Policy | Primal Solutions',
        'description': 'Read the privacy policy for Primal Solutions and understand how we handle your personal data and website usage information.',
        'keywords': 'privacy policy, data protection, personal information, Primal Solutions privacy'
    },
    'terms-and-conditions.vue': {
        'title': 'Terms & Conditions | Primal Solutions',
        'description': 'Review the terms and conditions for using Primal Solutions website services and consulting information.',
        'keywords': 'terms and conditions, website usage terms, Primal Solutions terms, legal terms'
    },
    'case-study/case-study.vue': {
        'title': 'Case Studies | Primal Solutions',
        'description': 'Explore Primal Solutions case studies showcasing operational excellence, lean transformation, and manufacturing performance improvements.',
        'keywords': 'case studies, manufacturing transformation, lean consulting case studies, industrial success stories'
    }
}

service_pages = {
    'business-strategy.vue': ('Business Strategy', 'Business Strategy Consulting', 'business strategy consulting, manufacturing strategy, operations strategy'),
    'market-research-intelligence-services.vue': ('Market Research & Intelligence Services', 'Market research and intelligence services for manufacturing and industrial clients.', 'market research, intelligence services, manufacturing market insights'),
    'plant-layout-design-optimization.vue': ('Plant Layout Design & Optimization', 'Plant layout design and optimization services for efficient manufacturing operations.', 'plant layout design, manufacturing optimization, factory layout consulting'),
    'operational-excellence-lean-transformation.vue': ('Operational Excellence & Lean Transformation', 'Operational excellence and lean transformation services for manufacturing process improvement.', 'operational excellence, lean transformation, manufacturing improvement'),
    'zero-defect-culture-deployment.vue': ('Zero Defect Culture Deployment', 'Zero-defect culture deployment to improve quality and reduce defects in manufacturing operations.', 'zero defect culture, quality management, manufacturing defect reduction'),
    'digital-smart-factory-transformation.vue': ('Digital & Smart Factory Transformation', 'Digital and smart factory transformation services for connected manufacturing and Industry 4.0.', 'smart factory, digital manufacturing, industry 4.0 consulting'),
    'supplier-capability-performance-enhancement.vue': ('Supplier Capability and Performance Enhancement', 'Supplier capability and performance enhancement services to strengthen supply chain quality.', 'supplier capability, supply chain performance, supplier development'),
    'skill-development-programs-certifications.vue': ('Skill Development Programs and Certifications', 'Skill development programs and certification readiness solutions for manufacturing teams.', 'skill development, training programs, certification readiness'),
    'talent-hiring-management-services.vue': ('Talent Hiring & Management Services', 'Talent hiring and management services designed for manufacturing and industrial organizations.', 'talent hiring, workforce management, manufacturing recruitment')
}

case_study_pages = {
    'prabha-automotive.vue': ('Prabha Automotive Case Study', 'Prabha Automotive case study showcasing supplier excellence and operational improvement.', 'Prabha automotive case study, supplier excellence, manufacturing improvement'),
    'mrlp.vue': ('MRLP Case Study', 'MRLP case study highlighting operational transformation in automotive supply manufacturing.', 'MRLP case study, automotive transformation, manufacturing performance'),
    'sri-kvs.vue': ('Sri KVS Case Study', 'Sri KVS case study demonstrating plant layout and process improvement.', 'Sri KVS case study, plant layout improvement, manufacturing efficiency'),
    'sts-lean.vue': ('STS Lean Case Study', 'STS Lean case study exploring operational excellence and lean transformation.', 'STS Lean case study, lean transformation, operational excellence'),
    'vee-s-vee.vue': ('Vee S Vee Case Study', 'Vee S Vee case study on zero-defect culture and manufacturing performance.', 'Vee S Vee case study, zero defect culture, manufacturing quality')
}

alt_map = {
    '/assets/image/factoryVector.webp': 'Factory illustration',
    '/assets/image/vision.webp': 'Vision illustration',
    '/assets/image/missionImage2.webp': 'Mission illustration',
    '/assets/image/valuesImg.webp': 'Values illustration',
    '/assets/image/Strategic-Planning.png': 'Strategic planning graphic',
    '/assets/image/Operational-Excellence.png': 'Operational excellence graphic',
    '/assets/image/Team-Development.png': 'Team development graphic',
    '/assets/image/Market-Insights.png': 'Market insights graphic',
    '/assets/image/faqImg.webp': 'FAQ illustration',
    '/assets/image/blogImg2.webp': 'Factory floor optimization image',
    '/assets/image/blogImg1.webp': 'Digital smart factory image',
    '/assets/image/caseStudyImg1.webp': 'Operational excellence case study image',
    '/assets/image/careersImg.webp': 'Careers introduction image',
    '/assets/image/careerFormImg.webp': 'Career form illustration',
    '/assets/image/serviceImg1.webp': 'Business strategy illustration',
    '/assets/image/operationsImg.webp': 'Operations improvement image',
    '/assets/image/DigitalSmartFactoryTransformationImg.webp': 'Digital smart factory transformation image',
    '/assets/image/Market ResearchIntelligenceServicesImg.webp': 'Market research intelligence image',
    '/assets/image/ZeroDefectCultureDeploymentImg.webp': 'Zero defect culture deployment image',
    '/assets/image/OptimizeplanlayoutImg.webp': 'Plant layout optimization image',
    '/assets/image/OperationalExcellenceImg.webp': 'Operational excellence image',
    '/assets/image/SupplierCapabilityImg.webp': 'Supplier capability image',
    '/assets/image/TalentHiringManagementServicesImg.webp': 'Talent hiring services image',
    '/assets/image/SkilldevelopmentprogramsImg.webp': 'Skill development programs image',
    '/assets/image/caseStudyImg.webp': 'Case study banner image',
    '/assets/image/Driving Supplier Excellence Under OEM.webp': 'Driving supplier excellence banner image',
    '/assets/image/30 day rapid 1.webp': '30 day rapid transformation banner image',
    '/assets/image/Sheet metal.webp': 'Sheet metal transformation banner image',
    '/assets/image/Transforming legacy automotive supplier for furture growth.webp': 'Legacy automotive supplier transformation banner image',
    '/assets/image/Bar Machining.webp': 'Bar machining transformation banner image'
}


def add_meta(file_path, title, description, keywords):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    if 'definePageMeta' in text or 'useHead' in text:
        return False
    if '<script setup>' not in text:
        return False
    insert = f"\ndefinePageMeta({{
  title: '{title}',
  meta: [
    {{ name: 'description', content: '{description}' }},
    {{ name: 'keywords', content: '{keywords}' }}
  ]
}})\n"
    text = text.replace('<script setup>', '<script setup>' + insert)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    return True


def patch_alt_and_lazy(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    original = text

    def repl_alt(match):
        src = match.group(1)
        alt = alt_map.get(src)
        if alt:
            return match.group(0).replace('alt=""', f'alt="{alt}"')
        return match.group(0)

    text = re.sub(r'src=["\']([^"\']+)["\']([^>]*?)alt=["\']{2}["\']', repl_alt, text)

    def repl_alt_missing(match):
        src = match.group(1)
        attrs = match.group(2)
        alt = alt_map.get(src)
        if alt:
            return f'src="{src}"{attrs} alt="{alt}"'
        return match.group(0)

    text = re.sub(r'src=["\']([^"\']+)["\']([^>]*?)(?<!alt=["\'][^"\']*["\'])(?=>)', repl_alt_missing, text)

    def repl_lazy(match):
        attrs = match.group(1)
        if 'loading=' in attrs.lower():
            return match.group(0)
        if re.search(r'class=["\'][^"\']*(tickImg|icon|Comma|comma)[^"\']*["\']', attrs):
            return match.group(0)
        return f'<img{attrs} loading="lazy">'

    text = re.sub(r'<img\b([^>]*)>', repl_lazy, text)

    if text != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        return True
    return False

changed = []
for dirpath, _, filenames in os.walk(root):
    for name in filenames:
        if not name.endswith('.vue'):
            continue
        rel_path = os.path.relpath(os.path.join(dirpath, name), os.getcwd())
        key = os.path.relpath(os.path.join(dirpath, name), root).replace('\\', '/')
        meta = None
        if key in meta_map:
            meta = meta_map[key]
        elif key.startswith('services/') and key.split('/')[-1] in service_pages:
            title, desc, keywords = service_pages[key.split('/')[-1]]
            meta = {'title': title + ' | Primal Solutions', 'description': desc, 'keywords': keywords}
        elif key.startswith('case-study/') and key.split('/')[-1] in case_study_pages:
            title, desc, keywords = case_study_pages[key.split('/')[-1]]
            meta = {'title': title + ' | Primal Solutions', 'description': desc, 'keywords': keywords}
        if meta:
            file_path = os.path.join(dirpath, name)
            if add_meta(file_path, meta['title'], meta['description'], meta['keywords']):
                changed.append(f'META {rel_path}')
        if patch_alt_and_lazy(os.path.join(dirpath, name)):
            changed.append(f'IMG {rel_path}')

print('Changed files:')
print('\n'.join(changed))
