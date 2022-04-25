#version 410

out vec4 fragColor;

uniform vec2 u_resolution;
uniform float u_time;

void main(){
	vec2 st = gl_FragCoord.xy/u_resolution;
    float pct = 0.0;

    vec3 A = vec3(0.383*abs(cos(u_time)),0.985*abs(sin(u_time)),0.947*tan(cos(u_time)));
    vec3 B = vec3(0.627*abs(cos(u_time)),0.556*abs(tan(u_time)),0.845*abs(cos(u_time)));


    pct = distance(st,vec2(0.5));

    float a = atan(st.x-0.5, st.y-0.5);

    float f = abs(sin(pct+a+7.381*sin(u_time))/1.456)*abs(cos(a/pct *abs(sin(u_time))));

    f = smoothstep(f,f+0.932,pct);

    vec3 color = mix(A/pct/4.144,B+pct,f/pct*abs(sin(u_time)));

	gl_FragColor = vec4( color, 1.0 );
}