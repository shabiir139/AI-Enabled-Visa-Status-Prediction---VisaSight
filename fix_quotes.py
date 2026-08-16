import re
import os

files = {
    'frontend/src/app/auth/login/page.tsx': [(r"Don't have an account\?", r"Don&apos;t have an account?")],
    'frontend/src/app/auth/signup/page.tsx': [(r"Already have an account\?", r"Already have an account?")], # Let's read first
    'frontend/src/app/error.tsx': [(r"We couldn't process your request", r"We couldn&apos;t process your request")],
    'frontend/src/app/not-found.tsx': [(r"The page you're looking for doesn't exist", r"The page you&apos;re looking for doesn&apos;t exist")],
    'frontend/src/app/page.tsx': [(r"Navigate the complexities of US immigration with AI-powered insights, real-time tracking, and predictive approval probabilities.", r"Navigate the complexities of US immigration with AI-powered insights, real-time tracking, and predictive approval probabilities.")]
}
