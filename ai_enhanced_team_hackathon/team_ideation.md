# 1. Reponu klonla (əgər hələ yoxdursa)
git clone https://github.com/<istifadəçi-adı>/holbertonschool-ai4devs.git
cd holbertonschool-ai4devs

# 2. Qovluğu yarat
mkdir -p ai_enhanced_team_hackathon

# 3. Faylı bura köçür (yüklədiyin faylın yerinə uyğun yol yaz)
cp ~/Downloads/team_ideation.md ai_enhanced_team_hackathon/

# 4. Commit və push et
git add ai_enhanced_team_hackathon/team_ideation.md
git commit -m "Add team ideation"
git push origin main
