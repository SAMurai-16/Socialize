/**
 * Content Generation Template Configuration
 * This structure defines the multi-step form for content generation
 */

const contentTemplate = {
  title: "Content Generator",
  steps: [
    {
      step: "Step 1: Content Basics",
      fields: {
        content_type: { 
          label: "Content Type", 
          description: "What type of content? (e.g., article, social post, email, product description)" 
        },
        topic: { 
          label: "Topic/Subject", 
          description: "What is the main topic or subject matter?" 
        },
        audience: { 
          label: "Target Audience", 
          description: "Who is this content for?" 
        }
      }
    },
    {
      step: "Step 2: Style & Requirements",
      fields: {
        tone: { 
          label: "Tone", 
          description: "Desired tone (e.g., professional, casual, persuasive, informative)" 
        },
        style: { 
          label: "Writing Style", 
          description: "Any specific style requirements? (e.g., conversational, technical, storytelling)" 
        },
        keywords: { 
          label: "Keywords/Phrases", 
          description: "Important keywords or phrases to include (comma-separated)" 
        }
      }
    },
    {
      step: "Step 3: Format & Objectives",
      fields: {
        length: { 
          label: "Length", 
          description: "Desired length (e.g., 500 words, 280 characters, 3 paragraphs)" 
        },
        format: { 
          label: "Format", 
          description: "Any formatting requirements? (e.g., bullet points, headings, Q&A)" 
        },
        objective: { 
          label: "Content Objective", 
          description: "What should this content achieve? (e.g., inform, persuade, entertain, CTA)" 
        }
      }
    }
  ]
};

/**
 * Blog Post Specific Template
 */
const blogTemplate = {
  title: "Blog Post Generator",
  steps: [
    {
      step: "Step 1: Basic Info",
      fields: {
        title: { 
          label: "Blog Title", 
          description: "What's the title of your blog?" 
        },
        audience: { 
          label: "Target Audience", 
          description: "Who are you writing for?" 
        }
      }
    },
    {
      step: "Step 2: Style & Tone",
      fields: {
        tone: { 
          label: "Tone", 
          description: "Casual, formal, humorous, etc." 
        },
        keywords: { 
          label: "Keywords", 
          description: "Enter SEO keywords (comma-separated)" 
        }
      }
    },
    {
      step: "Step 3: Length & Call-to-Action",
      fields: {
        length: { 
          label: "Length", 
          description: "Approximate length (e.g., 500 words)" 
        },
        cta: { 
          label: "Call To Action", 
          description: "What do you want the reader to do?" 
        }
      }
    }
  ]
};

/**
 * Function to generate prompt from template data
 */
function generatePromptFromTemplate(templateData) {
  let prompt = `Generate ${templateData.content_type || 'content'} based on the following requirements:\n\n`;
  
  if (templateData.title) prompt += `**Title:** ${templateData.title}\n\n`;
  if (templateData.topic) prompt += `**Topic/Subject:** ${templateData.topic}\n\n`;
  if (templateData.audience) prompt += `**Target Audience:** ${templateData.audience}\n\n`;
  if (templateData.tone) prompt += `**Tone:** ${templateData.tone}\n\n`;
  if (templateData.style) prompt += `**Writing Style:** ${templateData.style}\n\n`;
  if (templateData.keywords) prompt += `**Keywords to Include:** ${templateData.keywords}\n\n`;
  if (templateData.length) prompt += `**Desired Length:** ${templateData.length}\n\n`;
  if (templateData.format) prompt += `**Format Requirements:** ${templateData.format}\n\n`;
  if (templateData.objective) prompt += `**Content Objective:** ${templateData.objective}\n\n`;
  if (templateData.cta) prompt += `**Call To Action:** ${templateData.cta}\n\n`;
  
  prompt += "Please create compelling, well-structured content that meets all these requirements.";
  
  return prompt;
}

/**
 * Function to send content generation request
 */
async function generateContent(formData) {
  try {
    const response = await fetch('/api/generate-content/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        prompt: generatePromptFromTemplate(formData)
      })
    });
    
    const data = await response.json();
    
    if (data.success) {
      return data.content;
    } else {
      throw new Error(data.error || 'Failed to generate content');
    }
  } catch (error) {
    console.error('Error generating content:', error);
    throw error;
  }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { contentTemplate, blogTemplate, generatePromptFromTemplate, generateContent };
}
