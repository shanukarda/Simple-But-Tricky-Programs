aliens = []
# Make a million green aliens, worth 5 points
# each. Have them all start in one row.
for alien_num in range(25):
 new_alien = {}
 new_alien['color'] = 'green'
 new_alien['points'] = 5
 new_alien['x'] = 20 * alien_num
 new_alien['y'] = 0
 aliens.append(new_alien)
# Prove the list contains a million aliens.
num_aliens = len(aliens)
print("Number of aliens created:")
print(num_aliens)
print(new_alien)