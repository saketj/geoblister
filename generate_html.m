function [] = generate_html(data,lat,lon,score,ix,K)
data = data(ix(1:K),:); 
lat = (lat(ix(1:K))); lat = reshape(lat,1,[]);
lon = (lon(ix(1:K))); lon = reshape(lon,1,[]);
score = (score(ix(1:K))); score = reshape(score,1,[]);
w = pwd;
cd('data');
csvwrite('timeseries.dat',data);
csvwrite('lat.dat',lat);
csvwrite('lon.dat',lon);
csvwrite('score.dat',score);
cd(w);
disp('Executing the Python Script to generate HTML...');
system('python template_loader.py');
end