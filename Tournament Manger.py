from main import TournamentManager
import time
startTime= time.time()

run=TournamentManager
run.run()

endTime= time.time()
elapsed_Time=endTime-startTime
elapsed_Time=float(str(elapsed_Time)[0:4])
print('Exit...',elapsed_Time,'Seconds')