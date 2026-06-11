def analyze_ideas(ideas):
    def calculate_time(optimistic, realistic, pessimistic, name_length):
        return ((optimistic + 4 * realistic + pessimistic) / 6) * name_length
    
    ideas = [[idea[0], calculate_time(idea[1], idea[2], idea[3], len(idea[0]))] for idea in ideas]

    ideas.sort(key=lambda idea: idea[1])

    return [idea[0] for idea in ideas]

# print(analyze_ideas([["Add logging", 2, 5, 15], ["SEO optimization", 4, 8, 20], ["Fix bug", 1, 3, 5]]))
# print(analyze_ideas([["Dark mode", 1, 3, 8], ["Real-time collaboration feature", 6, 12, 20], ["Add tooltip", 1, 2, 4]]))
# print(analyze_ideas([["Update user profile page", 3, 7, 14], ["Add pagination", 2, 5, 10], ["Add tags", 2, 3, 6], ["Fix login bug", 1, 4, 8]]))
# print(analyze_ideas([["Migrate database", 14, 25, 40], ["Add chat assistant", 8, 15, 24], ["Redesign onboarding flow", 3, 7, 13], ["Add language support", 6, 11, 18]]))
# print(analyze_ideas([["Add email notifications", 3, 7, 10], ["Migrate deployment flow", 6, 10, 16], ["Add push notifications", 2, 6, 10], ["Optimize continuous integration", 5, 8, 15], ["Analyze user patterns", 5, 10, 18], ["Create onboarding curriculum", 6, 15, 25]]))